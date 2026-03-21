---
title: DR Diagnosis System
emoji: 👁️
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 👁️ DR Diagnosis System — Hệ Thống Chẩn Đoán Võng Mạc Đái Tháo Đường (DR)

<div align="center">

Hệ thống hỗ trợ chẩn đoán và **phân loại 5 mức độ bệnh võng mạc đái tháo đường (Diabetic Retinopathy — DR)** từ ảnh đáy mắt (fundus) bằng học sâu. Ứng dụng chạy **cục bộ (localhost)**, cho phép tải ảnh và nhận kết quả dự đoán kèm xác suất 5 lớp và chỉ số độ bất định.
![Python](https://img.shields.io/badge/Python-3.10%2F3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API%20%2B%20Static-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](<https://img.shields.io/badge/TensorFlow-Keras%20(.h5)-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white>)
![OpenCV](https://img.shields.io/badge/OpenCV-opencv--python--headless-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Port](https://img.shields.io/badge/Port-7860-blue?style=for-the-badge)

**Web app chạy cục bộ để phân loại mức độ bệnh võng mạc đái tháo đường từ ảnh đáy mắt (fundus),**
**trả về xác suất 5 lớp kèm chỉ số độ bất định (uncertainty) và ảnh sau xử lý CLAHE để đối chiếu.**

[🚀 Bắt đầu nhanh](#-bắt-đầu-nhanh) · [🌐 Demo online](#-demo-online-hugging-face-spaces) · [🧱 Công nghệ](#-công-nghệ-sử-dụng) · [📡 API](#-api-reference) · [☁️ Huấn luyện](#️-huấn-luyện-mô-hình)

</div>

> ⚕️ **Tuyên bố từ chối trách nhiệm**: Dự án chỉ phục vụ **học thuật / hỗ trợ tham khảo**, không thay thế chẩn đoán của bác sĩ chuyên khoa.

---

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng](#-tính-năng)
- [Kiến trúc & pipeline](#-kiến-trúc--pipeline)
- [Công nghệ sử dụng](#-công-nghệ-sử-dụng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Bắt đầu nhanh](#-bắt-đầu-nhanh)
- [Demo online (Hugging Face Spaces)](#-demo-online-hugging-face-spaces)
- [Cấu hình](#️-cấu-hình)
- [Sử dụng](#-sử-dụng)
- [API Reference](#-api-reference)
- [Huấn luyện mô hình](#️-huấn-luyện-mô-hình)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Tác giả](#-tác-giả)

---

## 🌟 Giới thiệu

**Bệnh võng mạc đái tháo đường (Diabetic Retinopathy — DR)** là biến chứng nguy hiểm của bệnh tiểu đường. Dự án này xây dựng một **ứng dụng Web chạy hoàn toàn local** để:

- Nhận ảnh đáy mắt (PNG/JPG/JPEG)
- Tiền xử lý (crop viền đen → resize 224×224 → CLAHE trên LAB)
- Chạy inference bằng **model Keras (.h5)** (pipeline hiện tại dùng chuẩn tiền xử lý của **DenseNet**)
- Trả về: lớp dự đoán 0–4, phân phối xác suất 5 lớp, entropy, và chỉ số **uncertainty = 1 − max(probabilities)**

---

## ✨ Tính năng

- 🔬 Phân loại 5 mức độ DR (0–4)
- 🖼️ Tiền xử lý ảnh: crop viền đen, resize 224×224, CLAHE (LAB)
- 📊 Trả về xác suất 5 lớp + entropy + chỉ số độ bất định
- 🌐 Giao diện Web: kéo-thả ảnh, preview, thanh xác suất, cảnh báo bất định
- 🖨️ In báo cáo trực tiếp từ trình duyệt
- 🕑 Lưu lịch sử 10 lần chẩn đoán gần nhất (localStorage)
- 🧪 Mock mode để test UI/API khi chưa có model thật

## 🏗️ Kiến trúc & pipeline

```
Ảnh đáy mắt (PNG/JPG/JPEG)
                        ↓
Frontend (HTML/CSS/JS)
                        ↓  POST /api/predict (multipart/form-data)
Backend Flask
                        ↓
Tiền xử lý (OpenCV): crop → resize 224×224 → CLAHE
                        ↓
Model Keras (.h5) inference
                        ↓
JSON: predicted_class + probabilities + uncertainty + entropy + ảnh CLAHE (base64 JPG)
```

## 🧱 Công nghệ sử dụng

Phần này được viết theo đúng code hiện có trong dự án:

### Backend (API + serve UI)

- **Python 3.10/3.11**
- **Flask**: serve `frontend/index.html` ở `/` và cung cấp API ở `/api/*`
- **Flask-CORS**: bật CORS cho `/api/*`
- **Werkzeug**: `secure_filename` cho file upload (dependency đi kèm Flask)

### AI / Deep Learning

- **TensorFlow + Keras**: load model `backend/models/dr_classifier.h5` và chạy inference
- **DenseNet preprocess_input**: dùng chuẩn tiền xử lý DenseNet cho ảnh đầu vào (trong `backend/utils/image_processing.py`)

### Xử lý ảnh

- **OpenCV (opencv-python-headless)**: đọc ảnh, crop viền đen, resize, CLAHE trên LAB
- **NumPy**: xử lý tensor và hậu xử lý output

### Frontend

- **HTML5 / CSS3 / Vanilla JavaScript**
- Fetch API gọi `/api/health` và `/api/predict`
- localStorage lưu lịch sử chẩn đoán

### Đóng gói / triển khai

- **Docker** (Dockerfile tại thư mục gốc) — cấu hình port **7860** (phù hợp Hugging Face Spaces)

## 🖥️ Yêu cầu hệ thống

- **Python 3.10 hoặc 3.11** (TensorFlow thường không hỗ trợ tốt Python 3.12+)
- Trình duyệt hiện đại: Chrome/Edge/Firefox

Khuyến nghị khi chạy inference:

- RAM 4GB+ (tùy model)
- CPU chạy được; GPU không bắt buộc khi suy luận

## 🚀 Bắt đầu nhanh

### 1) Tạo môi trường ảo và cài thư viện

```bash
python -m venv venv

# Windows
venv\Scripts\activate

pip install -r backend/requirements.txt
```

### 2) Đặt file model

Copy model đã huấn luyện vào đúng đường dẫn:

```
backend/models/dr_classifier.h5
```

Nếu chưa có model, bạn vẫn có thể bật **mock mode** để test giao diện.

### 3) Chạy server

Chạy theo 1 trong 2 cách sau:

```bash
# Cách 1: chạy từ thư mục gốc (khuyến nghị)
python -m backend.app
```

```bash
# Cách 2: chạy trong thư mục backend/
cd backend
python app.py
```

Server mặc định chạy tại:

```
http://127.0.0.1:7860
```

### 4) Mở giao diện

Truy cập:

```
http://127.0.0.1:7860/
```

### (Tuỳ chọn) Chạy bằng Docker

```bash
docker build -t dr-diagnosis-system .
docker run --rm -p 7860:7860 dr-diagnosis-system
```

## 🌐 Demo online (Hugging Face Spaces)

Bạn có thể trải nghiệm bản online tại:

https://huggingface.co/spaces/thanhnguyen-nguyen/dr-diagnosis-system

Cách dùng nhanh:

1. Mở link Spaces
2. Upload/kéo-thả ảnh đáy mắt (PNG/JPG/JPEG)
3. Chẩn đoán và xem: grade dự đoán, phân phối xác suất 5 lớp, uncertainty/entropy và ảnh sau xử lý CLAHE

Lưu ý:

- Nếu Spaces đang “sleep” thì có thể mất vài giây khi lần đầu load lại.
- Kết quả chỉ mang tính chất học thuật/tham khảo, không thay thế chẩn đoán y khoa.

## ⚙️ Cấu hình

### Biến môi trường

| Biến            | Giá trị   | Ý nghĩa                                 |
| --------------- | --------- | --------------------------------------- |
| `DR_ALLOW_MOCK` | `1` / `0` | Bật chế độ mock khi model chưa sẵn sàng |

### Bật mock mode

```bash
# Windows PowerShell
$env:DR_ALLOW_MOCK="1"
python -m backend.app
```

```bash
# Windows CMD
set DR_ALLOW_MOCK=1
python -m backend.app
```

Khi mock bật, `/api/predict` sẽ trả JSON mẫu đúng format để UI render.

## 📖 Sử dụng

1. Mở `http://127.0.0.1:7860/`
2. Kéo & thả ảnh đáy mắt (PNG/JPG/JPEG, tối đa 10MB)
3. Nhấn **Chẩn đoán ngay**
4. Xem kết quả: grade dự đoán, phân phối xác suất, thanh bất định, ảnh sau CLAHE
5. Nhấn **In báo cáo** nếu cần

## 📡 API Reference

Base URL (local):

```
http://127.0.0.1:7860
```

### `GET /`

Serve giao diện Web (`frontend/index.html`).

### `GET /api/health`

Trả trạng thái model.

**200 OK**

```json
{
  "ready": true,
  "mock_enabled": false
}
```

**503 Service Unavailable** (thiếu model / lỗi load)

```json
{
  "ready": false,
  "error": "...",
  "mock_enabled": false
}
```

### `POST /api/predict`

Upload ảnh và nhận kết quả.

**Request**: `multipart/form-data`

| Field  | Type | Mô tả                     |
| ------ | ---- | ------------------------- |
| `file` | file | PNG/JPG/JPEG, tối đa 10MB |

**Response 200 OK**

```json
{
  "predicted_class": 2,
  "diagnosis": "Mức 2 - Tiền tăng sinh nhẹ/trung bình",
  "probabilities": [0.05, 0.1, 0.6, 0.2, 0.05],
  "uncertainty": 0.4,
  "entropy": 0.0,
  "is_high_uncertainty": false,
  "processed_image_base64_jpg": "<base64>",
  "heatmap_url": ""
}
```

Ghi chú:

- `uncertainty = 1 - max(probabilities)`
- `entropy` hiện tính theo log tự nhiên (natural log)

## ☁️ Huấn luyện mô hình

Notebook huấn luyện nằm ở:

- `training/train_model_colab.ipynb`

Sau khi train xong, export model Keras `.h5` và đặt vào:

- `backend/models/dr_classifier.h5`

## 📂 Cấu trúc thư mục

```
DR_Diagnosis_System/
├── backend/                       # Backend Flask + suy luận AI
│   ├── app.py                     # Entry server: serve UI + API (/api/health, /api/predict)
│   ├── requirements.txt           # Thư viện Python cho backend
│   ├── models/                    # Nơi đặt artifact mô hình
│   │   └── dr_classifier.h5        # Model Keras đã train (bắt buộc khi chạy inference thật)
│   ├── uploads/                   # Ảnh upload tạm khi gọi /api/predict
│   └── utils/                     # Các module xử lý ảnh & inference
│       ├── image_processing.py     # Crop viền đen + resize 224 + CLAHE + DenseNet preprocess_input
│       └── ai_inference.py         # Load model + predict + trả về probabilities/uncertainty/entropy
├── frontend/                      # Giao diện web (HTML/CSS/JS)
│   ├── index.html                 # UI: upload ảnh, hiển thị kết quả, in báo cáo
│   ├── css/
│   │   └── style.css              # Style giao diện
│   └── js/
│       └── script.js              # Logic gọi API, render kết quả, lưu history localStorage
├── training/                      # Notebook/flow huấn luyện
│   └── train_model_colab.ipynb    # Notebook train (Colab/Kaggle), export .h5
└── Dockerfile                     # Docker hoá backend + frontend (port 7860)
```

Ghi chú:

- Repo có thêm thư mục `dr-diagnosis-system/` (bản copy cùng mã nguồn) phục vụ đóng gói/triển khai; phần README này mô tả theo cây thư mục `DR_Diagnosis_System/`.
- Khi chạy local, bạn chỉ cần quan tâm các thư mục: `backend/`, `frontend/`, và model `.h5` trong `backend/models/`.

## 👥 Tác giả

| Vai trò              | Thông tin                |
| -------------------- | ------------------------ |
| Sinh viên thực hiện  | Nguyễn Thành Nguyên      |
| Mã sinh viên         | 225255                   |
| Lớp                  | DH22TIN03                |
| Giảng viên hướng dẫn | Trần Văn Thiện           |
| Đơn vị               | Khoa Công Nghệ Thông Tin |
