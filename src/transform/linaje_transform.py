import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


class LinajeTransform:
    """Gestiona el linaje de datos y registro en AWS Glue Data Catalog.
    
    Enriquece los datos con metadatos de linaje incluyendo origen,
    timestamp de procesamiento y versión del pipeline. Registra
    esquemas en AWS Glue Data Catalog para trazabilidad.
    """
    
    def __init__(
        self, 
        pipeline_version: str = "1.0.0",
        glue_database: str = "fintechcorp_gobernanza",
        glue_table_prefix: str = "transacciones_"
    ):
        self.pipeline_version = pipeline_version
        self.glue_database = glue_database
        self.glue_table_prefix = glue_table_prefix
        self.glue_client = boto3.client("glue")
        self.s3_client = boto3.client("s3")
    
    def adicionar_metadatos_linaje(
        self, 
        df: DataFrame, 
        origen: str,
        proceso: str = "transform"
    ) -> DataFrame:
        """Enriquece el DataFrame con columnas de linaje.
        
        Args:
            df: DataFrame a enriquecer
            origen: Sistema de origen de los datos
            proceso: Etapa del pipeline (extract, transform, load)
            
        Returns:
            DataFrame enriquecido con metadatos de linaje
        """
        timestamp_procesamiento = datetime.utcnow()
        
        df_linaje = df \
            .withColumn("linaje_origen", F.lit(origen)) \
            .withColumn("linaje_proceso", F.lit(proceso)) \
            .withColumn("linaje_timestamp", F.lit(timestamp_procesamiento)) \
            .withColumn("linaje_pipeline_version", F.lit(self.pipeline_version)) \
            .withColumn(
                "linaje_id_ejecucion", 
                F.concat(
                    F.lit(proceso), 
                    F.lit("_"), 
                    F.lit(timestamp_procesamiento.strftime("%Y%m%d%H%M%S"))
                )
            )
        
        logger.info(f"Metadatos de linaje adicionados: origen={origen}, proceso={proceso}")
        
        return df_linaje
    
    def registrar_tabla_glue(
        self, 
        table_name: str, 
        schema: List[Dict[str, str]], 
        s3_location: str,
        partition_keys: Optional[List[Dict[str, str]]] = None
    ) -> bool:
        """Registra una tabla en AWS Glue Data Catalog.
        
        Args:
            table_name: Nombre de la tabla
            schema: Lista de diccionarios con 'name' y 'type'
            s3_location: Ubicación S3 de los datos
            partition_keys: Claves de partición si aplica
            
        Returns:
            True si el registro fue exitoso
        """
        try:
            table_input = {
                "Name": f"{self.glue_table_prefix}{table_name}",
                "Description": f"Tabla de {table_name} con linaje de datos",
                "StorageDescriptor": {
                    "Location": s3_location,
                    "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveOutputFormat",
                    "SerdeInfo": {
                        "SerializationLibrary": "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
                    },
                    "Columns": [
                        {"Name": col["name"], "Type": col["type"]} 
                        for col in schema
                    ]
                },
                "TableType": "EXTERNAL_TABLE"
            }
            
            if partition_keys:
                table_input["StorageDescriptor"]["PartitionKeys"] = [
                    {"Name": pk["name"], "Type": pk["type"]} 
                    for pk in partition_keys
                ]
            
            self.glue_client.create_table(
                DatabaseName=self.glue_database,
                TableInput=table_input
            )
            
            logger.info(f"Tabla {table_name} registrada en Glue Data Catalog")
            return True
            
        except ClientError as e:
            error_code = e.response.get("Error", {}).get("Code", "")
            if error_code == "AlreadyExistsException":
                self.actualizar_tabla_glue(table_name, schema, s3_location, partition_keys)
                return True
            else:
                logger.error(f"Error al registrar tabla en Glue: {e}")
                raise
    
    def actualizar_tabla_glue(
        self, 
        table_name: str, 
        schema: List[Dict[str, str]], 
        s3_location: str,
        partition_keys: Optional[List[Dict[str, str]]] = None
    ) -> bool:
        """Actualiza una tabla existente en AWS Glue Data Catalog."""
        try:
            table_input = {
                "Name": f"{self.glue_table_prefix}{table_name}",
                "StorageDescriptor": {
                    "Location": s3_location,
                    "Columns": [
                        {"Name": col["name"], "Type": col["type"]} 
                        for col in schema
                    ]
                }
            }
            
            if partition_keys:
                table_input["StorageDescriptor"]["PartitionKeys"] = [
                    {"Name": pk["name"], "Type": pk["type"]} 
                    for pk in partition_keys
                ]
            
            self.glue_client.update_table(
                DatabaseName=self.glue_database,
                TableInput=table_input
            )
            
            logger.info(f"Tabla {table_name} actualizada en Glue Data Catalog")
            return True
            
        except ClientError as e:
            logger.error(f"Error al actualizar tabla en Glue: {e}")
            raise
    
    def obtener_esquema_existente(self, table_name: str) -> Optional[Dict[str, Any]]:
        """Obtiene el esquema actual de una tabla en Glue Data Catalog."""
        try:
            response = self.glue_client.get_table(
                DatabaseName=self.glue_database,
                Name=f"{self.glue_table_prefix}{table_name}"
            )
            return response.get("Table")
        except ClientError as e:
            if e.response.get("Error", {}).get("Code") == "EntityNotFoundException":
                return None
            raise
    
    def registrar_lineage_glue(
        self,
        source_table: str,
        target_table: str,
        transform_type: str
    ) -> bool:
        """Registra linaje entre tablas en AWS Glue Data Catalog.
        
        Args:
            source_table: Tabla de origen
            target_table: Tabla de destino
            transform_type: Tipo de transformación aplicada
            
        Returns:
            True si el registro fue exitoso
        """
        try:
            self.glue_client.create_crawler(
                Name=f"lineage_{source_table}_to_{target_table}",
                Role="arn:aws:iam::123456789012:role/GlueServiceRole",
                DatabaseName=self.glue_database,
                Targets={
                    "CatalogTargets": [
                        {
                            "DatabaseName": self.glue_database,
                            "TableName": f"{self.glue_table_prefix}{target_table}"
                        }
                    ]
                },
                SchemaChangePolicy={
                    "UpdateBehavior": "UPDATE_IN_DATABASE",
                    "DeleteBehavior": "DEPRECATE_IN_DATABASE"
                }
            )
            
            logger.info(f"Linaje registrado: {source_table} -> {target_table} ({transform_type})")
            return True
            
        except ClientError as e:
            error_code = e.response.get("Error", {}).get("Code", "")
            if error_code == "AlreadyExistsException":
                logger.info(f"Linaje ya existe: {source_table} -> {target_table}")
                return True
            else:
                logger.error(f"Error al registrar linaje en Glue: {e}")
                return False
    
    def generar_reporte_linaje(self, df: DataFrame) -> Dict[str, Any]:
        """Genera reporte de metadatos de linaje del DataFrame."""
        columnas_linaje = ["linaje_origen", "linaje_proceso", "linaje_timestamp", 
                          "linaje_pipeline_version", "linaje_id_ejecucion"]
        
        columnas_existentes = [c for c in columnas_linaje if c in df.columns]
        
        if not columnas_existentes:
            return {"error": "DataFrame no tiene metadatos de linaje"}
        
        df_select = df.select(columnas_existentes).distinct()
        
        registros = df_select.collect()
        
        return {
            "origenes": list(set(r["linaje_origen"] for r in registros)),
            "procesos": list(set(r["linaje_proceso"] for r in registros)),
            "versiones_pipeline": list(set(r["linaje_pipeline_version"] for r in registros)),
            "total_ejecuciones": len(registros)
        }


def crear_linaje_transform(pipeline_version: str = "1.0.0") -> LinajeTransform:
    """Factory para crear instancia de LinajeTransform."""
    return LinajeTransform(pipeline_version=pipeline_version)