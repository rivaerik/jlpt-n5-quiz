# JLPT N5 Studio (v2.0)

El objetivo de este proyecto es **unificar en una sola herramienta portable todo lo que va a estar sí o sí en el examen JLPT N5**: vocabulario completo, kanjis, partículas, negaciones verbales, contadores, calendario y las trampas más repetidas de exámenes oficiales anteriores.

Corre directo en el navegador sin servidor, sin instalaciones, sin librerías externas y **100% offline**.

**Probar online:** https://rivaerik.github.io/jlpt-n5-quiz/

## Qué unifica la v2.0

- **Vocabulario (644 palabras):** práctica aleatoria por tipo y tema. En verbos muestra grupo verbal, forma diccionario, forma て y forma ない; en adjetivos indica si es い o な.
- **Kanji Examen (72 preguntas + 15 trampas):** simulacro estilo *Mondai 1* (lecturas en hiragana) y *Mondai 2* (trampas visuales y okurigana), con explicaciones y tarjetas flash entre preguntas.
- **Gramática y Partículas (65 preguntas):** entrenamiento directo sobre partículas (`に / で / を / へ / は / が / と / や / も`), negaciones irregulares (`〜ない`), estructuras verbales, paráfrasis (*Mondai 4*), KOSOADO, comparaciones, fechas y contadores.
- **Biblioteca N5 completa:** las 3 guías de estudio íntegras con tablas y buscador instantáneo para consultar cualquier regla sin salir de la app.
- **Sprint por tiempo (3 / 5 / 10 min) + Progreso local:** sesiones cortas contrarreloj con recordatorios de examen, modo claro/oscuro y seguimiento de dominio guardado en el navegador.

## Uso offline (portable)

1. Descargá el repositorio (`Code` → `Download ZIP`) y descomprimilo.
2. Abrí `index.html` con doble clic en cualquier navegador.

## Estructura y actualizaciones

- `index.html` — aplicación portable lista para usar (autogenerada).
- `src/template.html` — código fuente HTML, CSS y JS puro.
- `data/vocabulario_n5.json`, `data/kanji_examen_n5.json`, `data/gramatica_n5.json`, `data/biblioteca_n5.json` — bancos de preguntas y guías editables.
- `scripts/build.py` — recompila `index.html` usando solo Python 3 estándar (`python3 scripts/build.py`).

Las sugerencias y *Pull Requests* para sumar oraciones o mejoras son bienvenidas.
