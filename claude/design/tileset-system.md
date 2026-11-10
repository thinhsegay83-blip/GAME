# Design System — Tileset

> Trạng thái: **bản nháp B1, chờ duyệt**
> Game: game mới, bối cảnh Bách Khoa (xem `gdd.md`) · Engine: Godot 4

## 1. Quy cách kỹ thuật

| Thông số | Giá trị | Lý do |
|---|---|---|
| Kích thước tile | **16×16 px** | Nhân vật 32×32 cao đúng 2 tile — tỷ lệ người/cảnh tự nhiên |
| Góc nhìn | **3/4 top-down** | Thấy được mặt trước tường → không gian có chiều sâu |
| Số màu toàn game | **24** | Đủ phong phú, vẫn giữ được kỷ luật pixel art |
| Phóng to khi hiển thị | Bội số nguyên (×2, ×3, ×4) | Tránh méo pixel |
| Lọc texture | **Nearest** (tắt khử răng cưa) | Bắt buộc với pixel art |

## 2. Tông màu chủ đạo

Ấm, nắng Việt Nam. Ba quy tắc nền:

1. **Không dùng đen thuần và trắng thuần.** Viền là nâu sẫm `#2B2320`, điểm sáng là trắng ngà `#FFF6E4`. Đen/trắng thuần làm hình bị lạnh và cứng.
2. **Bóng đổ ngả tím ấm** `#4A3A52`, không ngả xám. Đây là thứ tạo cảm giác nắng.
3. **Nguồn sáng thống nhất: trên — trái.** Mọi tile phải đổ bóng về phía dưới — phải.

## 3. Bảng màu

| Nhóm | Highlight | Base | Shadow | Dùng cho |
|---|---|---|---|---|
| `grass` | `#8FC855` | `#5FA03C` | `#3D7030` | Co, bui cay, tan la nhin tu tren |
| `conc` | `#DCD2BD` | `#BCAE96` | `#897D6A` | San be tong, loi di, bac thang, san nha |
| `brick` | `#E08A5A` | `#C2603A` | `#8C3F28` | Gach dat, mai ngoi, bon hoa, duong gach do |
| `wall` | `#FFE9B8` | `#F2CD84` | `#C49A55` | Tuong nha vang kem - mau chu dao cua truong |
| `wood` | `#B5804E` | `#8C5A33` | `#5E3B21` | Ban ghe giang duong, cua go, bang tin |
| `metal` | `#9FB8C4` | `#6D8A9A` | `#45606E` | Khung cua so, quat tran, lan can, cot den |
| `blue` | `#6FB4D6` | `#3A7CA5` | `#24516E` | Bang viet, bien chi dan, chi tiet nhan |

**Ba màu hệ thống**

| Tên | Mã | Vai trò |
|---|---|---|
| `outline` | `#2B2320` | Viền mọi vật thể. Nâu sẫm, không phải đen |
| `ivory` | `#FFF6E4` | Điểm sáng mạnh nhất: nắng gắt, đèn, mép kim loại |
| `shade` | `#4A3A52` | Bóng đổ trên mặt đất, phủ chế độ nhân (multiply) |

Xem mẫu: `claude/design/palette.png`

## 4. Quy ước vẽ

**Đổ bóng 3 bậc.** Mỗi bề mặt dùng đúng 3 màu cùng nhóm: `_hi` ở mặt hứng sáng, base ở mặt chính, `_sh` ở mặt khuất. Không pha màu ngoài nhóm.

**Viền chọn lọc.** Vật thể rời (bàn, cây, cột) có viền `outline`. Tile nền (sàn, cỏ) **không viền** — nếu viền hết thì map sẽ trông như lưới ô vuông.

**Chi tiết tối thiểu 2 px.** Nhỏ hơn 2 px sẽ không nhìn thấy ở tỷ lệ chơi thật. Thà bỏ còn hơn vẽ mờ.

**Chống lặp.** Mỗi tile nền cần 3–4 biến thể (thêm vết nứt, viên gạch lệch, cọng cỏ) để map rộng không bị rõ vết lặp.

## 5. Quy ước đặt tên file

```
assets/tilesets/<khu_vuc>_<loai>.png
```

Ví dụ: `san_truong_nen.png`, `giang_duong_noi_that.png`, `hanh_lang_tuong.png`

Mỗi tileset kèm 1 file `.md` cùng tên ghi chỉ số từng tile (hàng, cột, công dụng, có collision không).

## 6. Ghi chú cho Godot 4

- Import PNG: **Filter = Off**, **Mipmaps = Off**.
- Dùng `TileSetAtlasSource` với `texture_region_size = 16×16`.
- Bật **Terrain (autotile)** cho cỏ ↔ bê tông và cho tường — tiết kiệm rất nhiều công dựng map.
- Project Settings → **Stretch Mode = `viewport`**, **Aspect = `keep`** để pixel luôn vuông.

## 7. Điểm chưa chắc

- **[CẦN KIỂM TRA]** Map lấy cảm hứng từ cơ sở nào, tòa nhà nào của trường.
- **[CẦN KIỂM TRA]** Màu chủ đạo của nhân vật chính, để bảo đảm nhân vật nổi trên nền cỏ `#5FA03C` và sàn `#BCAE96`.
- Không dùng logo chính thức của trường trên bất kỳ tile nào (bản quyền). Nhận diện bằng dáng nhà, màu tường, biển chữ tự đặt.

