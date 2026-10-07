# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Implementación de Gobierno de Datos en una Empresa de Servicios Financieros**.

| | |
|---|---|
| Tema | Implementación de Gobierno de Datos |
| Nivel | senior-l2 |
| Chapter | Ciencia de Datos — Ingeniero de Datos |
| Especialidad | Ingeniero de datos |
| Stack | Python 3.13 / Apache Airflow 2.9 |
| Patron arquitectonico | Pipeline ETL/ELT con orquestación en Airflow, capas separadas para extracción, transformación con reglas de calidad, y carga con idempotencia. Linaje de datos con AWS Glue Data Catalog y trazabilidad con particionado en S3 (formato Parquet). |
| Tiempo estimado | 2 semanas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `dags/ con el DAG de Airflow o el orquestador equivalente`
- `src/extract con los lectores de origen`
- `src/transform con las transformaciones y las reglas de calidad`
- `src/load con los escritores de destino`
- `tests/ con casos de validacion de resultados esperados`
- `conf/ con la configuracion por ambiente`

Dependencias:

- apache-airflow 2.9.2
- pyspark 3.5.0
- great-expectations 0.18.12
- boto3 1.34.0
- pydantic 2.7.1
- pytest 8.1.1
- aws-glue-sessions n/a
- aws-lake-formation n/a
- pyyaml 6.0.1

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Evaluación de la situación actual**: Reporte de evaluación del gobierno de datos actual.
- **Fase 2 — Diseño de la solución de gobierno de datos**: Documento de diseño de la solución de gobierno de datos.
- **Fase 3 — Implementación de la solución de gobierno de datos**: Solución de gobierno de datos implementada y documentada.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Archivos que la arquitectura declara (3 de 16)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `dags/gobierno_datos_pipeline.py`
- [ ] `src/extract/transacciones_reader.py`
- [ ] `src/extract/analitica_reader.py`

### Presentes (13)

- `pyproject.toml`
- `src/schemas/transacciones_schema.json`
- `src/transform/reglas_calidad.py`
- `src/transform/linaje_transform.py`
- `src/load/redshift_loader.py`
- `src/load/s3_loader.py`
- `tests/test_reglas_calidad.py`
- `tests/test_linaje.py`
- `tests/test_idempotencia.py`
- `conf/config_dev.yaml`
- `docs/reporte_evaluacion.md`
- `docs/diseno_solucion.md`
- `docs/implementacion.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `dags`
- `src/extract`
- `src/transform`
- `src/load`
- `src/schemas`
- `tests`
- `conf`
- `docs`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **Pipeline ETL/ELT con orquestación en Airflow, capas separadas para extracción, transformación con reglas de calidad, y carga con idempotencia. Linaje de datos con AWS Glue Data Catalog y trazabilidad con particionado en S3 (formato Parquet).**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Seniority Senior
- Brecha que el reto ataca: Gestiona proyectos de mediana complejidad de Gobierno de Datos a través de marcos de trabajo como los propuestos en DAMA, TOGAF, CMMI.
- Mision: Candidato con experiencia avanzada en ingeniería de datos, trabajando en equipos distribuidos en contextos empresariales complejos.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
