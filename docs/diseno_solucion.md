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