import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

import boto3
from botocore.exceptions import ClientError
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, current_timestamp, lit

logger = logging.getLogger(__name__)


class RedshiftLoader:
    """Cargador de datos en Amazon Redshift con soporte para idempotencia.
    
    Utiliza estrategia de upsert basada en clave primaria para garantizar
    que cada registro se inserta una sola vez y las actualizaciones se
    reflejan correctamente. Emplea COPY desde S3 para optimizar la carga
    masiva de datos en formato Parquet.
    """
    
    def __init__(
        self,
        redshift_config: Dict[str, Any],
        s3_config: Dict[str, Any],
        glue_config: Optional[Dict[str, Any]] = None
    ):
        self.redshift_config = redshift_config
        self.s3_config = s3_config
        self.glue_config = glue_config or {}
        self._client = None
        self._spark = None
        self.execution_id = str(uuid.uuid4())
        logger.info(f"Inicializando RedshiftLoader con execution_id: {self.execution_id}")
    
    @property
    def client(self):
        if self._client is None:
            self._client = boto3.client(
                'redshift-data',
                region_name=self.redshift_config.get('region', 'us-east-1'),
                aws_access_key_id=self.redshift_config.get('access_key_id'),
                aws_secret_access_key=self.redshift_config.get('secret_access_key')
            )
        return self._client
    
    @property
    def spark(self) -> SparkSession:
        if self._spark is None:
            self._spark = SparkSession.builder \
                .appName(f"redshift-loader-{self.execution_id}") \
                .config("spark.sql.adaptive.enabled", "true") \
                .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
                .getOrCreate()
        return self._spark
    
    def load(
        self,
        df: DataFrame,
        table_name: str,
        primary_keys: List[str],
        staging_table: str,
        schema: str = "public"
    ) -> Dict[str, Any]:
        """Carga datos en Redshift usando estrategia de upsert.
        
        Args:
            df: DataFrame de PySpark con los datos a cargar.
            table_name: Nombre de la tabla destino.
            primary_keys: Lista de columnas que forman la clave primaria.
            staging_table: Nombre de la tabla temporal para staging.
            schema: Esquema de Redshift (default: public).
        
        Returns:
            Diccionario con métricas de la operación.
        """
        start_time = datetime.now()
        logger.info(f"Iniciando carga en {schema}.{table_name} con {df.count()} registros")
        
        try:
            full_table_name = f"{schema}.{table_name}"
            full_staging_name = f"{schema}.{staging_table}"
            
            s3_staging_path = self._upload_to_staging(df, table_name)
            
            self._copy_to_staging(s3_staging_path, full_staging_name)
            
            self._execute_upsert(full_staging_name, full_table_name, primary_keys)
            
            self._cleanup_staging(full_staging_name)
            
            duration = (datetime.now() - start_time).total_seconds()
            result = {
                "status": "success",
                "table": full_table_name,
                "records_processed": df.count(),
                "execution_id": self.execution_id,
                "duration_seconds": duration,
                "s3_staging_path": s3_staging_path
            }
            logger.info(f"Carga completada exitosamente: {result}")
            return result
            
        except Exception as e:
            logger.error(f"Error durante la carga en Redshift: {str(e)}")
            raise
    
    def _upload_to_staging(self, df: DataFrame, table_name: str) -> str:
        """Sube el DataFrame a S3 como staging para COPY.
        
        Args:
            df: DataFrame a subir.
            table_name: Nombre de la tabla para construir la ruta.
        
        Returns:
            Ruta S3 donde se almacenaron los datos.
        """
        bucket = self.s3_config['bucket']
        prefix = self.s3_config.get('staging_prefix', 'staging')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        s3_path = f"s3://{bucket}/{prefix}/{table_name}/{timestamp}/"
        
        logger.info(f"Subiendo datos a {s3_path}")
        
        df.write \
            .mode("overwrite") \
            .partitionBy("year", "month", "day") \
            .parquet(s3_path)
        
        return s3_path
    
    def _copy_to_staging(self, s3_path: str, staging_table: str) -> None:
        """Ejecuta COPY desde S3 a la tabla de staging en Redshift.
        
        Args:
            s3_path: Ruta S3 con los datos en Parquet.
            staging_table: Nombre de la tabla de staging.
        """
        database = self.redshift_config.get('database', 'dev')
        
        copy_sql = f"""
        COPY {staging_table}
        FROM '{s3_path}'
        IAM_ROLE '{self.redshift_config.get('iam_role')}'
        FORMAT AS PARQUET
        """
        
        logger.info(f"Ejecutando COPY: {copy_sql}")
        
        response = self.client.execute_statement(
            Database=database,
            Sql=copy_sql,
            ClusterIdentifier=self.redshift_config.get('cluster_identifier'),
            DbUser=self.redshift_config.get('db_user')
        )
        
        self._wait_for_completion(response['Id'])
        logger.info(f"COPY completado exitosamente para {staging_table}")
    
    def _execute_upsert(
        self,
        staging_table: str,
        target_table: str,
        primary_keys: List[str]
    ) -> None:
        """Ejecuta el upsert desde staging a la tabla objetivo.
        
        Args:
            staging_table: Tabla temporal con datos nuevos.
            target_table: Tabla destino.
            primary_keys: Columnas que forman la clave primaria.
        """
        database = self.redshift_config.get('database', 'dev')
        
        join_conditions = " AND ".join([
            f"s.{pk} = t.{pk}" for pk in primary_keys
        ])
        
        update_set = ", ".join([
            f"t.{col} = s.{col}" 
            for col in self._get_table_columns(target_table)
            if col not in primary_keys
        ])
        
        insert_columns = ", ".join(self._get_table_columns(target_table))
        insert_values = ", ".join([f"s.{col}" for col in self._get_table_columns(target_table)])
        
        upsert_sql = f"""
        BEGIN;
        
        UPDATE {target_table} t
        SET {update_set}
        FROM {staging_table} s
        WHERE {join_conditions};
        
        INSERT INTO {target_table} ({insert_columns})
        SELECT {insert_values}
        FROM {staging_table} s
        WHERE NOT EXISTS (
            SELECT 1 FROM {target_table} t
            WHERE {join_conditions}
        );
        
        COMMIT;
        """
        
        logger.info(f"Ejecutando upsert: {upsert_sql[:200]}...")
        
        response = self.client.execute_statement(
            Database=database,
            Sql=upsert_sql,
            ClusterIdentifier=self.redshift_config.get('cluster_identifier'),
            DbUser=self.redshift_config.get('db_user')
        )
        
        self._wait_for_completion(response['Id'])
        logger.info("Upsert completado exitosamente")
    
    def _get_table_columns(self, table_name: str) -> List[str]:
        """Obtiene la lista de columnas de una tabla.
        
        Args:
            table_name: Nombre de la tabla.
        
        Returns:
            Lista de nombres de columnas.
        """
        database = self.redshift_config.get('database', 'dev')
        
        describe_sql = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name.split('.')[-1]}' ORDER BY ordinal_position"
        
        response = self.client.execute_statement(
            Database=database,
            Sql=describe_sql,
            ClusterIdentifier=self.redshift_config.get('cluster_identifier'),
            DbUser=self.redshift_config.get('db_user')
        )
        
        self._wait_for_completion(response['Id'])
        
        result = self.client.get_statement_result(Id=response['Id'])
        return [row[0]['stringValue'] for row in result['Records']]
    
    def _cleanup_staging(self, staging_table: str) -> None:
        """Limpia la tabla de staging.
        
        Args:
            staging_table: Tabla temporal a limpiar.
        """
        database = self.redshift_config.get('database', 'dev')
        
        cleanup_sql = f"TRUNCATE {staging_table}"
        
        logger.info(f"Limpiando tabla de staging: {staging_table}")
        
        try:
            response = self.client.execute_statement(
                Database=database,
                Sql=cleanup_sql,
                ClusterIdentifier=self.redshift_config.get('cluster_identifier'),
                DbUser=self.redshift_config.get('db_user')
            )
            self._wait_for_completion(response['Id'])
        except ClientError as e:
            if "Table does not exist" not in str(e):
                raise
            logger.warning(f"Tabla {staging_table} no existe, omitiendo limpieza")
    
    def _wait_for_completion(self, statement_id: str, timeout: int = 600) -> None:
        """Espera a que una sentencia SQL se complete.
        
        Args:
            statement_id: ID de la sentencia a esperar.
            timeout: Timeout en segundos.
        """
        import time
        elapsed = 0
        interval = 5
        
        while elapsed < timeout:
            response = self.client.describe_statement(Id=statement_id)
            status = response['Status']
            
            if status in ['FINISHED']:
                if response.get('ErrorResult'):
                    raise RuntimeError(f"Sentencia falló: {response['ErrorResult']}")
                return
            elif status in ['FAILED', 'ABORTED']:
                raise RuntimeError(f"Sentencia {status}: {response.get('ErrorMessage', 'Unknown error')}")
            
            time.sleep(interval)
            elapsed += interval
        
        raise TimeoutError(f"Timeout esperando sentencia {statement_id}")
    
    def register_lineage(self, table_name: str, source_systems: List[str]) -> None:
        """Registra el linaje de datos en AWS Glue Data Catalog.
        
        Args:
            table_name: Tabla cuyo linaje se registra.
            source_sistemas: Lista de sistemas de origen.
        """
        if not self.glue_config.get('enable_lineage', False):
            logger.info("Registro de linaje deshabilitado")
            return
        
        glue_client = boto3.client(
            'glue',
            region_name=self.glue_config.get('region', 'us-east-1')
        )
        
        database_name = self.glue_config.get('database', 'gobierno_datos')
        
        try:
            glue_client.update_table(
                DatabaseName=database_name,
                TableInput={
                    'Name': table_name,
                    'Description': f'Tabla cargada desde: {', '.join(source_systems)}',
                    'Parameters': {
                        'lineage_source': ','.join(source_systems),
                        'last_execution_id': self.execution_id,
                        'last_updated': datetime.now().isoformat()
                    }
                }
            )
            logger.info(f"Linaje registrado para {table_name}")
        except ClientError as e:
            logger.warning(f"Error registrando linaje: {str(e)}")