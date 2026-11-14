"""food-picture-01 entry: copy the image beside this file to /output/entry.png.

The image is a food photograph made for this competition in this build
session: a steaming bowl of tonkotsu ramen — glossy noodles lifted in
creamy broth, a halved soft-boiled egg with a running yolk, chashu pork
and green onions, wisps of steam, warm side light on a dark wooden
table. Two dishes were generated and compared in-session (a smash
burger and this ramen); the ramen won for its visible steam, gloss and
melt, its clean composition with no artefacts, and how clearly the bowl
reads even at ~300 px. The chosen image was downscaled to 1024x683 so
it fits the gate (at most 1 MiB and 1024x1024), and is shipped beside
the program; the program itself does no drawing, only an exact copy.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).with_name("entry.png")
OUTPUT_NAME = "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, out_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
