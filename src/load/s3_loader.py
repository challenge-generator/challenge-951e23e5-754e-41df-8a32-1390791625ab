import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

import boto3
from botocore.exceptions import ClientError
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col, current_timestamp, lit, to_date

logger = logging.getLogger(__name__)


class S3Loader:
    """Cargador de datos en Amazon S3 con particionado y formato Parquet.
    
    Gestiona el almacenamiento de datos crudos y procesados en S3,
    organizando la información por fecha y origen para optimizar consultas
    y trazabilidad. Utiliza AWS Lake Formation para control de permisos.
    """
    
    def __init__(
        self,
        s3_config: Dict[str, Any],
        lake_formation_config: Optional[Dict[str, Any]] = None
    ):
        self.s3_config = s3_config
        self.lake_formation_config = lake_formation_config or {}
        self._client = None
        self._spark = None
        self.execution_id = str(uuid.uuid4())
        logger.info(f"Inicializando S3Loader con execution_id: {self.execution_id}")
    
    @property
    def client(self):
        if self._client is None:
            self._client = boto3.client(
                's3',
                region_name=self.s3_config.get('region', 'us-east-1'),
                aws_access_key_id=self.s3_config.get('access_key_id'),
                aws_secret_access_key=self.s3_config.get('secret_access_key')
            )
        return self._client
    
    @property
    def spark(self) -> SparkSession:
        if self._spark is None:
            self._spark = SparkSession.builder \
                .appName(f"s3-loader-{self.execution_id}") \
                .config("spark.sql.extensions", "org.apache.spark.sql.hive.HiveExtensions") \
                .config("spark.sql.adaptive.enabled", "true") \
                .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
                .config("spark.sql.parquet.compression.codec", "snappy") \
                .getOrCreate()
        return self._spark
    
    def load_raw(
        self,
        df: DataFrame,
        source_system: str,
        partition_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Carga datos crudos en S3 con particionado por fecha y origen.
        
        Args:
            df: DataFrame de PySpark con los datos crudos.
            source_system: Sistema de origen de los datos.
            partition_date: Fecha de particionado (default: ahora).
        
        Returns:
            Diccionario con métricas de la operación.
        """
        partition_date = partition_date or datetime.now()
        
        bucket = self.s3_config['bucket']
        prefix = self.s3_config.get('raw_prefix', 'raw')
        
        partition_path = self._build_partition_path(
            prefix=prefix,
            source_system=source_system,
            partition_date=partition_date
        )
        
        s3_uri = f"s3://{bucket}/{partition_path}"
        
        logger.info(f"Cargando datos crudos a {s3_uri}")
        
        df_with_metadata = df \
            .withColumn("year", lit(partition_date.year)) \
            .withColumn("month", lit(partition_date.month)) \
            .withColumn("day", lit(partition_date.day)) \
            .withColumn("source_system", lit(source_system)) \
            .withColumn("ingestion_timestamp", current_timestamp())
        
        df_with_metadata.write \
            .mode("append") \
            .partitionBy("year", "month", "day", "source_system") \
            .parquet(s3_uri, compression="snappy")
        
        self._register_table_in_catalog(
            table_name=f"raw_{source_system}",
            s3_uri=s3_uri,
            partition_columns=["year", "month", "day", "source_system"]
        )
        
        result = {
            "status": "success",
            "s3_uri": s3_uri,
            "source_system": source_system,
            "records_written": df.count(),
            "execution_id": self.execution_id,
            "partition_date": partition_date.isoformat()
        }
        
        logger.info(f"Carga cruda completada: {result}")
        return result
    
    def load_processed(
        self,
        df: DataFrame,
        dataset_name: str,
        partition_date: Optional[datetime] = None,
        quality_status: str = "passed"
    ) -> Dict[str, Any]:
        """Carga datos procesados en S3 con metadatos de calidad.
        
        Args:
            df: DataFrame de PySpark con los datos procesados.
            dataset_name: Nombre del dataset procesado.
            partition_date: Fecha de particionado (default: ahora).
            quality_status: Estado de calidad de los datos (passed/failed).
        
        Returns:
            Diccionario con métricas de la operación.
        """
        partition_date = partition_date or datetime.now()
        
        bucket = self.s3_config['bucket']
        prefix = self.s3_config.get('processed_prefix', 'processed')
        
        partition_path = self._build_partition_path(
            prefix=prefix,
            source_system=dataset_name,
            partition_date=partition_date
        )
        
        s3_uri = f"s3://{bucket}/{partition_path}"
        
        logger.info(f"Cargando datos procesados a {s3_uri}")
        
        df_with_metadata = df \
            .withColumn("year", lit(partition_date.year)) \
            .withColumn("month", lit(partition_date.month)) \
            .withColumn("day", lit(partition_date.day)) \
            .withColumn("dataset_name", lit(dataset_name)) \
            .withColumn("quality_status", lit(quality_status)) \
            .withColumn("processing_timestamp", current_timestamp())
        
        df_with_metadata.write \
            .mode("overwrite") \
            .partitionBy("year", "month", "day", "dataset_name", "quality_status") \
            .parquet(s3_uri, compression="snappy")
        
        self._register_table_in_catalog(
            table_name=f"processed_{dataset_name}",
            s3_uri=s3_uri,
            partition_columns=["year", "month", "day", "dataset_name", "quality_status"]
        )
        
        result = {
            "status": "success",
            "s3_uri": s3_uri,
            "dataset_name": dataset_name,
            "records_written": df.count(),
            "execution_id": self.execution_id,
            "quality_status": quality_status,
            "partition_date": partition_date.isoformat()
        }
        
        logger.info(f"Carga procesada completada: {result}")
        return result
    
    def _build_partition_path(
        self,
        prefix: str,
        source_system: str,
        partition_date: datetime
    ) -> str:
        """Construye la ruta de partición según el esquema de directorios.
        
        Args:
            prefix: Prefijo base del path.
            source_system: Sistema de origen o nombre del dataset.
            partition_date: Fecha para el particionado.
        
        Returns:
            Ruta de partición formateada.
        """
        return f"{prefix}/{source_system}/{partition_date.strftime('%Y/%m/%d')}"
    
    def _register_table_in_catalog(
        self,
        table_name: str,
        s3_uri: str,
        partition_columns: List[str]
    ) -> None:
        """Registra la tabla en AWS Glue Data Catalog.
        
        Args:
            table_name: Nombre de la tabla.
            s3_uri: Ruta S3 de los datos.
            partition_columns: Columnas de partición.
        """
        if not self.lake_formation_config.get('enable_catalog', False):
            logger.info("Registro en catálogo deshabilitado")
            return
        
        glue_client = boto3.client(
            'glue',
            region_name=self.lake_formation_config.get('region', 'us-east-1')
        )
        
        database_name = self.lake_formation_config.get('database', 'gobierno_datos')
        
        table_input = {
            'Name': table_name,
            'Description': f'Tabla registrada automáticamente por pipeline de gobierno de datos',
            'StorageDescriptor': {
                'Location': s3_uri,
                'InputFormat': 'org.apache.hadoop.mapred.parquetInputFormat',
                'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.OutputFormat',
                'SerdeInfo': {
                    'SerializationLibrary': 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
                }
            },
            'PartitionKeys': [
                {'Name': col, 'Type': 'string'} for col in partition_columns
            ],
            'TableType': 'EXTERNAL_TABLE',
            'Parameters': {
                'classification': 'parquet',
                'execution_id': self.execution_id,
                'last_updated': datetime.now().isoformat()
            }
        }
        
        try:
            glue_client.create_table(
                DatabaseName=database_name,
                TableInput=table_input
            )
            logger.info(f"Tabla {table_name} registrada en Glue Catalog")
        except ClientError as e:
            if "AlreadyExistsException" in str(e):
                logger.info(f"Tabla {table_name} ya existe, actualizando metadatos")
                glue_client.update_table(
                    DatabaseName=database_name,
                    TableInput=table_input
                )
            else:
                logger.warning(f"Error registrando tabla en catálogo: {str(e)}")
    
    def grant_permissions(
        self,
        table_name: str,
        principal_arn: str,
        permissions: List[str]
    ) -> None:
        """Otorga permisos en Lake Formation.
        
        Args:
            table_name: Nombre de la tabla.
            principal_arn: ARN del principal a quien se otorgan permisos.
            permissions: Lista de permisos (SELECT, ALTER, etc.).
        """
        if not self.lake_formation_config.get('enable_permissions', False):
            logger.info("Gestión de permisos deshabilitada")
            return
        
        lf_client = boto3.client(
            'lakeformation',
            region_name=self.lake_formation_config.get('region', 'us-east-1')
        )
        
        database_name = self.lake_formation_config.get('database', 'gobierno_datos')
        
        try:
            lf_client.grant_permissions(
                Principal={'DataLakePrincipalIdentifier': principal_arn},
                Resource={
                    'Table': {
                        'DatabaseName': database_name,
                        'Name': table_name
                    }
                },
                Permissions=permissions
            )
            logger.info(f"Permisos otorgados a {principal_arn} sobre {table_name}")
        except ClientError as e:
            logger.error(f"Error otorgando permisos: {str(e)}")
            raise
    
    def cleanup_old_partitions(
        self,
        prefix: str,
        retention_days: int = 365
    ) -> Dict[str, Any]:
        """Limpia particiones antiguas según la política de retención.
        
        Args:
            prefix: Prefijo del path a limpiar.
            retention_days: Días de retención.
        
        Returns:
            Diccionario con métricas de la limpieza.
        """
        bucket = self.s3_config['bucket']
        cutoff_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        cutoff_date = cutoff_date.replace(day=cutoff_date.day - retention_days)
        
        logger.info(f"Limpiando particiones anteriores a {cutoff_date.isoformat()}")
        
        paginator = self.client.get_paginator('list_objects_v2')
        objects_to_delete = []
        
        response = paginator.paginate(
            Bucket=bucket,
            Prefix=prefix
        )
        
        for page in response:
            if 'Contents' not in page:
                continue
                
            for obj in page['Contents']:
                key = obj['Key']
                last_modified = obj['LastModified']
                
                if last_modified < cutoff_date:
                    objects_to_delete.append({'Key': key})
        
        if objects_to_delete:
            delete_chunks = [
                objects_to_delete[i:i + 1000] 
                for i in range(0, len(objects_to_delete), 1000)
            ]
            
            for chunk in delete_chunks:
                self.client.delete_objects(
                    Bucket=bucket,
                    Delete={'Objects': chunk}
                )
            
            logger.info(f"Eliminados {len(objects_to_delete)} objetos")
        
        return {
            "status": "success",
            "objects_deleted": len(objects_to_delete),
            "execution_id": self.execution_id
        }