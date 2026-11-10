"""Sinh anh TAM cho M1: san, tuong (mat tren + mat truoc), nhan vat 4 huong.
Day la anh giu cho, se duoc thay bang tileset va nhan vat that o M2.
Chay: python3 tools/pixel/gen_placeholder.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from palette import rgb

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "assets", "placeholder")
T = 16


def rect(img, x0, y0, x1, y1, key):
    """To mau hinh chu nhat, toa do bao gom ca hai dau."""
    color = rgb(key) + (255,)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if 0 <= x < img.width and 0 <= y < img.height:
                img.putpixel((x, y), color)


def floor_tile():
    img = Image.new("RGBA", (T, T), rgb("conc") + (255,))
    # Chi danh dau goc o bang 1 diem toi + 1 diem sang, khong ke ca duong,
    # de san khong thanh luoi o vuong.
    rect(img, T - 1, T - 1, T - 1, T - 1, "conc_sh")
    rect(img, 0, 0, 0, 0, "conc_hi")
    return img


def wall_top_tile():
    img = Image.new("RGBA", (T, T), rgb("wall_sh") + (255,))
    return img


def wall_face_tile():
    img = Image.new("RGBA", (T, T), rgb("wall") + (255,))
    rect(img, 0, 0, T - 1, 1, "wall_hi")           # mep tren hung nang
    rect(img, 0, T - 4, T - 1, T - 2, "wall_sh")   # chan tuong
    rect(img, 0, T - 1, T - 1, T - 1, "outline")   # duong tiep dat
    return img


def player_frame(facing):
    """Nhan vat tam 32x32, chan cham day anh. facing: down/up/left/right."""
    img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    # Vien: ve khoi lon hon 1 px bang mau outline truoc
    rect(img, 9, 5, 22, 18, "outline")     # dau
    rect(img, 8, 17, 23, 26, "outline")    # than + tay
    rect(img, 11, 26, 20, 31, "outline")   # chan
    # Dau
    rect(img, 10, 6, 21, 17, "wall_hi")    # da (mau tam)
    rect(img, 10, 6, 21, 9, "wood_sh")     # toc
    # Than
    rect(img, 11, 18, 20, 25, "blue")
    rect(img, 11, 18, 20, 19, "blue_hi")
    rect(img, 9, 18, 10, 24, "blue_sh")    # tay trai
    rect(img, 21, 18, 22, 24, "blue_sh")   # tay phai
    # Chan
    rect(img, 12, 26, 15, 30, "metal_sh")
    rect(img, 17, 26, 19, 30, "metal_sh")
    rect(img, 16, 26, 16, 30, "outline")

    if facing == "down":
        rect(img, 13, 12, 14, 13, "outline")
        rect(img, 17, 12, 18, 13, "outline")
    elif facing == "up":
        rect(img, 10, 6, 21, 15, "wood_sh")   # nhin tu sau: toc phu gan het dau
    elif facing == "left":
        rect(img, 16, 6, 21, 15, "wood_sh")   # toc phia sau gay
        rect(img, 11, 12, 12, 13, "outline")
    elif facing == "right":
        rect(img, 10, 6, 15, 15, "wood_sh")
        rect(img, 19, 12, 20, 13, "outline")
    return img


def player_sheet():
    sheet = Image.new("RGBA", (32 * 4, 32), (0, 0, 0, 0))
    for i, facing in enumerate(["down", "up", "left", "right"]):
        sheet.paste(player_frame(facing), (i * 32, 0))
    return sheet


def main():
    os.makedirs(OUT, exist_ok=True)
    files = {
        "floor_tam.png": floor_tile(),
        "wall_top_tam.png": wall_top_tile(),
        "wall_face_tam.png": wall_face_tile(),
        "player_tam.png": player_sheet(),
    }
    for name, img in files.items():
        img.save(os.path.join(OUT, name))
        print(f"Da ghi assets/placeholder/{name} {img.size}")


if __name__ == "__main__":
    main()
