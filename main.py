"""make.fun news-image-20261124 entry (Python 3.13, standard library only).

Copies the pre-built entry.png in this repository to /output/entry.png.
Deterministic: the same bytes are written on every run, no network.
Local test: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST = os.path.join(OUTPUT_DIR, "entry.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
# Copy, don't re-render: the image is fixed for 24 November 2026.
shutil.copyfile(SOURCE, DEST)
