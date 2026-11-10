import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
from palette import PALETTE, ROLES, rgb

GROUPS = ["grass", "conc", "brick", "wall", "wood", "metal", "blue"]
CELL, PAD = 64, 8
W = PAD + 3 * (CELL + PAD)
H = PAD + (len(GROUPS) + 1) * (CELL + PAD)

img = Image.new("RGB", (W, H), rgb("outline"))
d = ImageDraw.Draw(img)

for r, g in enumerate(GROUPS):
    for c, suf in enumerate(["_hi", "", "_sh"]):
        key = g + suf
        x = PAD + c * (CELL + PAD)
        y = PAD + r * (CELL + PAD)
        d.rectangle([x, y, x + CELL - 1, y + CELL - 1], fill=rgb(key))

# hang cuoi: 3 mau he thong
for c, key in enumerate(["outline", "ivory", "shade"]):
    x = PAD + c * (CELL + PAD)
    y = PAD + len(GROUPS) * (CELL + PAD)
    d.rectangle([x, y, x + CELL - 1, y + CELL - 1], fill=rgb(key))
    d.rectangle([x, y, x + CELL - 1, y + CELL - 1], outline=rgb("ivory"))

out = "/home/user/GAME/claude/design/palette.png"
img.save(out)
print(f"Da ghi {out} ({W}x{H}), {len(PALETTE)} mau")
