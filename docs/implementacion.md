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