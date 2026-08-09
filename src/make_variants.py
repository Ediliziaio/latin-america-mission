#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera le varianti piccole delle immagini responsive.

    python3 src/make_variants.py

Richiede Pillow (pip install Pillow). Va rilanciato solo quando aggiungi o
sostituisci un'immagine di uno slot marcato "responsive" in src/content.py.
La build normale (src/build.py) non ha dipendenze: usa le varianti se ci sono.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import IMAGES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMGDIR = os.path.join(ROOT, "assets", "img")


def main():
    from PIL import Image  # import tardivo: serve solo qui

    made = 0
    for slot, spec in IMAGES.items():
        for width in spec.get("responsive", []):
            src = os.path.join(IMGDIR, spec["file"])
            if not os.path.exists(src):
                continue
            stem, ext = os.path.splitext(spec["file"])
            dst = os.path.join(IMGDIR, "{}-{}{}".format(stem, width, ext))
            im = Image.open(src)
            if im.width <= width:
                continue
            small = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
            small.save(dst, quality=72, optimize=True, progressive=True, subsampling=1)
            made += 1
            print("  {:<34} {}x{}  {} kB".format(
                os.path.basename(dst), small.width, small.height,
                round(os.path.getsize(dst) / 1024)))
    print("  {} varianti generate".format(made))


if __name__ == "__main__":
    main()
