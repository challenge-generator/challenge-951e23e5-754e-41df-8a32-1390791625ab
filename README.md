# Implementación de Gobierno de Datos en una Empresa de Servicios Financieros

La empresa de servicios financieros 'FintechCorp' requiere un gobierno de datos robusto para gestionar sus proyectos de mediana complejidad en ciencia de datos. Los datos se originan desde el 'sistema de origen de transacciones', 'plataforma de analítica' y 'almacenamiento de datos maestro'. El gobierno de datos debe asegurar la calidad, consistencia y trazabilidad de los datos a través de todos los sistemas. El gobierno de datos se mide por la precisión de los datos en un 99.9%, con una latencia máxima de 2 segundos en la actualización de los registros. El gobierno de datos debe manejar volúmenes de hasta 10 millones de transacciones diarias y asegurar la trazabilidad de los datos por al menos 5 años.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Implementación de Gobierno de Datos |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 2 semanas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Evaluación de la situación actual

**Objetivo:** Identificar las brechas actuales en el gobierno de datos de FintechCorp.

**Tiempo estimado:** 3 días

**Instrucciones:**

- Analiza los flujos de datos actuales desde el sistema de origen de transacciones, plataforma de analítica y almacenamiento de datos maestro.
- Identifica las brechas en la calidad, consistencia y trazabilidad de los datos.
- Documenta las brechas identificadas y propone mejoras potenciales.

**Entregable:** Reporte de evaluación del gobierno de datos actual.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los marcos de trabajo DAMA, TOGAF y CMMI para la evaluación.
- Piensa en cómo los datos fluyen entre los sistemas y cómo se pueden asegurar su calidad y consistencia.

</details>

### Fase 2: Diseño de la solución de gobierno de datos

**Objetivo:** Diseñar una solución de gobierno de datos que aborde las brechas identificadas.

**Tiempo estimado:** 5 días

**Instrucciones:**

- Propone un diseño que asegure la calidad, consistencia y trazabilidad de los datos.
- Considera los marcos de trabajo DAMA, TOGAF y CMMI en tu diseño.
- Documenta el diseño propuesto y justifica tus decisiones.

**Entregable:** Documento de diseño de la solución de gobierno de datos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo puedes asegurar la calidad de los datos en cada etapa del flujo de datos.
- Piensa en cómo puedes garantizar la consistencia de los datos entre los sistemas.

</details>

### Fase 3: Implementación de la solución de gobierno de datos

**Objetivo:** Implementar la solución de gobierno de datos propuesta.

**Tiempo estimado:** 5 días

**Instrucciones:**

- Implementa el diseño propuesto en la fase anterior.
- Asegura que la solución cumpla con los requisitos de calidad, consistencia y trazabilidad de los datos.
- Documenta la implementación y realiza pruebas para validar la solución.

**Entregable:** Solución de gobierno de datos implementada y documentada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo puedes asegurar que la solución cumpla con los requisitos de calidad, consistencia y trazabilidad de los datos.
- Piensa en cómo puedes validar la solución implementada.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es el gobierno de datos y por qué es importante para FintechCorp?
- **paraQueSirve**: ¿Para qué sirve el gobierno de datos en el contexto de FintechCorp?
- **comoSeUsa**: ¿Cómo se usa el gobierno de datos para asegurar la calidad, consistencia y trazabilidad de los datos en FintechCorp?
- **erroresComunes**: ¿Cuáles son los errores comunes en la implementación del gobierno de datos y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la implementación del gobierno de datos en FintechCorp?

## Criterios de Evaluacion

- Identificación de brechas en el gobierno de datos actual.
- Propuesta de mejoras para el gobierno de datos.
- Diseño de una solución de gobierno de datos que aborde las brechas identificadas.
- Implementación de la solución de gobierno de datos propuesta.
- Validación de la solución implementada.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
