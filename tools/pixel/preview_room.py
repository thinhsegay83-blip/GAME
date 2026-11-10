"""Dung anh MO PHONG khung hinh game tu ban do + anh tam.
KHONG phai anh chup tu Godot. Luat ve giong scripts/world/test_room.gd:
tuong co tuong phia duoi -> mat tren; nguoc lai -> mat truoc.
Chay: python3 tools/pixel/preview_room.py
"""
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T, VIEW_W, VIEW_H, SCALE = 16, 640, 360, 2


def load(name):
    return Image.open(os.path.join(ROOT, "assets", "placeholder", name)).convert("RGBA")


def main():
    with open(os.path.join(ROOT, "data", "maps", "test_room.txt"), encoding="utf-8") as f:
        rows = [line.strip() for line in f if line.strip()]
    floor, top, face = load("floor_tam.png"), load("wall_top_tam.png"), load("wall_face_tam.png")
    player = load("player_tam.png").crop((0, 0, 32, 32))  # khung nhin xuong

    def is_wall(x, y):
        if y < 0 or y >= len(rows) or x < 0 or x >= len(rows[y]):
            return True
        return rows[y][x] == "#"

    world = Image.new("RGBA", (len(rows[0]) * T, len(rows) * T))
    spawn = (1, 2)
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == "P":
                spawn = (x, y)
            tile = floor if ch != "#" else (top if is_wall(x, y + 1) else face)
            world.paste(tile, (x * T, y * T))

    # Nguoi choi: goc toa do o chan, sprite lech len 16 px (giong player.tscn)
    px, py = spawn[0] * T + T // 2, spawn[1] * T + T // 2
    world.alpha_composite(player, (px - 16, py - 32))

    # Camera bam theo nguoi choi, bi chan boi mep ban do
    cx = min(max(px - VIEW_W // 2, 0), world.width - VIEW_W)
    cy = min(max(py - 16 - VIEW_H // 2, 0), world.height - VIEW_H)
    view = world.crop((cx, cy, cx + VIEW_W, cy + VIEW_H))
    view = view.resize((VIEW_W * SCALE, VIEW_H * SCALE), Image.NEAREST)
    out = os.path.join(ROOT, "claude", "design", "preview_m1.png")
    view.convert("RGB").save(out)
    print(f"Da ghi claude/design/preview_m1.png {view.size}, ban do {world.size}")


if __name__ == "__main__":
    main()
