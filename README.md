# JLPT N5 Quiz

Aplicación web portable para practicar vocabulario y kanji del examen JLPT N5. Corre directo en el navegador sin servidor, sin instalaciones y sin conexión a internet.

**Probar online:** https://rivaerik.github.io/jlpt-n5-quiz/ *(una vez activado GitHub Pages)*

## Qué incluye

- **Vocabulario (644 palabras):** práctica aleatoria con filtro por tipo (verbos, adjetivos, otros) y tema. En verbos muestra grupo, forma diccionario y forma て; en adjetivos indica si es い o な.
- **Kanji Examen (72 preguntas):** simulacro estilo *Mondai 1* (lecturas en hiragana) y *Mondai 2* (trampas visuales y okurigana), con explicaciones y tarjetas de trucos frecuentes.
- **Sprint por tiempo:** sesiones rápidas de 3, 5 o 10 minutos con recordatorios de examen.
- **Progreso local:** guarda palabras dominadas, rachas y precisión en el navegador, con modo claro y oscuro.

## Uso offline

1. Descargá el repositorio (`Code` → `Download ZIP`) y descomprimilo.
2. Abrí `index.html` con doble clic en cualquier navegador.

## Desarrollo y aportes

Los datos y la plantilla están separados para facilitar mejoras y correcciones:

- `src/template.html` — interfaz y lógica en HTML, CSS y JS puro.
- `data/vocabulario_n5.json` y `data/kanji_examen_n5.json` — bancos de preguntas editables.
- `scripts/build.py` — recompila `index.html` usando solo Python 3 estándar.

Si modificás la plantilla o los JSON, regenerá el archivo portable con:

```bash
python3 scripts/build.py
