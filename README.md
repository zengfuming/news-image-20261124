# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)

Sum up 24 November 2026's world news in one image: a newspaper front
page with five stories from that day.

## Run it

```sh
python3 main.py
# writes /output/entry.png (1024x1024 PNG, 721820 bytes)
```

The program needs Python 3.13 and nothing else. It takes no arguments,
reads only the image file in this repository, uses no network, and exits
non-zero if the source image is missing or the copy does not match it
byte for byte. Run it twice and the two outputs are identical.

## What's in the image

- **HUANG RETURNS — NVIDIA SOARS:** Jensen Huang is reinstated as
  Nvidia CEO after resigning on 12 November; shares surge.
- **NATO: SPACE DEFENCE:** NATO's chief vows a space defence response
  after reports of a possible Russian nuclear-armed satellite.
- **COP31 COLLAPSES:** the climate summit in Antalya ends with no
  overarching agreement over fossil fuels.
- **IRAN STRIKES US TARGETS IN BAHRAIN:** Iran's third strike on US
  targets in Bahrain after a two-month lull, followed by US retaliation.
- **Ukraine energy grid hit ahead of winter:** Russian attacks on
  Ukraine's energy grid intensify as winter approaches.

## Files

- `main.py` — the entrypoint. Copies the image to `/output/entry.png`
  and verifies the copy with SHA-256.
- `ead97dd4-15bd-491c-8c00-2925eff30230.png` — the image itself,
  1024x1024, under the 1 MiB limit.
- `LICENSE` — MIT.
