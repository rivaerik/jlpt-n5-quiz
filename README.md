# 🇯🇵 JLPT N5 Studio — Portable y 100% Offline

Aplicación web **totalmente portable y sin dependencias externas** (cero CDNs, cero instalaciones, cero servidores) para practicar el examen **JLPT N5**:
- **644 palabras** del vocabulario N5 con lectura (hiragana + romaji), forma diccionario, forma TE y grupo verbal en verbos, y clasificación `い`/`な` en adjetivos.
- **72 preguntas de Kanji estilo examen oficial** (*Mondai 1* de lecturas y *Mondai 2* de trampas visuales/okurigana) + **15 tarjetas de trucos** entre preguntas.
- **⏱️ Sprint Rápido (3 / 5 / 10 min)** con temporizador y recordatorios de consejos clave para sesiones cortas de estudio.
- **📊 Panel de Progreso** guardado en el navegador (palabras dominadas por categoría, racha diaria y precisión) + **Modo Claro / Oscuro**.

## 🚀 Cómo usarla (funciona incluso sin internet)
1. Descargá el repositorio (`Code` → `Download ZIP`) y descomprimilo, o clonalo con `git clone`.
2. Hacé **doble clic en `index.html`** para abrirla en cualquier navegador. No requiere internet ni librerías externas.

## ☁️ Cómo subirlo a tu GitHub
```bash
git init
git add .
git commit -m "Versión inicial: JLPT N5 Studio portable"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/jlpt-n5-quiz.git
git push -u origin main
```

### (Opcional) Publicarlo gratis en GitHub Pages
En tu repositorio de GitHub andá a **Settings → Pages → Build and deployment → Source: GitHub Actions**. Cada `git push` a `main` publicará la última versión automáticamente.

## 🛠️ Cómo meter actualizaciones
```text
├── index.html                           # Archivo portable 100% offline (autogenerado)
├── src/template.html                    # Código fuente HTML/CSS/JS sin dependencias
├── data/
│   ├── vocabulario_n5.json              # 644 palabras (editable)
│   ├── kanji_examen_n5.json             # 72 preguntas Kanji + 15 tips (editable)
│   └── Vocabulario_JLPT_N5_Completo.xlsx# Excel maestro de referencia
├── scripts/build.py                     # Recompila index.html (solo Python 3 estándar)
└── .github/workflows/pages.yml          # Publicación automática en GitHub Pages
```

Cuando edites `data/*.json` o `src/template.html`, corré:
```bash
python3 scripts/build.py
git add .
git commit -m "Actualización"
git push
```
