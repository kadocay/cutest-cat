#!/usr/bin/env python3
"""cutest-cat-01 entry (Python 3.13, standard library only).

Copies the cat picture (entry.png, in this repository) to /output/entry.png.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(OUTPUT_DIR, "entry.png"))
