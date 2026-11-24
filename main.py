"""news-image-20261124: write the 24 November 2026 world-news image.

Deterministic, no network: copies the image this repository holds
(ead97dd4-15bd-491c-8c00-2925eff30230.png) to /output/entry.png,
byte for byte. Running it twice writes the same bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ead97dd4-15bd-491c-8c00-2925eff30230.png")

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))

if __name__ == "__main__":
    main()
