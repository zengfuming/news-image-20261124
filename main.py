"""news-image-20261124: write the 24 November 2026 world-news image.

Deterministic, no network: copies the image this repository holds
(entry.png) to /output/entry.png, byte for byte. Running it twice
writes the same bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))

if __name__ == "__main__":
    main()
