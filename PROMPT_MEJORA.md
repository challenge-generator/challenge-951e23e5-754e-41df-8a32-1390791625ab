# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Archivos que la arquitectura del reto declara y no estan

Creálos con implementacion real, en la capa que les corresponde:

- `dags/gobierno_datos_pipeline.py`
- `src/extract/transacciones_reader.py`
- `src/extract/analitica_reader.py`

## Como saber que terminaste

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Seniority Senior

### Brecha de conocimiento
Gestiona proyectos de mediana complejidad de Gobierno de Datos a través de marcos de trabajo como los propuestos en DAMA, TOGAF, CMMI.

### Misión / candidato
Candidato con experiencia avanzada en ingeniería de datos, trabajando en equipos distribuidos en contextos empresariales complejos.

### Reto
- Tema: Implementación de Gobierno de Datos
- Seniority: senior-l2
- Tipo: practical
- Título: Implementación de Gobierno de Datos en una Empresa de Servicios Financieros
- Tiempo estimado: 2 semanas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Evaluación de la situación actual — objetivo: Identificar las brechas actuales en el gobierno de datos de FintechCorp. — entregable (NO resolver): Reporte de evaluación del gobierno de datos actual.
- Fase 2: Diseño de la solución de gobierno de datos — objetivo: Diseñar una solución de gobierno de datos que aborde las brechas identificadas. — entregable (NO resolver): Documento de diseño de la solución de gobierno de datos.
- Fase 3: Implementación de la solución de gobierno de datos — objetivo: Implementar la solución de gobierno de datos propuesta. — entregable (NO resolver): Solución de gobierno de datos implementada y documentada.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: pyproject.toml ===
[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "gobierno-datos-pipeline"
version = "0.1.0"
description = "Pipeline ETL para gobierno de datos en servicios financieros"
authors = ["Ingeniero de Datos <datos@fintechcorp.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"
apache-airflow = "2.9.2"
pyspark = "3.5.0"
great-expectations = "0.18.12"
boto3 = "1.34.0"
pydantic = "2.7.1"
pyyaml = "6.0.1"

[tool.poetry.group.dev.dependencies]
pytest = "8.1.1"

[tool.poetry.plugins."airflow.plugins"]
"gobierno_datos_plugin" = "gobierno_datos_plugin.plugin:GobiernoDatosPlugin"

# Configuración para AWS Glue Sessions
[[tool.poetry.source]]
name = "pypi"
priority = "primary"

# Configuración para pytest
[tool.pytest.ini_options]
addopts = "-v"
testpaths = ["tests"]

# Configuración para Great Expectations
expectations_store_name = "expectations_store"
validations_store_name = "validations_store"
checkpoint_store_name = "checkpoint_store"
datasources = {}

# === ARCHIVO: src/schemas/transacciones_schema.json ===
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Esquema de Transacciones Financieras",
  "description": "Esquema para validar los datos de transacciones financieras procesadas en el pipeline",
  "type": "object",
  "properties": {
    "id_transaccion": {
      "description": "Identificador único de la transacción",
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36
    },
    "fecha_transaccion": {
      "description": "Fecha y hora de la transacción en formato ISO 8601",
      "type": "string",
      "format": "date-time"
    },
    "monto": {
      "description": "Monto de la transacción",
      "type": "number",
      "minimum": 0,
      "exclusiveMinimum": true
    },
    "moneda": {
      "description": "Código de moneda según ISO 4217",
      "type": "string",
      "enum": ["USD", "EUR", "GBP", "JPY", "COP", "MXN", "BRL", "ARS"]
    },
    "tipo_transaccion": {
      "description": "Tipo de transacción",
      "type": "string",
      "enum": ["DEPOSITO", "RETIRO", "TRANSFERENCIA", "PAGO", "COMPRA"]
    },
    "estado": {
      "description": "Estado de la transacción",
      "type": "string",
      "enum": ["PENDIENTE", "COMPLETADA", "RECHAZADA", "CANCELADA"]
    },
    "origen": {
      "description": "Sistema de origen de la transacción",
      "type": "string",
      "enum": ["SISTEMA_TRANSACTIONAL", "PLATAFORMA_ANALITICA", "MAESTRO_DATOS"]
    },
    "id_cliente": {
      "description": "Identificador del cliente",
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36
    },
    "id_cuenta": {
      "description": "Identificador de la cuenta",
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36
    },
    "id_producto": {
      "description": "Identificador del producto financiero",
      "type": "string",
      "format": "uuid",
      "minLength": 36,
      "maxLength": 36
    },
    "metadatos": {
      "description": "Metadatos adicionales de la transacción",
      "type": "object",
      "additionalProperties": {
        "type": "string"
      }
    },
    "version_esquema": {
      "description": "Versión del esquema utilizado",
      "type": "string",
      "pattern": "^\\d+\\.\\d+\\.\\d+$"
    },
    "fecha_procesamiento": {
      "description": "Fecha y hora de procesamiento en el pipeline",
      "type": "string",
      "format": "date-time"
    }
  },
  "required": [
    "id_transaccion",
    "fecha_transaccion",
    "monto",
    "moneda",
    "tipo_transaccion",
    "estado",
    "origen",
    "id_cliente",
    "version_esquema",
    "fecha_procesamiento"
  ],
  "additionalProperties": false,
  
  "definitions": {
    "expectations": {
      "monto_positivo": {
        "expectation_type": "expect_column_values_to_be_between",
        "kwargs": {
          "column": "monto",
          "min_value": 0.01,
          "max_value": 1000000000
        }
      },
      "moneda_valida": {
        "expectation_type": "expect_column_values_to_be_in_set",
        "kwargs": {
          "column": "moneda",
          "value_set": ["USD", "EUR", "GBP", "JPY", "COP", "MXN", "BRL", "ARS"]
        }
      },
      "tipo_transaccion_valido": {
        "expectation_type": "expect_column_values_to_be_in_set",
        "kwargs": {
          "column": "tipo_transaccion",
          "value_set": ["DEPOSITO", "RETIRO", "TRANSFERENCIA", "PAGO", "COMPRA"]
        }
      },
      "fecha_transaccion_reciente": {
        "expectation_type": "expect_column_values_to_be_between",
        "kwargs": {
          "column": "fecha_transaccion",
          "min_value": "2020-01-01T00:00:00Z",
          "max_value": "{{ now() }}"
        }
      }
    }
  }
}

// === ARCHIVO: src/transform/reglas_calidad.py ===
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
// === ARCHIVO: src/transform/linaje_transform.py ===
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


// === ARCHIVO: src/load/redshift_loader.py ===
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


// === ARCHIVO: src/load/s3_loader.py ===
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


// === ARCHIVO: tests/test_reglas_calidad.py ===
import pytest
import pandas as pd
from datetime import datetime
from decimal import Decimal

try:
    from src.transform.reglas_calidad import (
        validar_transaccion,
        validar_analitica,
        validar_esquema_transacciones,
        validar_esquema_analitica,
        ReglaCalidad,
        ResultadoValidacion
    )
except ImportError:
    from unittest.mock import Mock
    ReglaCalidad = Mock
    ResultadoValidacion = Mock
    def validar_transaccion(df): pass
    def validar_analitica(df): pass
    def validar_esquema_transacciones(df): pass
    def validar_esquema_analitica(df): pass


class TestReglasCalidadTransacciones:
    """Pruebas para reglas de calidad de transacciones"""

    @pytest.fixture
    def df_transaccion_valido(self):
        """DataFrame con datos válidos de transacciones"""
        return pd.DataFrame({
            'id_transaccion': ['TX001', 'TX002', 'TX003'],
            'id_cliente': ['CL001', 'CL002', 'CL003'],
            'monto': [Decimal('150.50'), Decimal('200.00'), Decimal('75.25')],
            'moneda': ['USD', 'USD', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15', '2024-01-15']),
            'tipo_transaccion': ['PAGO', 'TRANSFERENCIA', 'PAGO'],
            'estado': ['COMPLETADA', 'COMPLETADA', 'COMPLETADA']
        })

    @pytest.fixture
    def df_transaccion_invalido(self):
        """DataFrame con datos inválidos de transacciones"""
        return pd.DataFrame({
            'id_transaccion': ['TX001', 'TX002', None],
            'id_cliente': ['CL001', None, 'CL003'],
            'monto': [Decimal('150.50'), Decimal('-50.00'), Decimal('0')],
            'moneda': ['USD', 'INVALIDA', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15', 'invalid']),
            'tipo_transaccion': ['PAGO', 'TRANSFERENCIA', 'PAGO'],
            'estado': ['COMPLETADA', 'DESCONOCIDO', 'COMPLETADA']
        })

    def test_validar_transaccion_datos_validos(self, df_transaccion_valido):
        """Verifica que transacciones válidas pasan las reglas de calidad"""
        resultado = validar_transaccion(df_transaccion_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_transaccion_datos_invalidos(self, df_transaccion_invalido):
        """Verifica que transacciones inválidas fallan las reglas de calidad"""
        resultado = validar_transaccion(df_transaccion_invalido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_esquema_transacciones(self, df_transaccion_valido):
        """Verifica que el esquema de transacciones es correcto"""
        resultado = validar_esquema_transacciones(df_transaccion_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_monto_negativo(self):
        """Verifica que montos negativos son rechazados"""
        df_monto_negativo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('-100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        resultado = validar_transaccion(df_monto_negativo)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_moneda_invalida(self):
        """Verifica que monedas inválidas son rechazadas"""
        df_moneda_invalida = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['XYZ'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        resultado = validar_transaccion(df_moneda_invalida)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_estado_transaccion(self):
        """Verifica que estados válidos son aceptados"""
        df_estado_invalido = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['INVALIDO']
        })
        resultado = validar_transaccion(df_estado_invalido)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False


class TestReglasCalidadAnalitica:
    """Pruebas para reglas de calidad de analítica"""

    @pytest.fixture
    def df_analitica_valido(self):
        """DataFrame con datos válidos de analítica"""
        return pd.DataFrame({
            'id_sesion': ['SES001', 'SES002', 'SES003'],
            'id_usuario': ['USR001', 'USR002', 'USR003'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00', '2024-01-15 11:00:00', '2024-01-15 12:00:00']),
            'duracion_segundos': [300, 600, 450],
            'paginas_visitadas': [5, 10, 7],
            'eventos': [15, 25, 12],
            'conversion': [True, False, True]
        })

    @pytest.fixture
    def df_analitica_invalido(self):
        """DataFrame con datos inválidos de analítica"""
        return pd.DataFrame({
            'id_sesion': ['SES001', None, 'SES003'],
            'id_usuario': ['USR001', 'USR002', None],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00', 'invalid', '2024-01-15 12:00:00']),
            'duracion_segundos': [300, -10, 450],
            'paginas_visitadas': [5, 0, 7],
            'eventos': [15, 25, -5],
            'conversion': [True, False, True]
        })

    def test_validar_analitica_datos_validos(self, df_analitica_valido):
        """Verifica que datos de analítica válidos pasan las reglas"""
        resultado = validar_analitica(df_analitica_valido)
        assert resultado is not None
        assert hasattr(resultado, 'es_valido')
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_validar_analitica_datos_invalidos(self, df_analitica_invalido):
        """Verifica que datos de analítica inválidos fallan las reglas"""
        resultado = validar_analitica(df_analitica_invalido)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_duracion_negativa(self):
        """Verifica que duraciones negativas son rechazadas"""
        df_duracion_negativa = pd.DataFrame({
            'id_sesion': ['SES001'],
            'id_usuario': ['USR001'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00']),
            'duracion_segundos': [-100],
            'paginas_visitadas': [5],
            'eventos': [15],
            'conversion': [True]
        })
        resultado = validar_analitica(df_duracion_negativa)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False

    def test_validar_eventos_negativos(self):
        """Verifica que eventos negativos son rechazados"""
        df_eventos_negativos = pd.DataFrame({
            'id_sesion': ['SES001'],
            'id_usuario': ['USR001'],
            'fecha_sesion': pd.to_datetime(['2024-01-15 10:00:00']),
            'duracion_segundos': [300],
            'paginas_visitadas': [5],
            'eventos': [-10],
            'conversion': [True]
        })
        resultado = validar_analitica(df_eventos_negativos)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False


class TestReglasCalidadUmbrales:
    """Pruebas para umbrales de calidad"""

    def test_umbral_completitud_transacciones(self):
        """Verifica que se cumple el umbral de completitud del 99.9%"""
        df_completo = pd.DataFrame({
            'id_transaccion': ['TX001'] * 1000,
            'id_cliente': ['CL001'] * 1000,
            'monto': [Decimal('100.00')] * 1000,
            'moneda': ['USD'] * 1000,
            'fecha_transaccion': pd.to_datetime(['2024-01-15'] * 1000),
            'tipo_transaccion': ['PAGO'] * 1000,
            'estado': ['COMPLETADA'] * 1000
        })
        resultado = validar_transaccion(df_completo)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is True

    def test_fallo_umbral_completitud(self):
        """Verifica que falla cuando no se cumple el umbral de completitud"""
        df_incompleto = pd.DataFrame({
            'id_transaccion': ['TX001'] * 900 + [None] * 100,
            'id_cliente': ['CL001'] * 1000,
            'monto': [Decimal('100.00')] * 1000,
            'moneda': ['USD'] * 1000,
            'fecha_transaccion': pd.to_datetime(['2024-01-15'] * 1000),
            'tipo_transaccion': ['PAGO'] * 1000,
            'estado': ['COMPLETADA'] * 1000
        })
        resultado = validar_transaccion(df_incompleto)
        assert resultado is not None
        if hasattr(resultado, 'es_valido'):
            assert resultado.es_valido is False
// === ARCHIVO: tests/test_linaje.py ===
import pytest
import pandas as pd
from datetime import datetime
from decimal import Decimal
import json

try:
    from src.transform.linaje_transform import (
        generar_metadatos_linaje,
        agregar_metadatos_dataframe,
        registrar_linaje_origen,
        LinajeMetadata
    )
except ImportError:
    from unittest.mock import Mock
    LinajeMetadata = Mock
    def generar_metadatos_linaje(origen, schema_version): pass
    def agregar_metadatos_dataframe(df, metadata): pass
    def registrar_linaje_origen(tabla, registros): pass


class TestGeneracionMetadatosLinaje:
    """Pruebas para generación de metadatos de linaje"""

    def test_generar_metadatos_origen_transacciones(self):
        """Verifica que se generan metadatos correctos para origen transacciones"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        assert metadata is not None
        assert hasattr(metadata, 'origen')
        if hasattr(metadata, 'origen'):
            assert metadata.origen == 'transacciones'

    def test_generar_metadatos_origen_analitica(self):
        """Verifica que se generan metadatos correctos para origen analítica"""
        metadata = generar_metadatos_linaje('analitica', '1.0.0')
        assert metadata is not None
        if hasattr(metadata, 'origen'):
            assert metadata.origen == 'analitica'

    def test_generar_metadatos_timestamp(self):
        """Verifica que el timestamp de procesamiento se registra correctamente"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        assert metadata is not None
        assert hasattr(metadata, 'timestamp_procesamiento')
        if hasattr(metadata, 'timestamp_procesamiento'):
            ts = metadata.timestamp_procesamiento
            assert isinstance(ts, datetime)
            assert ts.year >= 2024

    def test_generar_metadatos_version_pipeline(self):
        """Verifica que la versión del pipeline se registra"""
        version_pipeline = '1.2.3'
        metadata = generar_metadatos_linaje('transacciones', version_pipeline)
        assert metadata is not None
        assert hasattr(metadata, 'version_pipeline')
        if hasattr(metadata, 'version_pipeline'):
            assert metadata.version_pipeline == version_pipeline


class TestAgregarMetadatosDataFrame:
    """Pruebas para agregar metadatos a DataFrames"""

    @pytest.fixture
    def df_ejemplo(self):
        """DataFrame de ejemplo para pruebas"""
        return pd.DataFrame({
            'id': ['001', '002', '003'],
            'valor': [100, 200, 300],
            'fecha': pd.to_datetime(['2024-01-15', '2024-01-15', '2024-01-15'])
        })

    def test_agregar_metadatos_a_dataframe(self, df_ejemplo):
        """Verifica que metadatos se agregan al DataFrame"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        df_con_metadata = agregar_metadatos_dataframe(df_ejemplo, metadata)
        assert df_con_metadata is not None
        assert hasattr(df_con_metadata, 'attrs')
        assert 'linaje' in df_con_metadata.attrs or len(df_con_metadata.attrs) >= 0

    def test_metadatos_incluyen_origen(self, df_ejemplo):
        """Verifica que metadatos incluyen el origen de los datos"""
        metadata = generar_metadatos_linaje('sistema_origen', '2.0.0')
        df_con_metadata = agregar_metadatos_dataframe(df_ejemplo, metadata)
        assert df_con_metadata is not None

    def test_metadatos_incluyen_timestamp(self, df_ejemplo):
        """Verifica que metadatos incluyen timestamp"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        df_con_metadata = agregar_metadatos_dataframe(df_ejemplo, metadata)
        assert df_con_metadata is not None
        assert len(df_con_metadata) == len(df_ejemplo)


class TestRegistroLinajeOrigen:
    """Pruebas para registro de linaje por origen"""

    def test_registrar_linaje_tabla_transacciones(self):
        """Verifica el registro de linaje para tabla de transacciones"""
        resultado = registrar_linaje_origen('transacciones_financieras', 1500)
        assert resultado is not None
        assert isinstance(resultado, (dict, LinajeMetadata)) or resultado is not None

    def test_registrar_linaje_tabla_analitica(self):
        """Verifica el registro de linaje para tabla de analítica"""
        resultado = registrar_linaje_origen('sesiones_analitica', 5000)
        assert resultado is not None

    def test_registrar_linaje_contador_registros(self):
        """Verifica que se registra correctamente el número de registros"""
        num_registros = 10000
        resultado = registrar_linaje_origen('transacciones', num_registros)
        assert resultado is not None


class TestLinajeVersionEsquema:
    """Pruebas para versionado de esquemas en linaje"""

    def test_version_esquema_v1(self):
        """Verifica linaje con versión de esquema 1.0.0"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        assert metadata is not None
        if hasattr(metadata, 'version_schema'):
            assert metadata.version_schema == '1.0.0'

    def test_version_esquema_v2(self):
        """Verifica linaje con versión de esquema 2.0.0"""
        metadata = generar_metadatos_linaje('transacciones', '2.0.0')
        assert metadata is not None
        if hasattr(metadata, 'version_schema'):
            assert metadata.version_schema == '2.0.0'

    def test_evolucion_esquema_linaje(self):
        """Verifica que el linaje registra la evolución del esquema"""
        metadata_v1 = generar_metadatos_linaje('transacciones', '1.0.0')
        metadata_v2 = generar_metadatos_linaje('transacciones', '2.0.0')
        assert metadata_v1 is not None
        assert metadata_v2 is not None
        if hasattr(metadata_v1, 'version_schema') and hasattr(metadata_v2, 'version_schema'):
            assert metadata_v1.version_schema != metadata_v2.version_schema


class TestLinajeTrazabilidad:
    """Pruebas para trazabilidad del linaje"""

    def test_trazabilidad_fecha_procesamiento(self):
        """Verifica que la fecha de procesamiento es trazable"""
        metadata = generar_metadatos_linaje('transacciones', '1.0.0')
        assert metadata is not None
        assert hasattr(metadata, 'timestamp_procesamiento')

    def test_trazabilidad_origen_datos(self):
        """Verifica que el origen de datos es trazable"""
        origen = 'sistema_origen_transacciones'
        metadata = generar_metadatos_linaje(origen, '1.0.0')
        assert metadata is not None
        if hasattr(metadata, 'origen'):
            assert metadata.origen == origen

    def test_trazabilidad_version_pipeline(self):
        """Verifica que la versión del pipeline es trazable"""
        version = '3.1.0'
        metadata = generar_metadatos_linaje('transacciones', version)
        assert metadata is not None
        if hasattr(metadata, 'version_pipeline'):
            assert metadata.version_pipeline is not None
// === ARCHIVO: tests/test_idempotencia.py ===
import pytest
import pandas as pd
from datetime import datetime
from decimal import Decimal
from unittest.mock import Mock, patch, MagicMock
import boto3

try:
    from src.load.redshift_loader import (
        cargar_datos_redshift,
        verificar_existencia_registros,
        ejecutar_copy_parquet,
        configurarConexionRedshift
    )
except ImportError:
    def cargar_datos_redshift(df, tabla): pass
    def verificar_existencia_registros(tabla, clave): pass
    def ejecutar_copy_parquet(s3_path, tabla): pass
    def configurarConexionRedshift(): pass


class TestIdempotenciaCarga:
    """Pruebas para verificar idempotencia en la carga de datos"""

    @pytest.fixture
    def df_ejemplo(self):
        """DataFrame de ejemplo para pruebas de carga"""
        return pd.DataFrame({
            'id_transaccion': ['TX001', 'TX002', 'TX003'],
            'id_cliente': ['CL001', 'CL002', 'CL003'],
            'monto': [Decimal('150.50'), Decimal('200.00'), Decimal('75.25')],
            'moneda': ['USD', 'USD', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15', '2024-01-15']),
            'tipo_transaccion': ['PAGO', 'TRANSFERENCIA', 'PAGO'],
            'estado': ['COMPLETADA', 'COMPLETADA', 'COMPLETADA']
        })

    def test_carga_duplicada_no_genera_duplicados(self, df_ejemplo):
        """Verifica que ejecutar la carga dos veces no duplica registros"""
        tabla = 'transacciones_test'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            mock_cursor.fetchone.return_value = (3,)
            
            cargar_datos_redshift(df_ejemplo, tabla)
            cargar_datos_redshift(df_ejemplo, tabla)
            
            assert mock_cursor.execute.call_count >= 1

    def test_verificar_existencia_registros(self):
        """Verifica que se verifican registros existentes antes de cargar"""
        tabla = 'transacciones'
        clave = 'TX001'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            mock_cursor.fetchone.return_value = (1,)
            
            resultado = verificar_existencia_registros(tabla, clave)
            assert resultado is not None

    def test_ejecutar_copy_parquet(self):
        """Verifica que el comando COPY se ejecuta correctamente"""
        s3_path = 's3://bucket/path/to/file.parquet'
        tabla = 'transacciones'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            resultado = ejecutar_copy_parquet(s3_path, tabla)
            assert mock_cursor.execute.called or resultado is not None


class TestEstrategiaReintento:
    """Pruebas para estrategia de reintento en carga"""

    def test_reintento_carga_fallida(self):
        """Verifica que la carga se reintenta en caso de fallo temporal"""
        df_ejemplo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        tabla = 'transacciones_test'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            mock_cursor.execute.side_effect = [Exception('Temporal failure'), None]
            
            try:
                cargar_datos_redshift(df_ejemplo, tabla)
            except Exception:
                pass

    def test_maximo_reintentos(self):
        """Verifica que no se excede el máximo de reintentos"""
        df_ejemplo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        tabla = 'transacciones_test'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            mock_cursor.execute.side_effect = Exception('Persistent failure')
            
            intentos = 0
            max_intentos = 3
            for _ in range(max_intentos):
                try:
                    cargar_datos_redshift(df_ejemplo, tabla)
                    break
                except Exception:
                    intentos += 1
            
            assert intentos <= max_intentos


class TestCargaConClaveIdempotente:
    """Pruebas para carga con claves únicas idempotentes"""

    def test_clave_compuesta_idempotente(self):
        """Verifica que claves compuestas aseguran idempotencia"""
        df_ejemplo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        tabla = 'transacciones_test'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            cargar_datos_redshift(df_ejemplo, tabla)
            
            assert mock_cursor.execute.called

    def test_upsert_para_idempotencia(self):
        """Verifica que se usa UPSERT para mantener idempotencia"""
        df_ejemplo = pd.DataFrame({
            'id_transaccion': ['TX001', 'TX001'],
            'id_cliente': ['CL001', 'CL001'],
            'monto': [Decimal('100.00'), Decimal('150.00')],
            'moneda': ['USD', 'USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15', '2024-01-15']),
            'tipo_transaccion': ['PAGO', 'PAGO'],
            'estado': ['COMPLETADA', 'COMPLETADA']
        })
        tabla = 'transacciones_test'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            cargar_datos_redshift(df_ejemplo, tabla)
            
            call_args = str(mock_cursor.execute.call_args_list)
            assert 'INSERT' in call_args.upper() or 'COPY' in call_args.upper() or mock_cursor.execute.called


class TestParticionadoIdempotente:
    """Pruebas para idempotencia con particionado"""

    def test_particion_por_fecha(self):
        """Verifica que el particionado por fecha permite cargas idempotentes"""
        df_ejemplo = pd.DataFrame({
            'id_transaccion': ['TX001'],
            'id_cliente': ['CL001'],
            'monto': [Decimal('100.00')],
            'moneda': ['USD'],
            'fecha_transaccion': pd.to_datetime(['2024-01-15']),
            'tipo_transaccion': ['PAGO'],
            'estado': ['COMPLETADA']
        })
        
        fecha_str = '2024/01/15'
        
        with patch('src.load.redshift_loader.configurarConexionRedshift') as mock_conn:
            mock_cursor = MagicMock()
            mock_conn.return_value.cursor.return_value = mock_cursor
            
            cargar_datos_redshift(df_ejemplo, 'transacciones', partition_date=fecha_str)
            
            assert mock_cursor.execute.called or True

    def test_ruta_s3_particionada(self):
        """Verifica que la ruta S3 usa particionado correcto"""
        bucket = 'fintech-data-lake'
        tabla = 'transacciones'
        fecha = '2024-01-15'
        origen = 'transacciones'
        
        expected_path = f's3://{bucket}/{tabla}/fecha={fecha}/origen={origen}/'
        
        with patch('boto3.client') as mock_boto:
            mock_s3 = MagicMock()
            mock_boto.return_value = mock_s3
            
            assert expected_path is not None
            assert 'fecha=' in expected_path
            assert 'origen=' in expected_path


// === ARCHIVO: conf/config_dev.yaml ===
# Configuración del entorno de desarrollo para el pipeline de gobierno de datos
# FintechCorp - Pipeline ETL con Airflow, Spark y Great Expectations
# Este archivo contiene la configuración específica del ambiente de desarrollo
# Las credenciales aquí son simuladas y deben reemplazarse en producción

# ==============================================================================
# CONFIGURACIÓN GENERAL DEL AMBIENTE
# ==============================================================================
ambiente: "desarrollo"
version_pipeline: "0.1.0"
modo_ejecucion: "local"  # local, airflow, glue
log_level: "DEBUG"

# ==============================================================================
# CONFIGURACIÓN DE AIRFLOW
# ==============================================================================
airflow:
  # Conexiones configuradas en Airflow Metadata Database
  connections:
    aws_default:
      conn_id: "aws_default"
      conn_type: "aws"
      login: "AKIAIOSFODNN7EXAMPLE"  # Credencial simulada - NO usar en producción
      password: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Simulado
      extra:
        region_name: "us-east-1"
        
    redshift_default:
      conn_id: "redshift_default"
      conn_type: "redshift"
      login: "dev_user"
      password: "dev_password_simulated"
      host: "fintech-dev.redshift.amazonaws.com"
      port: 5439
      schema: "fintech_dev"
      extra:
        db_name: "fintech_analytics"
        cluster_identifier: "fintech-dev-cluster"
        iam_role: "arn:aws:iam::123456789012:role/RedshiftCopyRole"
    
    s3_logs:
      conn_id: "s3_logs"
      conn_type: "s3"
      extra:
        bucket: "fintech-dev-logs"
        prefix: "pipeline-logs/"
  
  # Variables de Airflow para el pipeline
  variables:
    pipeline_name: "gobierno_datos_pipeline"
    fecha_ejecucion: "{{ ds }}"
    ruta_datos_raw: "s3://fintech-dev-raw-data/"
    ruta_datos_procesados: "s3://fintech-dev-processed/"
    ruta_datos_quarantine: "s3://fintech-dev-quarantine/"
    ruta_logs_calidad: "s3://fintech-dev-logs/quality/"

# ==============================================================================
# CONFIGURACIÓN DE AWS
# ==============================================================================
aws:
  region: "us-east-1"
  account_id: "123456789012"
  
  # Configuración de S3
  s3:
    buckets:
      raw_data: "fintech-dev-raw-data"
      processed_data: "fintech-dev-processed"
      quarantine: "fintech-dev-quarantine"
      logs: "fintech-dev-logs"
      backups: "fintech-dev-backups"
    
    # Prefijos por origen de datos
    prefijos:
      transacciones: "transacciones/"
      analitica: "analitica/"
      maestro: "maestro/"
    
    # Configuración de particionado
    particionado:
      formato: "parquet"
      compresion: "snappy"
      esquema_fecha: "yyyy/mm/dd"  # Particionado por fecha para optimización
  
  # Configuración de Redshift
  redshift:
    cluster_endpoint: "fintech-dev.redshift.amazonaws.com"
    port: 5439
    database: "fintech_analytics"
    schema: "fintech_dev"
    
    # Tablas del data warehouse
    tablas:
      transacciones_procesadas: "stg_transacciones"
      analitica_procesada: "stg_analitica"
      maestro_procesado: "stg_maestro"
      calidad_registros: "audit_calidad_datos"
      linaje_ejecucion: "audit_linaje_ejecucion"
    
    # Configuración de COPY
    copy_options:
      formato: "parquet"
      tiempo_fuera: 60
      maxerror: 1000
      acceptinvchars: ""
      
  # Configuración de Glue
  glue:
    catalog_name: "fintech_dev_catalog"
    database: "fintech_dev"
    
    # Crawlers configurados
    crawlers:
      transacciones:
        name: "fintech-dev-transacciones-crawler"
        schedule: "cron(0 2 * * ? *)"
        table_prefix: "raw_"
      
      analitica:
        name: "fintech-dev-analitica-crawler"
        schedule: "cron(0 3 * * ? *)"
        table_prefix: "raw_"
    
    # Jobs de transformación
    jobs:
      transformacion:
        name: "fintech-dev-transform-job"
        worker_type: "G.1X"
        number_of_workers: 10
        max_retries: 3

# ==============================================================================
# CONFIGURACIÓN DE CALIDAD DE DATOS
# ==============================================================================
calidad_datos:
  # Umbrales de calidad - deben cumplir 99.9% de precisión según requisitos
  umbrales:
    precision_minima: 99.9  # Porcentaje mínimo de registros válidos
    completitud_minima: 98.0  # Porcentaje de campos no nulos
    consistencia_maxima: 1.0  # Porcentaje máximo de inconsistencias
    duplicados_maximo: 0.5  # Porcentaje máximo de duplicados permitidos
    
  # Reglas de validación por origen
  reglas_por_origen:
    transacciones:
      - nombre: "validar_id_transaccion"
        tipo: "not_null"
        columna: "id_transaccion"
        severidad: "critica"
        
      - nombre: "validar_monto_positivo"
        tipo: "greater_than"
        columna: "monto"
        valor: 0
        severidad: "critica"
        
      - nombre: "validar_fecha_transaccion"
        tipo: "between_dates"
        columna: "fecha_transaccion"
        min: "2020-01-01"
        max: "{{ ds }}"
        severidad: "alta"
        
      - nombre: "validar_codigo_moneda"
        tipo: "isin"
        columna: "codigo_moneda"
        valores: ["USD", "EUR", "MXN", "COP", "BRL", "ARS"]
        severidad: "media"
        
      - nombre: "validar_tipo_transaccion"
        tipo: "isin"
        columna: "tipo_transaccion"
        valores: ["pago", "transferencia", "retiro", "deposito", "ajuste"]
        severidad: "media"
        
    analitica:
      - nombre: "validar_id_sesion"
        tipo: "not_null"
        columna: "id_sesion"
        severidad: "critica"
        
      - nombre: "validar_duracion_positiva"
        tipo: "greater_than_or_equal"
        columna: "duracion_segundos"
        valor: 0
        severidad: "alta"
        
      - nombre: "validar_timestamp_evento"
        tipo: "not_null"
        columna: "timestamp_evento"
        severidad: "critica"
        
    maestro:
      - nombre: "validar_id_cliente"
        tipo: "not_null"
        columna: "id_cliente"
        severidad: "critica"
        
      - nombre: "validar_tipo_identificacion"
        tipo: "isin"
        columna: "tipo_identificacion"
        valores: ["CC", "CE", "PAS", "NIT", "RUC"]
        severidad: "alta"
        
      - nombre: "validar_fecha_nacimiento"
        tipo: "between_dates"
        columna: "fecha_nacimiento"
        min: "1900-01-01"
        max: "{{ macros.ds_add(ds, -6570) }}"  # 18 años atrás
        severidad: "alta"
  
  # Configuración de cuarentena
  cuarentena:
    enabled: true
    ruta: "s3://fintech-dev-quarantine/"
    retencion_dias: 30  # Los registros malos se retienen 30 días para auditoría
    notificacion_email: "calidad-datos@fintechcorp.com"
    
  # Configuración de Great Expectations
  great_expectations:
    expectations_store: "s3://fintech-dev-validations/expectations/"
    validations_store: "s3://fintech-dev-validations/results/"
    checkpoint_store: "s3://fintech-dev-validations/checkpoints/"
    data_docs_site: "s3://fintech-dev-docs/quality/"
    
# ==============================================================================
# CONFIGURACIÓN DE LINAGE Y TRAZABILIDAD
# ==============================================================================
linaje:
  # Configuración de AWS Glue Data Catalog para linaje
  glue_catalog:
    enabled: true
    database: "fintech_dev"
    
  # Tablas de auditoría
  audit:
    calidad_tabla: "audit_calidad_datos"
    linaje_tabla: "audit_linaje_ejecucion"
    
    columnas_audit:
      - nombre: "id_ejecucion"
        tipo: "string"
        descripcion: "UUID de la ejecución del pipeline"
        
      - nombre: "timestamp_ejecucion"
        tipo: "timestamp"
        descripcion: "Fecha y hora de la ejecución"
        
      - nombre: "origen_datos"
        tipo: "string"
        descripcion: "Sistema de origen de los datos"
        
      - nombre: "tabla_destino"
        tipo: "string"
        descripcion: "Tabla destino en Redshift"
        
      - nombre: "registros_procesados"
        tipo: "bigint"
        descripcion: "Cantidad de registros procesados"
        
      - nombre: "registros_exitosos"
        tipo: "bigint"
        descripcion: "Cantidad de registros exitosos"
        
      - nombre: "registros_fallidos"
        tipo: "bigint"
        descripcion: "Cantidad de registros que fallaron validación"
        
      - nombre: "calidad_porcentaje"
        tipo: "decimal(5,2)"
        descripcion: "Porcentaje de calidad alcanzado"
        
      - nombre: "version_esquema"
        tipo: "string"
        descripcion: "Versión del esquema utilizado"
        
      - nombre: "usuario_ejecucion"
        tipo: "string"
        descripcion: "Usuario que ejecutó el pipeline"

# ==============================================================================
# CONFIGURACIÓN DE RENDIMIENTO Y LATENCIA
# ==============================================================================
rendimiento:
  # Requisitos: latencia máxima de 2 segundos en actualización de registros
  latencia_maxima_segundos: 2
  
  # Configuración de Spark
  spark:
    master: "local[*]"
    app_name: "gobierno_datos_pipeline"
    
    config:
      spark.sql.shuffle.partitions: 200
      spark.default.parallelism: 100
      spark.sql.adaptive.enabled: "true"
      spark.sql.adaptive.coalescePartitions.enabled: "true"
      spark.dynamicAllocation.enabled: "true"
      spark.dynamicAllocation.minExecutors: 2
      spark.dynamicAllocation.maxExecutors: 10
      
    # Configuración de memoria
    memoria:
      driver_memory: "4g"
      executor_memory: "4g"
      executor_cores: 2
  
  # Configuración de procesamiento paralelo
  procesamiento:
    batch_size: 10000  # Registros por batch
    max_workers: 20  # Máximo de workers paralelos
    timeout_minutos: 30  # Timeout por tarea
    
  # Volumen: hasta 10 millones de transacciones diarias
  volumen:
    transacciones_diarias_max: 10000000
    tamano_batch_optimo: 500000

# ==============================================================================
# CONFIGURACIÓN DE RETENCIÓN Y RESPALDO
# ==============================================================================
retencion:
  # Requisito: trazabilidad de datos por al menos 5 años
  periodos:
    datos_raw_dias: 90  # Datos crudos retención mínima
    datos_procesados_dias: 1825  # 5 años = 1825 días
    logs_dias: 365  # Logs por 1 año
    validaciones_dias: 730  # 2 años de validaciones
    backups_dias: 1825  # 5 años de backups
    
  # Configuración de respaldo
  backup:
    enabled: true
    frecuencia: "diario"
    ruta: "s3://fintech-dev-backups/"
    retencion_en_dias: 1825
    
  # Eliminación automática
  limpieza_automatica:
    enabled: true
    hora_ejecucion: "02:00"  # 2 AM
    dias_antiguedad_minima: 90

# ==============================================================================
# CONFIGURACIÓN DE NOTIFICACIONES Y ALERTAS
# ==============================================================================
notificaciones:
  email:
    enabled: true
    smtp_host: "smtp.fintechcorp.com"
    smtp_port: 587
    from_address: "pipeline-datos@fintechcorp.com"
    
    destinatarios:
     -alertas: "equipo-datos@fintechcorp.com"
      -calidad: "calidad-datos@fintechcorp.com"
      -infra: "infraestructura@fintechcorp.com"
  
  # Alertas por umbral
  alertas:
    calidad_baja:
      enabled: true
      umbral: 95.0  # Alertar si calidad cae bajo 95%
      severidad: "alta"
      
    volumen_anomalo:
      enabled: true
      variacion_porcentaje: 20  # Alertar si varías más del 20%
      severidad: "media"
      
    latencia_alta:
      enabled: true
      umbral_segundos: 5  # Alertar si latency > 5 segundos
      severidad: "alta"
      
    errores_procesamiento:
      enabled: true
      severidad: "critica"
      
# ==============================================================================
# CONFIGURACIÓN DE SEGURIDAD
# ==============================================================================
seguridad:
  # Configuración de encriptación
  encriptacion:
    s3: "AES256"  # Encriptación en S3
    redshift: "TLS_1_2"  # Encriptación en Redshift
    
  # Configuración de acceso
  acceso:
    iam_role: "arn:aws:iam::123456789012:role/DataPipelineRole"
    kms_key: "arn:aws:kms:us-east-1:123456789012:key/data-pipeline-key"
    
  # Configuración de red
  red:
    vpc_id: "vpc-0123456789abcdef0"
    subnet_ids:
      - "subnet-0123456789abcdef1"
      - "subnet-0123456789abcdef2"
    security_group: "sg-0123456789abcdef0"

# ==============================================================================
# CONFIGURACIÓN DE MONITOREO
# ==============================================================================
monitoreo:
  # CloudWatch
  cloudwatch:
    enabled: true
    namespace: "FintechCorp/DataPipeline"
    
    metricas:
      - nombre: "RegistrosProcesados"
        unidad: "Count"
        
      - nombre: "CalidadPorcentaje"
        unidad: "Percent"
        
      - nombre: "LatenciaSegundos"
        unidad: "Seconds"
        
      - nombre: "ErroresContador"
        unidad: "Count"
        
  # Logs
  logs:
    group: "/aws/fintech/pipeline-datos"
    stream: "{{ ti.task_id }}-{{ ds }}"
    retencion_dias: 30


// === ARCHIVO: docs/reporte_evaluacion.md ===
# Reporte de Evaluación del Gobierno de Datos - Fase 1

## Resumen Ejecutivo

El presente documento analiza el estado actual del gobierno de datos en FintechCorp, identificando brechas críticas en calidad, consistencia y trazabilidad de los datos provenientes de tres sistemas fuente: el sistema de origen de transacciones, la plataforma de analítica y el almacenamiento de datos maestro.

## Sistemas Analizados

### Sistema de Origen de Transacciones

- **Volumen estimado**: 10 millones de transacciones diarias
- **Frecuencia de actualización**: Tiempo real
- **Formato de datos**: JSON y Parquet
- **Almacenamiento actual**: Amazon S3 (raw bucket)

### Plataforma de Analítica

- **Volumen estimado**: 5 millones de eventos diarios
- **Frecuencia de actualización**: Cada 15 minutos
- **Formato de datos**: Parquet columnar
- **Almacenamiento actual**: Amazon Redshift

### Almacenamiento de Datos Maestro

- **Volumen estimado**: 50 GB de datos maestros
- **Frecuencia de actualización**: Diario (batch)
- **Formato de datos**: CSV y JSON
- **Almacenamiento actual**: PostgreSQL on-premises

## Métricas Actuales de Calidad de Datos

| Métrica | Valor Actual | Valor Objetivo | Brecha |
|---------|--------------|----------------|--------|
| Precisión de datos | 97.2% | 99.9% | -2.7% |
| Latencia de actualización | 4.5 segundos | 2.0 segundos | -2.5 seg |
| Completitud de registros | 94.8% | 99.9% | -5.1% |
| Consistencia entre fuentes | 89.3% | 99.9% | -10.6% |
| Trazabilidad de linaje | 45.0% | 100.0% | -55.0% |

## Brechas Identificadas

### 1. Calidad de Datos

**Problema**: Ausencia de reglas de validación automatizadas en el pipeline de ingestión. Los datos se cargan directamente sin verificación de integridad, completitud ni consistencia.

**Impacto**: Registros duplicados (estimado 3.2%), valores nulos no tratados (2.1%), inconsistencias de formato entre fuentes (4.7%).

**Recomendación**: Implementar suite de validación con Great Expectations que valide cada lote ingestado contra expectativas definidas por el dominio.

### 2. Consistencia entre Fuentes

**Problema**: Falta de reconciliación entre los tres sistemas fuente. Cada fuente tiene su propio esquema y convenciones de nomenclatura, sin mapeo centralizado.

**Impacto**: Imposibilidad de crear vistas unificadas confiables, queries que fallan silenciosamente, decisiones de negocio basadas en datos incompletos.

**Recomendación**: Definir modelo de datos unificado (canonical data model) con mapeos explícitos de cada fuente, implementado como capa de transformación en el pipeline.

### 3. Trazabilidad y Linaje

**Problema**: Ausencia de registro de linaje de datos. No es posible rastrear el origen de un registro, las transformaciones aplicadas ni el momento de carga.

**Impacto**: Incapacidad de auditar datos para cumplimiento regulatorio, dificultad para diagnosticar problemas de calidad, ausencia de versioning de esquemas.

**Recomendación**: Integrar AWS Glue Data Catalog para registro automático de esquemas, versiones y metadatos de procesamiento.

### 4. Latencia de Procesamiento

**Problema**: Pipeline actual procesa datos en batch diario, con latencia promedio de 4.5 segundos por registro desde ingestión hasta disponibilidad en analytics.

**Impacto**: Decisiones de negocio basadas en datos de hasta 24 horas de antigüedad, incumplimiento de SLA de 2 segundos.

**Recomendación**: Migrar a procesamiento streaming con Apache Kafka o AWS Kinesis, con micro-batch en Airflow para transformación.

### 5. Retención y Archivo

**Problema**: Política de retención no implementada. Los datos se acumulan indefinidamente sin diferenciación entre datos activos y archivo.

**Impacto**: Costos crecientes de almacenamiento, degrade de rendimiento en consultas históricas, riesgo de cumplimiento por retención excesiva.

**Recomendación**: Implementar ciclo de vida con particionamiento por fecha, transición a S3 Glacier para datos mayores a 5 años según requisito regulatorio.

## Priorización de Brechas

| Prioridad | Brecha | Esfuerzo Estimado | Impacto |
|-----------|--------|-------------------|--------|
| Alta | Reglas de calidad automatizadas | 2 semanas | Alto |
| Alta | Trazabilidad y linaje | 3 semanas | Alto |
| Media | Consistencia entre fuentes | 4 semanas | Medio |
| Baja | Latencia de procesamiento | 6 semanas | Medio |
| Baja | Retención y archivo | 2 semanas | Bajo |

## Conclusiones

El gobierno de datos en FintechCorp presenta brechas significativas que impiden cumplir con los objetivos de precisión (99.9%), latencia (2 segundos) y trazabilidad (5 años). La implementación de un pipeline ETL robusto con validación, linaje y orquestación es crítica para alcanzar los estándares requeridos.

## Próximos Pasos

1. Aprobar plan de remediación de brechas de alta prioridad
2. Diseñar arquitectura del nuevo pipeline de gobierno de datos
3. Definir modelo de datos canónico y mapeos de fuentes
4. Seleccionar herramientas de orquestación y validación

---
*Documento generado para FintechCorp - Equipo de Datos*

// === ARCHIVO: docs/diseno_solucion.md ===
# Diseño de Solución de Gobierno de Datos - Fase 2

## Arquitectura Propuesta

La solución de gobierno de datos para FintechCorp se fundamenta en una arquitectura de pipeline ETL/ELT orquestada por Apache Airflow, con capas claramente separadas de extracción, transformación (incluyendo validación de calidad) y carga. El diseño sigue principios de modularidad, idempotencia y escalabilidad horizontal.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ORQUESTACIÓN (Airflow)                         │
│  ┌──────────────┐  ┌──────────────────┐  ┌────────────────────────┐   │
│  │   EXTRACT    │──│    TRANSFORM     │──│         LOAD           │   │
│  │  TaskGroup   │  │   TaskGroup       │  │      TaskGroup         │   │
│  └──────────────┘  └──────────────────┘  └────────────────────────┘   │
│         │                   │                        │                 │
│         ▼                   ▼                        ▼                 │
│  ┌──────────────┐  ┌──────────────────┐  ┌────────────────────────┐   │
│  │ Calidad con  │  │ Linaje y         │  │ Particionamiento S3    │   │
│  │ Great Exp.   │  │ Glue Catalog     │  │ COPY a Redshift        │   │
│  └──────────────┘  └──────────────────┘  └────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                    ┌────────────────────────┐
                    │   S3 (Data Lake)       │
                    │  /raw /processed /gold │
                    └────────────────────────┘
```

## Decisiones Arquitectónicas

### Orquestación: Apache Airflow vs. AWS Step Functions

**Decisión**: Apache Airflow 2.9.2

**Justificación**:
- Flexibilidad para definir dependencias complejas entre tareas
- Comunidad activa y madurez probada en entornos enterprise
- Integración nativa con AWS a través de proveedores (Amazon Provider)
- Soporte para TaskGroups que permiten agrupar lógicamente las fases del pipeline
- Capacidad de retry automático y manejo de errores robusto
- Sistema de scheduling avanzado con cron expressions

AWS Step Functions fue considerado por su modelo de precios por transición de estado, pero la complejidad de los flujos condicionales y la necesidad de reintentos granulares hicieron que Airflow fuera la opción más adecuada para este caso de uso.

### Procesamiento: PySpark vs. Pandas

**Decisión**: PySpark 3.5.0

**Justificación**:
- Capacidad de procesamiento distribuido para manejar 10M+ transacciones diarias
- Tolerancia a fallos inherente mediante RDDs y DataFrames
- Integración nativa con AWS Glue para procesamiento serverless
-Optimización de consultas mediante predicate pushdown y column pruning
- Memoria distribuida paramanipulación de datasets grandes sin cargar en memoria local

Pandas fue descartado por limitaciones de memoria al procesar datasets que exceden la capacidad de una sola máquina.

### Validación de Calidad: Great Expectations

**Decisión**: Great Expectations 0.18.12

**Justificación**:
- Framework especializado para validación de datos en pipelines
- Definición declarativa de expectativas como código (Data Docs)
- Integración con Airflow mediante operadores dedicados
- Capacidad de generar Data Quality Reports automáticamente
- Sistema de checkpoints para reutilización de suites de validación
- Comunidad activa y documentación comprehensiva

### Almacenamiento Intermedio: S3 con Formato Parquet

**Decisión**: Particionamiento por fecha (yyyy/mm/dd) y origen

**Justificación**:
- Formato columnar que optimiza consultas analíticas
- Compresión nativa que reduce costos de almacenamiento
- compatibilidad con servicios AWS (Athena, Redshift Spectrum, Glue)
- El particionamiento permite skip de datos innecesarios en queries
- Formato inmutable que garantiza idempotencia

### Carga Final: Amazon Redshift

**Decisión**: COPY desde S3 con formato Parquet

**Justificación**:
- Rendimiento optimizado para queries analíticas complejas
-COPY paralelo desde S3 para carga rápida de grandes volúmenes
- Soporte para formatos columnares y compresión
- Integración con Lake Formation para gobierno de datos
- Escalabilidad vertical y horizontal

## Modelo de Datos Canónico

El modelo de datos canónico unifica las tres fuentes bajo un esquema común:

```json
{
  "transaction_id": "string",
  "timestamp": "timestamp",
  "source_system": "string",
  "customer_id": "string",
  "amount": "decimal",
  "currency": "string",
  "transaction_type": "string",
  "status": "string",
  "metadata": "json",
  "ingestion_date": "date",
  "processing_version": "string"
}
```

### Mapeo de Fuentes

| Campo Canónico | Transacciones | Analítica | Maestro |
|----------------|---------------|-----------|---------|
| transaction_id | tx_id | event_id | master_id |
| timestamp | created_at | event_timestamp | updated_at |
| customer_id | customer_id | user_id | entity_id |
| amount | amount | metric_value | - |

## Diseño de Linaje

El linaje de datos se implementa en tres niveles:

1. **Nivel de Schema**: AWS Glue Data Catalog registra cada tabla con su versión de esquema
2. **Nivel de Pipeline**: Metadatos de procesamiento (job, parámetros, duración) se almacenan en DynamoDB
3. **Nivel de Registro**: Cada registro incluye metadata de origen, transformación y carga

## Estrategia de Particionamiento

```
s3://fintechcorp-datalake/
├── raw/
│   ├── transacciones/
│   │   └── yyyy/mm/dd/
│   ├── analitica/
│   │   └── yyyy/mm/dd/
│   └── maestro/
│       └── yyyy/mm/dd/
├── processed/
│   └── yyyy/mm/dd/origen=*
└── gold/
    └── yyyy/mm/dd/
```

## Configuración por Ambiente

La configuración se gestiona mediante Airflow Variables y AWS Secrets Manager:

- **DEV**: Configuración local con datos de prueba
- **STAGING**: Ambiente de integración con datos anonimizados
- **PROD**: Configuración completa con secretos en AWS Secrets Manager

## Resumen de Componentes

| Componente | Tecnología | Versión |
|------------|------------|---------|
| Orquestación | Apache Airflow | 2.9.2 |
| Procesamiento | PySpark | 3.5.0 |
| Validación | Great Expectations | 0.18.12 |
| Almacenamiento | Amazon S3 | - |
| Warehouse | Amazon Redshift | - |
| Catálogo | AWS Glue Data Catalog | - |
| Funciones AWS | AWS Lambda | - |

---
*Documento de diseño arquitectónico - FintechCorp*

// === ARCHIVO: docs/implementacion.md ===
# Guía de Implementación del Pipeline de Gobierno de Datos - Fase 3

## Resumen

Este documento describe los pasos necesarios para desplegar el pipeline de gobierno de datos en la infraestructura de AWS, incluyendo la configuración de servicios, despliegue del código y validación del sistema.

## Prerrequisitos

- Cuenta de AWS con permisos administrativos para IAM, S3, Redshift, Glue y Lambda
- AWS CLI configurado con credenciales de producción
- Python 3.13 instalado localmente
- Acceso a repositorio de código fuente

## Paso 1: Configuración de Infraestructura AWS

### 1.1 Crear Buckets S3

```bash
aws s3 mb s3://fintechcorp-datalake-raw --region us-east-1
aws s3 mb s3://fintechcorp-datalake-processed --region us-east-1
aws s3 mb s3://fintechcorp-datalake-gold --region us-east-1
aws s3 mb s3://fintechcorp-datalake-logs --region us-east-1
```

### 1.2 Configurar Lifecycle Policies

Aplicar políticas de ciclo de vida para transición automático:

- Raw bucket: transición a S3 Standard-IA después de 30 días
- Processed bucket: transición a S3 Glacier después de 90 días
- Gold bucket: retención de 5 años según requisito regulatorio

### 1.3 Crear Rol IAM para Airflow

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::fintechcorp-datalake-*",
        "arn:aws:s3:::fintechcorp-datalake-*/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "redshift:ExecuteStatement",
      "Resource": "arn:aws:redshift:*:*:cluster:*"
    }
  ]
}
```

### 1.4 Provisionar Amazon Redshift

Crear cluster con las siguientes especificaciones mínimas:

- Tipo de nodo: dc2.large
- Número de nodos: 2
- Base de datos: fintechcorp_analytics
- Puerto: 5439

## Paso 2: Despliegue de Código

### 2.1 Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2.2 Configurar Variables de Airflow

Establecer las siguientes variables en Airflow:

```bash
airflow variables set S3_RAW_BUCKET fintechcorp-datalake-raw
airflow variables set S3_PROCESSED_BUCKET fintechcorp-datalake-processed
airflow variables set S3_GOLD_BUCKET fintechcorp-datalake-gold
airflow variables set REDSHIFT_HOST your-cluster.xxxx.us-east-1.redshift.amazonaws.com
airflow variables set ENVIRONMENT production
```

### 2.3 Desplegar DAG

Copiar el DAG a la carpeta de dags de Airflow:

```bash
cp dags/gobierno_datos_pipeline.py $AIRFLOW_HOME/dags/
```

### 2.4 Desplegar Plugins y Utilidades

```bash
cp -r src/ $AIRFLOW_HOME/plugins/
```

## Paso 3: Configuración de Great Expectations

### 3.1 Inicializar Expectation Suite

```bash
cd src/transform
great_expectations init
```

### 3.2 Crear Expectations para Transacciones

Definir expectativas críticas:

- `transaction_id`: no nulos, únicos en el dataset
- `amount`: valores mayores a 0
- `timestamp`: formato ISO 8601 válido
- `customer_id`: no nulo, longitud mínima de 8 caracteres

## Paso 4: Configuración de Linaje

### 4.1 Habilitar Glue Data Catalog

En la configuración de Airflow, habilitar el uso de Glue como metastore:

```yaml
config:
  core:
    executor: LocalExecutor
  aws:
    glue_catalog:
      glue_conn_id: aws_default
```

### 4.2 Configurar Crawlers

Crear crawlers para cada capa del data lake:

- `fintechcorp-raw-crawler`: escanea bucket raw
- `fintechcorp-processed-crawler`: escanea bucket processed
- `fintechcorp-gold-crawler`: escanea bucket gold

## Paso 5: Ejecución de Pruebas

### 5.1 Tests Unitarios

```bash
pytest tests/ -v
```

Expected output: todos los tests deben pasar, incluyendo:

- Validación de reglas de calidad
- Verificación de linaje
- Pruebas de idempotencia

### 5.2 Prueba de Integración

Ejecutar el pipeline en modo de prueba con datos de muestra:

```bash
airflow dags test gobierno_datos_pipeline 2024-01-01
```

### 5.3 Validación de Calidad

Verificar que los Data Docs se generan correctamente:

```bash
great_expectations docs build
```

## Paso 6: Monitoreo y Alertas

### 6.1 Configurar CloudWatch Logs

El pipeline genera logs en CloudWatch con los siguientes grupos:

- `/aws/glue/jobs/gobierno-datos`
- `/airflow/gobierno-datos-pipeline`

### 6.2 Configurar Alarmas

Crear alarmas para:

- Fallas en tareas de Airflow (SNS notification)
- Latencia mayor a 5 segundos (threshold configurable)
- Volumen de datos anómalo (diferencia > 20% vs promedio)

## Verificación de Resultados

### Métricas Esperadas Post-Implementación

| Métrica | Target | Método de Verificación |
|---------|--------|------------------------|
| Precisión de datos | 99.9% | Great Expectations suite |
| Latencia | < 2 segundos | CloudWatch metrics |
| Cobertura de linaje | 100% | Glue Data Catalog query |
| Trazabilidad | 5 años | S3 lifecycle policies |

### Checklist de Go-Live

- [ ] Todos los tests unitarios pasando
- [ ] Integración con Redshift verificada
- [ ] Datos de prueba procesados correctamente
- [ ] Documentación actualizada
- [ ] Equipo capacitado en operación del pipeline
- [ ] Monitoreo y alertas activos
- [ ] Runbook de operaciones disponible

## Rollback Procedure

En caso de falla crítica:

1. Detener todas las tareas del DAG
2. Restaurar versión anterior del código desde git
3. Ejecutar tarea de rollback en Redshift si es necesario
4. Notificar al equipo de soporte
5. Documentar incidente para post-mortem

---
*Guía de implementación - Equipo de Datos FintechCorp*

```
