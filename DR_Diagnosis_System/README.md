Chào bạn, tôi đã đọc kỹ file `README.md` mẫu từ repo **ExpenseManagement** mà bạn cung cấp. Đó là một mẫu rất chuyên nghiệp, sử dụng Markdown tốt, có Badge đẹp và cấu trúc rõ ràng.

Dưới đây là phiên bản `README.md` được tôi viết lại hoàn toàn cho dự án **"Phân loại bệnh võng mạc đái tháo đường"** của bạn, giữ nguyên phong cách (style), cấu trúc và độ chuyên nghiệp của file mẫu, nhưng thay thế bằng nội dung kỹ thuật (CNN-SVD-GP, Flask, HTML/JS) của dự án bạn.

Bạn hãy copy toàn bộ nội dung trong khung code bên dưới và lưu vào file `README.md` nhé.

---

````markdown
# 👁️ Hệ Thống Chẩn Đoán Bệnh Võng Mạc Đái Tháo Đường (DR Diagnosis System)

> Ứng dụng hỗ trợ chẩn đoán y tế tự động sử dụng kiến trúc Học sâu lai ghép (Hybrid Deep Learning), tích hợp cảnh báo độ bất định (Uncertainty) và giao diện Web trực quan.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📖 Mục Lục

- [Giới Thiệu Đồ Án](#-giới-thiệu-đồ-án)
- [Tính Năng Chính](#-tính-năng-chính)
- [Kiến Trúc Hệ Thống](#-kiến-trúc-hệ-thống)
- [Công Nghệ Sử Dụng](#-công-nghệ-sử-dụng)
- [Cài Đặt & Hướng Dẫn](#-cài-đặt--hướng-dẫn)
- [Cấu Trúc Thư Mục](#-cấu-trúc-thư-mục)
- [Tác Giả & Liên Hệ](#-tác-giả--liên-hệ)

---

## 📖 Giới Thiệu Đồ Án

Bệnh võng mạc đái tháo đường (Diabetic Retinopathy - DR) là nguyên nhân hàng đầu gây mù lòa hiện nay. Việc sàng lọc thủ công tốn nhiều thời gian và phụ thuộc vào kinh nghiệm bác sĩ.

Dự án này xây dựng một hệ thống **Web Application (Localhost)** giúp tự động phân loại mức độ bệnh từ ảnh đáy mắt. Điểm đột phá của dự án là việc áp dụng mô hình **Hybrid (CNN + SVD + Gaussian Process)**, không chỉ đưa ra kết quả chẩn đoán mà còn **định lượng độ tin cậy**, giúp giảm thiểu sai sót y khoa.

---

## 🌟 Tính Năng Chính

✅ **Chẩn đoán đa cấp độ:** Phân loại chính xác 5 mức độ bệnh theo chuẩn ICO (0: Không bệnh ➝ 4: Tăng sinh).  
✅ **Cảnh báo độ bất định (Uncertainty-Aware):** Hệ thống tự động cảnh báo khi ảnh đầu vào bị mờ, nhiễu hoặc lạ, giúp bác sĩ không bị phụ thuộc sai vào AI.  
✅ **Xử lý ảnh nâng cao (CLAHE):** Tự động cân bằng sáng cục bộ để làm rõ các vi tổn thương nhỏ nhất.  
✅ **Giao diện Web thân thiện:** Tách biệt Frontend (HTML/JS) và Backend, dễ dàng sử dụng trên trình duyệt.  
✅ **Bảo mật dữ liệu (Offline Mode):** Hoạt động hoàn toàn trên máy cục bộ, không gửi dữ liệu bệnh nhân lên Cloud.

---

## 🏗️ Kiến Trúc Hệ Thống

Hệ thống hoạt động theo quy trình Pipeline khép kín:

```mermaid
graph LR
    User[Người dùng] -->|Upload Ảnh| FE[Frontend HTML/JS]
    FE -->|API Request| BE[Backend Flask]
    BE -->|Tiền xử lý| P[CLAHE & Resize]
    P -->|Trích xuất đặc trưng| CNN[CNN (InceptionV3)]
    CNN -->|Giảm chiều| SVD[SVD Decomposition]
    SVD -->|Phân loại| GP{Gaussian Process}
    GP -->|Kết quả + Độ bất định| FE
```
````

### Quy trình xử lý chi tiết:

1. **Input:** Ảnh đáy mắt thô từ người dùng.
2. **Preprocessing:** Cắt vùng quan tâm (ROI) và cân bằng sáng CLAHE.
3. **Core AI:** Vector đặc trưng từ CNN (2048 chiều) được nén qua SVD (50 chiều) và phân loại bởi Gaussian Process.
4. **Output:** Kết quả chẩn đoán và biểu đồ độ tin cậy hiển thị lên Web.

---

## 💻 Công Nghệ Sử Dụng

| Lĩnh vực        | Công nghệ | Mô tả                                      |
| --------------- | --------- | ------------------------------------------ |
| **Frontend**    |           | Giao diện người dùng, xử lý logic hiển thị |
| **Backend API** |           | Xử lý logic nghiệp vụ, API Endpoints       |
| **AI & ML**     |           | Xây dựng và chạy mô hình Hybrid            |
| **Image Proc**  |           | Xử lý ảnh số, thuật toán CLAHE             |

---

## 🚀 Cài Đặt & Hướng Dẫn

Dự án được thiết kế để chạy cục bộ (Localhost). Hãy làm theo các bước sau:

### 1. Clone dự án & Chuẩn bị môi trường

```bash
git clone [https://github.com/username/project-name.git](https://github.com/username/project-name.git)
cd project-name/backend

```

### 2. Cài đặt thư viện (Backend)

Yêu cầu Python 3.8 trở lên. Khuyên dùng môi trường ảo (Virtual Environment).

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường (Windows)
venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt

```

### 3. Khởi chạy Server

```bash
# Tại thư mục backend
python app.py

```

_Server sẽ khởi động tại: `http://127.0.0.1:5000_`

### 4. Sử dụng (Frontend)

- Truy cập thư mục `frontend`.
- Mở file `index.html` bằng trình duyệt (Chrome/Edge).
- Tải ảnh lên và xem kết quả chẩn đoán.

---

## ☁️ Huấn luyện Mô hình (Training)

Máy tính cá nhân thường không đủ mạnh để train mô hình Deep Learning. Bạn nên sử dụng các nền tảng miễn phí GPU mạnh mẽ sau:

### 1. Kaggle Kernels (Khuyên dùng 🏆)

Vì dataset **APTOS 2019** đã có sẵn trên Kaggle, đây là lựa chọn tốt nhất.

1. Tạo Notebook mới trên Kaggle.
2. Chọn **File -> Import Notebook** và upload file `training/train_model_colab.ipynb` của dự án này lên.
3. Ở cột phải, mục **Accelerator**, chọn **GPU P100** (hoặc T4).
4. Ở mục **Data**, nhấn **Add Data**, tìm kiếm "APTOS 2019 Blindness Detection" và thêm vào.
5. Đường dẫn dữ liệu sẽ tự động khớp với code trong notebook (`../input/aptos2019-blindness-detection`).
6. Chạy và tải file model về.

### 2. Google Colab

1. Upload file `training/train_model_colab.ipynb` lên Google Drive.
2. Mở bằng Google Colab.
3. Chọn **Runtime -> Change runtime type -> T4 GPU**.
4. Bạn sẽ cần tải dataset về máy rồi upload lên Colab (khá tốn thời gian vì dataset nặng >9GB), hoặc mount Google Drive.

---

## 📂 Cấu Trúc Thư Mục

```bash
DR-Diagnosis-System/
├── backend/                  # Xử lý Logic & AI (Python)
│   ├── app.py                # Server Flask chính
│   ├── models/               # Chứa file model (.h5, .pkl)
│   ├── utils/                # Hàm xử lý ảnh (CLAHE, Resize)
│   └── requirements.txt      # Danh sách thư viện
│
├── frontend/                 # Giao diện người dùng (Web)
│   ├── index.html            # Trang chủ
│   ├── css/                  # Stylesheet
│   └── js/                   # Script gọi API
│
├── dataset/                  # (Optional) Thư mục dữ liệu mẫu
└── README.md                 # Tài liệu dự án

```

---

## 📊 Dữ Liệu Huấn Luyện

Dự án sử dụng các bộ dữ liệu chuẩn y khoa quốc tế:

- **APTOS 2019:** Dùng cho quá trình huấn luyện (Training) và tinh chỉnh tham số.
- **Messidor:** Dùng cho quá trình kiểm thử độc lập (External Validation).

---

## 👥 Tác Giả & Liên Hệ

Dự án được thực hiện bởi:

- **Sinh viên:** Nguyễn Thành Nguyên - DH22TIN03 - 225255
- **GVHD:** Trần Văn Thiện
- **Đơn vị:** Khoa CNTT

---

## 📜 License

```

```
