#!/usr/bin/env python3
"""Compila index.html portable a partir de src/template.html y data/*.json.

Uso:
    python3 scripts/build.py

No requiere librerías externas (solo Python 3 estándar).
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
TEMPLATE = ROOT / "src" / "template.html"
OUTPUT = ROOT / "index.html"


def main() -> None:
    vocab = json.loads((DATA_DIR / "vocabulario_n5.json").read_text(encoding="utf-8"))
    kanji_bundle = json.loads((DATA_DIR / "kanji_examen_n5.json").read_text(encoding="utf-8"))
    questions = kanji_bundle["questions"]
    tips = kanji_bundle["tips"]

    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace("__VOCAB_JSON__", json.dumps(vocab, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("__KANJI_JSON__", json.dumps(questions, ensure_ascii=False, separators=(",", ":")))
    html = html.replace("__TIPS_JSON__", json.dumps(tips, ensure_ascii=False, separators=(",", ":")))

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"OK: {OUTPUT.name} generado ({len(vocab)} palabras, {len(questions)} preguntas Kanji, {len(tips)} tips)")


if __name__ == "__main__":
    main()
