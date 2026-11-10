# Observatorio de incidentes y fallos de control de IA

Proyecto público para registrar incidentes y revelaciones verificadas sobre agentes de IA.

## Activar la web
En **Settings → Pages → Build and deployment**, elegir **Deploy from a branch**, rama **main**, carpeta **/(root)** y pulsar **Save**.

URL prevista: https://nacho-iesps.github.io/observatorio-ia/

## Criterios
- Separar fecha del incidente y fecha de publicación.
- Distinguir producción, uso interno y evaluaciones controladas.
- Documentar el control vulnerado, la evidencia, sus límites y las fuentes primarias.
- No atribuir intención ni daños sin evidencia.
- No confundir una vulnerabilidad técnica con comportamiento autónomo desalineado.

## Datos
El archivo `data/incidentes.json` contiene el registro. Está inicialmente vacío hasta verificar las fichas.

## Automatización
El workflow `validate.yml` comprueba diariamente la integridad del archivo de datos. **No busca ni publica noticias nuevas**. La ingesta de novedades necesitará un flujo adicional de detección y verificación editorial.
