"""news-image-20261124: write the 24 November 2026 world-news image.

Deterministic, no network: copies the image this repository holds
(ead97dd4-15bd-491c-8c00-2925eff30230.png) to /output/entry.png,
byte for byte, then checks the copy matches the source.
Running it twice writes the same bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "ead97dd4-15bd-491c-8c00-2925eff30230.png")
OUT_DIR = "/output"
OUT_NAME = "entry.png"
CHUNK_SIZE = 65536


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"missing source image: {SRC}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, OUT_NAME)
    shutil.copyfile(SRC, out_path)
    if sha256(SRC) != sha256(out_path):
        print("copy does not match source", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    main()
