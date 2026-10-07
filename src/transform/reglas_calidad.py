import logging
from datetime import datetime
from typing import Tuple, List, Dict, Any
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from great_expectations.dataset import SparkDFDataset
from great_expectations.core import ExpectationSuite, ExpectationConfiguration

logger = logging.getLogger(__name__)


class ReglasCalidad:
    """Implementa reglas de calidad de datos usando Great Expectations.
    
    Valida nulidad, rangos, formatos y consistencia entre sistemas.
    Registra los resultados en un checkpoint y genera cuarentena para
    registros que no cumplen los criterios de calidad.
    """
    
    def __init__(self, spark: SparkSession, threshold: float = 0.99):
        self.spark = spark
        self.threshold = threshold
        self.expectation_suite_name = "transacciones_calidad"
        self.quarantine_path = "s3://fintechcorp/quarantine/"
    
    def crear_expectation_suite(self) -> ExpectationSuite:
        """Crea el conjunto de expectativas para validación de transacciones."""
        suite = ExpectationSuite(expectation_suite_name=self.expectation_suite_name)
        
        suite.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_values_to_not_be_null",
                kwargs={
                    "column": "transaction_id",
                    "mostly": self.threshold
                }
            )
        )
        
        suite.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_values_to_be_between",
                kwargs={
                    "column": "amount",
                    "min_value": 0,
                    "max_value": 1000000,
                    "mostly": self.threshold
                }
            )
        )
        
        suite.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_values_to_match_regex",
                kwargs={
                    "column": "transaction_id",
                    "regex": "^TXN-[0-9]{10}$",
                    "mostly": self.threshold
                }
            )
        )
        
        suite.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_distinct_values_to_be_in_set",
                kwargs={
                    "column": "transaction_status",
                    "value_set": ["COMPLETED", "PENDING", "FAILED", "CANCELLED"]
                }
            )
        )
        
        suite.add_expectation(
            ExpectationConfiguration(
                expectation_type="expect_column_values_to_be_of_type",
                kwargs={
                    "column": "transaction_date",
                    "type_": "TimestampType"
                }
            )
        )
        
        return suite
    
    def validar_dataframe(self, df: DataFrame, batch_kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Ejecuta validación completa del DataFrame contra las expectativas."""
        gx_df = SparkDFDataset(df)
        suite = self.crear_expectation_suite()
        gx_df.expectation_suite = suite
        
        results = gx_df.validate(
            result_format="COMPLETE",
            include_results=True
        )
        
        return {
            "success": results.success,
            "statistics": results.statistics,
            "results": results.results,
            "batch_kwargs": batch_kwargs,
            "validation_timestamp": datetime.utcnow().isoformat()
        }
    
    def separar_registros(self, df: DataFrame) -> Tuple[DataFrame, DataFrame]:
        """Separa registros válidos de los que fallan validación.
        
        Returns:
            Tuple de (DataFrame válidos, DataFrame en cuarentena)
        """
        valid_records = df.filter(
            (F.col("transaction_id").isNotNull()) &
            (F.col("amount").isNotNull()) &
            (F.col("amount") >= 0) &
            (F.col("amount") <= 1000000) &
            (F.col("transaction_status").isin(["COMPLETED", "PENDING", "FAILED", "CANCELLED"]))
        )
        
        quarantine_records = df.subtract(valid_records)
        
        logger.info(f"Registros válidos: {valid_records.count()}")
        logger.info(f"Registros en cuarentena: {quarantine_records.count()}")
        
        return valid_records, quarantine_records
    
    def guardar_cuarentena(self, df: DataFrame, partition_date: str) -> None:
        """Guarda registros en cuarentena con metadatos de razón de fallo."""
        quarantine_df = df.withColumn("quarantine_reason", F.lit("QUALITY_CHECK_FAILED")) \
            .withColumn("quarantine_timestamp", F.current_timestamp()) \
            .withColumn("partition_date", F.lit(partition_date))
        
        quarantine_df.write \
            .mode("append") \
            .partitionBy("partition_date") \
            .parquet(self.quarantine_path)
        
        logger.info(f"Cuarentena guardada en {self.quarantine_path}")
    
    def validar_consistencia_entre_sistemas(
        self, 
        df_transacciones: DataFrame, 
        df_analitica: DataFrame
    ) -> Dict[str, Any]:
        """Valida consistencia de datos entre el sistema de transacciones y analítica."""
        transactions_with_amounts = df_transacciones.select(
            "transaction_id", "amount", "customer_id"
        ).distinct()
        
        analitica_with_amounts = df_analitica.select(
            "transaction_id", "total_amount", "customer_id"
        ).distinct()
        
        joined = transactions_with_amounts.join(
            analitica_with_amounts,
            ["transaction_id", "customer_id"],
            "outer"
        )
        
        inconsistent = joined.filter(
            (F.col("amount").isNull()) | 
            (F.col("total_amount").isNull()) |
            (F.abs(F.col("amount") - F.col("total_amount")) > 0.01)
        )
        
        inconsistency_count = inconsistent.count()
        total_count = joined.count()
        consistency_rate = 1.0 - (inconsistency_count / total_count) if total_count > 0 else 0.0
        
        return {
            "inconsistency_count": inconsistency_count,
            "total_count": total_count,
            "consistency_rate": consistency_rate,
            "meets_threshold": consistency_rate >= self.threshold
        }
    
    def aplicar_reglas(self, df: DataFrame, partition_date: str) -> Tuple[DataFrame, Dict[str, Any]]:
        """Aplica todas las reglas de calidad y retorna DataFrame limpio con metadatos.
        
        Args:
            df: DataFrame con datos crudos
            partition_date: Fecha de partición en formato yyyy-mm-dd
            
        Returns:
            Tuple de (DataFrame limpio, métricas de validación)
        """
        valid_df, quarantine_df = self.separar_registros(df)
        
        if quarantine_df.count() > 0:
            self.guardar_cuarentena(quarantine_df, partition_date)
        
        batch_kwargs = {
            "datasource_name": "transacciones_source",
            "data_asset_name": f"transacciones_{partition_date}",
            "partition_date": partition_date
        }
        
        validation_results = self.validar_dataframe(valid_df, batch_kwargs)
        
        metrics = {
            "total_records": df.count(),
            "valid_records": valid_df.count(),
            "quarantined_records": quarantine_df.count(),
            "quality_rate": valid_df.count() / df.count() if df.count() > 0 else 0.0,
            "validation_results": validation_results
        }
        
        return valid_df, metrics


def crear_reglas_calidad(spark: SparkSession) -> ReglasCalidad:
    """Factory para crear instancia de ReglasCalidad."""
    return ReglasCalidad(spark=spark, threshold=0.99)