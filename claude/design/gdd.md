# GDD 1 trang — bản nháp M0

> Trạng thái: **chờ duyệt** · Tên game: *chưa đặt*
> Thể loại: 2D pixel top-down · sim-life · giải đố Vật lý + môi trường
> Engine: Godot 4 (GDScript) · Nền tảng: PC trước

## 1. Một câu mô tả

Sống một học kỳ ở Bách Khoa: ban ngày lo ăn – học – ngủ, và mở dần khuôn viên bằng cách giải các câu đố **vận hành theo định luật vật lý thật**.

## 2. Ba trụ cột

1. **Vật lý là cơ chế, không phải câu trắc nghiệm.** Người chơi lắp, đẩy, nối, xoay vật thể; đúng hay sai do mô phỏng quyết định, không phải do gõ đáp số.
2. **Thời gian là tài nguyên.** Mỗi ngày có số giờ giới hạn; học, ăn, ngủ, giải đố đều tốn giờ.
3. **Khuôn viên ấm và sống.** Tông nắng Việt Nam, NPC có lịch sinh hoạt riêng.

## 3. Vòng lặp chơi

| Vòng | Thời lượng | Nội dung |
|---|---|---|
| Ngắn | 1–3 phút | Đi lại → tương tác → làm 1 bước của câu đố |
| Ngày | 10–15 phút | Sáng lên lớp → chiều tự do (giải đố, gặp NPC) → tối về trọ, ngủ, lưu game |
| Học kỳ | nhiều ngày | Mỗi tuần mở 1 khu mới + 1 chủ đề vật lý; cuối kỳ là câu đố tổng hợp |

## 4. Sim-life tối thiểu

Ba chỉ số, không hơn:

| Chỉ số | Tăng khi | Giảm khi | Hết thì |
|---|---|---|---|
| Năng lượng | Ăn, ngủ | Đi lại, giải đố | Ngất, mất nửa ngày |
| Tiền | Nhận trợ cấp tuần | Ăn, mua dụng cụ | Không mua được đồ ăn |
| Kiến thức | Lên lớp, giải đố | — | Không mở được đố khó hơn |

## 5. Hệ giải đố

Nền là đố lưới 16×16 (đẩy vật, công tắc, cửa). Mỗi chủ đề thêm một lớp định luật thật.

| Chủ đề | Cơ chế trên lưới | Định luật |
|---|---|---|
| **Điện** *(làm trước)* | Đặt điện trở, nối dây để dòng điện đạt ngưỡng mở khóa | Định luật Ôm; nối tiếp, song song |
| Quang | Xoay gương dẫn tia sáng tới cảm biến | Phản xạ: góc tới = góc phản xạ |
| Cơ | Đẩy thùng trên các loại sàn khác nhau | Ma sát nghỉ: đẩy được khi F > μ·m·g |

**Câu đố mẫu (Điện).** Nguồn 12 V, khóa từ mở khi I = 2 A. Cần R = U/I = 12/2 = **6 Ω**. Trong phòng có điện trở 4 Ω, 2 Ω, 12 Ω, 12 Ω. Hai lời giải đúng:
- Nối tiếp 4 Ω + 2 Ω = 6 Ω
- Song song 12 Ω ∥ 12 Ω: 1/R = 1/12 + 1/12 → R = 6 Ω

**Câu đố mẫu (Cơ).** Thùng m = 50 kg, sàn μ = 0,4, g = 9,8 m/s². Lực ma sát nghỉ cực đại = 0,4 × 50 × 9,8 = **196 N**. Nhân vật đẩy tối đa 150 N → không đẩy được. Đổ nước xà phòng, μ còn 0,2 → 98 N → đẩy được.

> **[CẦN KIỂM TRA]** Các công thức trên là dạng chuẩn, số liệu chỉ minh họa. Chưa đối chiếu với bài giảng và sách bài tập gốc của bạn (ký hiệu, giá trị g, cách làm tròn). Cần đối chiếu trước khi đưa vào game.

## 6. Phạm vi bản chơi thử (~10 phút)

- 3 khu: phòng trọ, sân trường, phòng thí nghiệm điện
- 1 ngày trong game, 1 NPC có hội thoại
- 3 câu đố Điện tăng dần: 1 điện trở → nối tiếp → song song
- 3 chỉ số chạy thật, lưu/tải được

## 7. Không làm trong bản chơi thử

Chiến đấu · nhiều học kỳ · quan hệ tình cảm NPC · làm thêm · bản điện thoại · đố Quang và Cơ (để sau khi hệ Điện ổn).

## 8. Kỹ thuật

| Mục | Giá trị |
|---|---|
| Độ phân giải gốc | 640×360 (40 × 22,5 tile), phóng to bội số nguyên |
| Tile / nhân vật | 16×16 / 32×32 |
| Điều khiển | WASD hoặc phím mũi tên di chuyển, E tương tác, Esc mở menu |
| Lưu game | 1 file JSON trong `user://` |

## 9. Điểm còn treo

- Tên game và nhân vật chính (game mới nên không dùng story bible cũ).
- **[CẦN KIỂM TRA]** Phiên bản Godot 4.x bạn cài trên máy.
- **[CẦN KIỂM TRA]** Khuôn viên dựa trên cơ sở, tòa nhà nào.
- Không dùng logo chính thức của trường (bản quyền).
