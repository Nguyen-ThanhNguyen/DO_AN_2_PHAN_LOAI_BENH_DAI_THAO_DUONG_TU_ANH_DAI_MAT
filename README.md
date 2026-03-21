# HỆ THỐNG HỖ TRỢ CHẨN ĐOÁN VÀ PHÂN LOẠI BỆNH VÕNG MẠC ĐÁI THÁO ĐƯỜNG TỪ ẢNH ĐÁY MẮT (AI)

> **Dự án Nghiên cứu & Phát triển:** Ứng dụng mạng Nơ-ron Tích chập Sâu (DenseNet-121) kết hợp kỹ thuật sinh dữ liệu Mixup và tối ưu hóa ngưỡng phân loại để chẩn đoán 5 cấp độ bệnh võng mạc đái tháo đường trên bộ dữ liệu APTOS 2019.

![Kaggle Kernel](https://img.shields.io/badge/Platform-Kaggle%20Kernels-blue?style=for-the-badge&logo=kaggle)
![Framework](https://img.shields.io/badge/Deep%20Learning-TensorFlow%20%2F%20Keras-orange?style=for-the-badge&logo=tensorflow)
![Dataset](https://img.shields.io/badge/Dataset-APTOS%202019%20Blindness-green?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Model-DenseNet--121-red?style=for-the-badge&logo=keras)

---

## 📑 MỤC LỤC (TABLE OF CONTENTS)
1.  Báo cáo Tiến độ & Lộ trình (Progress & Roadmap)
2.  Giới thiệu & Tổng quan (Introduction)
3.  Phương pháp Nghiên cứu (Research Methodology)
4.  So sánh với các Nghiên cứu trước (Comparison)

---

## 1. BÁO CÁO TIẾN ĐỘ & LỘ TRÌNH (PROGRESS & ROADMAP)

### 🟢 Giai đoạn 1: Khám phá & Tiền xử lý dữ liệu
**Trạng thái:** ✅ Đã hoàn thành (Done)
- [x] Khám phá phân phối nhãn dữ liệu từ tập CSV của APTOS 2019.
- [x] Resize toàn bộ ảnh huấn luyện và kiểm thử về kích thước chuẩn `224x224` để phù hợp với định dạng ImageNet.
- [x] Xây dựng `Data Generator` kết hợp kỹ thuật biến đổi ảnh ngẫu nhiên (lật, xoay, thu phóng) và `Mixup` để xử lý vấn đề mất cân bằng và thiếu hụt dữ liệu (~3000 ảnh).

### 🟡 Giai đoạn 2: Xây dựng & Huấn luyện Mô hình
**Trạng thái:** ⏳ Đang thực hiện (In Progress)
- [x] Khởi tạo kiến trúc `DenseNet-121` (Pre-trained trên ImageNet).
- [x] Biên dịch mô hình với `Adam Optimizer` (Learning Rate: 0.00005) và hàm loss `Binary Crossentropy`.
- [ ] Huấn luyện mô hình trong 15 epochs.
- [ ] Tối ưu hóa ngưỡng phân loại (Best Threshold) dựa trên hệ số `Quadratic Weighted Kappa (QWK)` bằng thuật toán Nelder-Mead.

### 🔴 Giai đoạn 3: Tích hợp, Đánh giá & Hoàn thiện
**Trạng thái:** 🔴 Chưa bắt đầu (Pending)
- [ ] Đánh giá độ chính xác (Accuracy) và độ nhạy (Sensitivity) trên tập Test ẩn.
- [ ] Tích hợp mô hình vào ứng dụng trực quan, hỗ trợ chẩn đoán cho bác sĩ.
- [ ] Kiểm thử toàn diện (Debug) và xử lý lỗi phát sinh.
- [ ] Hoàn tất hồ sơ, viết báo cáo khóa luận chuẩn bị cho buổi bảo vệ.

---

## 2. GIỚI THIỆU & TỔNG QUAN (INTRODUCTION)

Bệnh đái tháo đường và các biến chứng của nó đang là thách thức lớn đối với hệ thống y tế toàn cầu. Trong đó, bệnh võng mạc đái tháo đường là nguyên nhân hàng đầu gây mù lòa và suy giảm thị lực vĩnh viễn ở người trong độ tuổi lao động. 

Tại các quốc gia đang phát triển như Việt Nam, việc thiếu hụt nhân lực y tế chuyên sâu về nhãn khoa tại các tuyến cơ sở khiến quy trình sàng lọc truyền thống (bác sĩ quan sát trực tiếp ảnh đáy mắt) gặp nhiều hạn chế. Nó không chỉ tốn thời gian mà còn phụ thuộc lớn vào kinh nghiệm chủ quan của bác sĩ, dễ làm mất "thời điểm vàng" điều trị. Dự án này được phát triển nhằm cung cấp một công cụ hỗ trợ chẩn đoán tự động bằng AI, mang lại kết quả nhanh chóng, chính xác và có khả năng triển khai rộng rãi.

---
## 3. SO SÁNH VỚI CÁC NGHIÊN CỨU TRƯỚC (COMPARISON)
Dựa trên các nghiên cứu khoa học tiên tiến được tham khảo, dưới đây là bảng so sánh phương pháp và hiệu suất của dự án đề xuất so với 2 nghiên cứu quốc tế nổi bật:
| Tiêu chí | Nghiên cứu của A. Bilal et al. (2022) | Nghiên cứu của S. Toledo-Cortés et al. (2020) | Dự án hiện tại (APTOS DenseNet-121) |
| :--- | :--- | :--- | :--- |
| **Phương pháp nghiên cứu** | Trí tuệ nhân tạo dựa trên U-Net kết hợp Deep Learning. | Học sâu lai ghép kết hợp Quá trình Gaussian (Hybrid Deep Learning Gaussian Process). | Học chuyển giao (Transfer Learning) với DenseNet-121 kết hợp Threshold Optimization. |
| **Mục tiêu chính** | Phát hiện tự động, khoanh vùng và phân loại cấp độ bệnh. | Chẩn đoán bệnh và lượng hóa độ không chắc chắn (Uncertainty Quantification). | Phân loại chính xác 5 cấp độ bệnh dựa trên việc cực đại hóa chỉ số QWK. |
| **Độ chính xác / Khả năng** | Accuracy đạt mức cao (lên tới ~97% trên một số tập dữ liệu). | Đạt chỉ số AUC tốt (~0.948) và cảnh báo rủi ro khi mô hình dự đoán không chắc chắn. | Hoạt động ổn định trên tập dữ liệu nhỏ nhờ kỹ thuật Mixup sinh dữ liệu. |
| **Độ nhạy (Sensitivity)** | Dao động rất tốt (>84%) trong việc nhận diện vi phình mạch máu. | Phụ thuộc vào ngưỡng tin cậy của Gaussian Process. | (Đang cập nhật chi tiết sau quá trình kiểm thử tập Test) |
---

## 4. PHƯƠNG PHÁP NGHIÊN CỨU (RESEARCH METHODOLOGY)

### Bước 1: Tiền xử lý và Data Generator
Giải thích: Thay đổi kích thước ảnh về chuẩn ImageNet và sử dụng Generator để tăng cường dữ liệu, kết hợp kỹ thuật Mixup giúp mô hình tổng quát hóa tốt hơn.
```python
# Cấu hình ImageDataGenerator để tăng cường dữ liệu
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    zoom_range=0.15,
    fill_mode='constant',
    cval=0.,
    horizontal_flip=True,
    vertical_flip=True,
)
```
### Bước 2: Khởi tạo mô hình DenseNet-121
Giải thích: Sử dụng phương pháp Học chuyển giao (Transfer Learning) với mạng DenseNet-121 mạnh mẽ, thiết lập đầu ra Multilabel để dự đoán 5 cấp độ của bệnh.
```python
from keras.applications import DenseNet121
from keras.models import Sequential
from keras.layers import Dense, GlobalAveragePooling2D, Dropout

# Tải mô hình Pre-trained, loại bỏ lớp phân loại trên cùng
densenet = DenseNet121(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

model = Sequential()
model.add(densenet)
model.add(GlobalAveragePooling2D())
model.add(Dropout(0.5))
model.add(Dense(5, activation='sigmoid')) # Đầu ra Multilabel cho 5 cấp độ bệnh
```
### Bước 3: Tối ưu hóa ngưỡng bằng Quadratic Weighted Kappa (QWK)
Giải thích: Thay vì dùng ngưỡng cắt 0.5 mặc định, dự án sử dụng thuật toán Nelder-Mead của scipy.optimize để tìm ngưỡng cắt (threshold) tối ưu, giúp cực đại hóa chỉ số QWK - thước đo chính của bài toán.
```python
import scipy.optimize
from sklearn.metrics import cohen_kappa_score

def compute_score_inv(threshold):
    y1 = y_val_pred > threshold
    y1 = y1.astype(int).sum(axis=1) - 1
    y2 = y_val.sum(axis=1) - 1
    score = cohen_kappa_score(y1, y2, weights='quadratic')
    return 1 - score

# Tìm ngưỡng tối ưu
simplex = scipy.optimize.minimize(
    compute_score_inv, 0.5, method='nelder-mead'
)
best_threshold = simplex['x'][0]
print(f"✅ Ngưỡng tối ưu hóa QWK: {best_threshold}")
```
