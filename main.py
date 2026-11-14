"""food-picture-01 round 2 entry: copy the image beside this file to /output/entry.png.

The image is a food photograph made for this competition in this build
session: a thick ribeye steak sizzling in a black cast iron skillet,
butter being basted over its charred, glistening crust, rosemary and
roasted garlic at the side, wisps of steam, warm dramatic side light
on a dark background. Unlike round 1's ramen, this is a different
subject entirely — a sizzling, action-filled plate instead of a calm
bowl — so it competes on its own appetite appeal rather than against
other ramen. Three dishes were generated and compared
in-session (this steak, Korean fried chicken in glossy gochujang
glaze, and a molten chocolate lava cake); the steak won for its
butter-basting action, its gloss and char, and how clearly the single
big subject reads even at ~300 px. The chosen image was downscaled to
1024x683 so it fits the gate (at most 1 MiB and 1024x1024), and is
shipped beside the program; the program itself does no drawing, only
an exact copy.

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
