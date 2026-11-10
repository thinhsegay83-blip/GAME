"""Bang mau chuan cho game "Toi La Sinh Vien Bach Khoa".
Tong: am, nang Viet Nam. Goc nhin 3/4, tile 16x16.
Moi nhom co 3 bac: hi (highlight) / base / sh (shadow).
Khong dung den thuan va trang thuan - outline la nau sam, trang la trang nga,
de moi mau deu nam trong tong am.
"""

PALETTE = {
    # Co, cay xanh san truong
    "grass_hi": "#8FC855",
    "grass":    "#5FA03C",
    "grass_sh": "#3D7030",

    # Be tong, san truong, loi di
    "conc_hi":  "#DCD2BD",
    "conc":     "#BCAE96",
    "conc_sh":  "#897D6A",

    # Gach dat, mai ngoi, duong gach
    "brick_hi": "#E08A5A",
    "brick":    "#C2603A",
    "brick_sh": "#8C3F28",

    # Tuong vang kem (dac trung truong hoc VN)
    "wall_hi":  "#FFE9B8",
    "wall":     "#F2CD84",
    "wall_sh":  "#C49A55",

    # Go: ban ghe, cua, bang tin
    "wood_hi":  "#B5804E",
    "wood":     "#8C5A33",
    "wood_sh":  "#5E3B21",

    # Kim loai, khung cua so, quat, lan can
    "metal_hi": "#9FB8C4",
    "metal":    "#6D8A9A",
    "metal_sh": "#45606E",

    # Xanh duong nhan: bang, bien bao, dong phuc
    "blue_hi":  "#6FB4D6",
    "blue":     "#3A7CA5",
    "blue_sh":  "#24516E",

    # Ba mau he thong
    "outline":  "#2B2320",  # nau sam - vien moi vat the
    "ivory":    "#FFF6E4",  # trang nga - diem sang manh nhat
    "shade":    "#4A3A52",  # tim am - dung cho bong do tren mat dat
}

ROLES = {
    "grass": "Co, bui cay, tan la nhin tu tren",
    "conc":  "San be tong, loi di, bac thang, san nha",
    "brick": "Gach dat, mai ngoi, bon hoa, duong gach do",
    "wall":  "Tuong nha vang kem - mau chu dao cua truong",
    "wood":  "Ban ghe giang duong, cua go, bang tin",
    "metal": "Khung cua so, quat tran, lan can, cot den",
    "blue":  "Bang viet, bien chi dan, chi tiet nhan",
}


def rgb(key):
    h = PALETTE[key].lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def count():
    return len(PALETTE)


if __name__ == "__main__":
    print(f"Tong so mau: {count()}")
    for k, v in PALETTE.items():
        print(f"  {k:10s} {v}")
