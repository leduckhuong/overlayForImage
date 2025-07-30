![overlayForImage](images/1.png)


**overlayForImage** là một công cụ giúp bạn dễ dàng **đề chữ lên ảnh** theo danh sách từ có sẵn trong file `.txt`. Mỗi dòng trong file sẽ tạo ra một ảnh mới với chữ tương ứng được chèn vào vị trí mong muốn.

---

## ✅ Yêu cầu

- Python 3.6+
- `Pillow` (được cài qua `requirements.txt`)
- Môi trường có hỗ trợ `tkinter` (đa phần hệ thống đều có sẵn)

---

## ⚙️ Cài đặt

### Bước 1: Tải mã nguồn từ GitHub

```bash
git clone https://github.com/leduckhuong/overlayForImage.git
````

### Bước 2: Truy cập vào thư mục

```bash
cd overlayForImage
```

### Bước 3: Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

### Bước 4: Chạy chương trình

```bash
python3 main.py
```

---

## 🚀 Hướng dẫn sử dụng

### Bước 1: Khởi động tool

```bash
python3 main.py
```

---

### Bước 2: Chọn ảnh nền

🖼️ *Mỗi từ sẽ được overlay lên ảnh này*

![overlayForImage](images/2.png)

---

### Bước 3: Chọn font chữ (`.ttf` hoặc `.otf`)

🔤 *Bạn có thể sử dụng bất kỳ font nào mà hệ thống hỗ trợ*

![overlayForImage](images/3.png)

---

### Bước 4: Chọn file `.txt`

📄 *Mỗi dòng là một dòng chữ sẽ overlay lên ảnh*

![overlayForImage](images/4.png)

---

### Bước 5: Chọn màu chữ

🎨 *Sử dụng bảng màu trực quan*

![overlayForImage](images/5.png)

---

### Bước 6: Chọn thư mục để lưu ảnh

📁 *Các ảnh sau khi overlay sẽ được lưu tại đây*

![overlayForImage](images/6.png)

---

### Bước 7: Cài đặt cỡ chữ và vị trí chữ (tọa độ dọc - y-offset)

🧮 *Căn chỉnh vị trí đề chữ trên ảnh*

![overlayForImage](images/7.png)

---

### Bước 8: Bấm `Generate Images` để bắt đầu

⚡ *Mỗi dòng chữ sẽ tạo ra một ảnh mới*

![overlayForImage](images/8.png)

---

## 📂 Output

* Ảnh đầu ra được lưu trong thư mục bạn chọn.
* Tên file sẽ được tự động đánh số tương ứng với dòng chữ trong file `.txt`.
![overlayForImage](images/9.png)
---

## 📌 Ghi chú

* Font chữ sử dụng nên hỗ trợ Unicode nếu bạn dùng tiếng Việt.
* Ảnh đầu vào hỗ trợ định dạng `.png`, `.jpg`, `.jpeg`, ...

---
