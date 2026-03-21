# BÁO CÁO ĐỀ CƯƠNG / THUYẾT MINH ĐỀ TÀI

**Trường/Khoa:** [Điền thông tin]  
**Học phần/Đồ án:** [Điền thông tin]  
**Sinh viên thực hiện:** [Họ tên – MSSV]  
**Giảng viên hướng dẫn:** [Họ tên GVHD]  
**Thời gian thực hiện:** [mm/yyyy – mm/yyyy]  
**Phiên bản báo cáo:** v1.0 — [ngày/tháng/năm]

---

## 1. Tên đề tài

**Hệ thống hỗ trợ chẩn đoán và phân loại bệnh võng mạc đái tháo đường từ ảnh đáy mắt ứng dụng học sâu (Deep Learning).**

(Tên tiếng Anh – tùy chọn): **Diabetic Retinopathy Diagnosis and Grading System from Fundus Images using Deep Learning.**

---

## 2. Đặt vấn đề

### 2.1. Tính cấp thiết

Bệnh võng mạc đái tháo đường (Diabetic Retinopathy – DR) là một biến chứng nguy hiểm của bệnh đái tháo đường, có thể dẫn đến suy giảm thị lực và mù lòa nếu không được phát hiện sớm. Trong thực tế, việc sàng lọc DR dựa trên ảnh đáy mắt thường cần bác sĩ chuyên khoa mắt hoặc kỹ thuật viên được đào tạo, tốn thời gian và phụ thuộc nhiều vào kinh nghiệm người đọc ảnh.

Trong bối cảnh số lượng bệnh nhân đái tháo đường ngày càng tăng, nhu cầu sàng lọc diện rộng cũng tăng theo. Do đó, việc xây dựng một hệ thống hỗ trợ tự động phân loại mức độ DR từ ảnh đáy mắt có ý nghĩa thiết thực:

- Giảm tải cho nhân lực y tế trong khâu sàng lọc ban đầu.
- Hỗ trợ phát hiện sớm và phân luồng bệnh nhân (ưu tiên ca nặng).
- Tăng tính nhất quán khi đánh giá ảnh, hạn chế sai khác giữa người chấm.

### 2.2. Mục tiêu nghiên cứu

**Mục tiêu tổng quát:**  
Xây dựng hệ thống ứng dụng học sâu để **phân loại 5 mức độ DR** từ ảnh đáy mắt và cung cấp kết quả dưới dạng giao diện web thân thiện, chạy cục bộ.

**Mục tiêu cụ thể:**

1. Khảo sát dữ liệu và xây dựng quy trình tiền xử lý ảnh đáy mắt (cắt viền đen, chuẩn hóa kích thước, tăng cường tương phản).
2. Xây dựng và huấn luyện mô hình học sâu (ưu tiên học chuyển giao) cho bài toán phân loại 5 lớp.
3. Xây dựng API backend nhận ảnh, thực hiện suy luận (inference), trả kết quả dự đoán và xác suất từng lớp.
4. Xây dựng giao diện web cho phép tải ảnh, hiển thị kết quả phân loại và biểu đồ xác suất.
5. Đánh giá hiệu năng mô hình và hệ thống theo các chỉ số phù hợp; phân tích lỗi và giới hạn.

### 2.3. Đối tượng và phạm vi nghiên cứu

**Đối tượng nghiên cứu:**

- Bài toán phân loại mức độ bệnh DR từ **ảnh đáy mắt màu (fundus images)**.
- Thuật toán/mô hình học sâu (CNN), đặc biệt là DenseNet/Transfer Learning.
- Quy trình tiền xử lý ảnh: cắt vùng quan tâm, cân bằng tương phản (CLAHE), chuẩn hóa đầu vào.

**Phạm vi ứng dụng:**

- Hệ thống chạy cục bộ (localhost), phục vụ mục đích học tập và nghiên cứu.
- Kết quả mang tính hỗ trợ tham khảo; **không thay thế chẩn đoán lâm sàng**.
- Dữ liệu huấn luyện/đánh giá: ưu tiên bộ dữ liệu công khai (ví dụ APTOS 2019).  
  (Tùy điều kiện, có thể mở rộng thêm các dataset như EyePACS/Messidor nếu đáp ứng được quyền truy cập.)

### 2.4. Phương pháp nghiên cứu

- **Thu thập tài liệu:** tổng hợp bài báo, báo cáo, tài liệu kỹ thuật liên quan đến DR grading và học chuyển giao.
- **Phân tích dữ liệu:** khảo sát phân bố nhãn, chất lượng ảnh, mất cân bằng lớp; lựa chọn chiến lược tiền xử lý/augmentation.
- **Thiết kế – triển khai hệ thống:** mô hình client–server đơn giản (frontend web + backend API).
- **Thử nghiệm – đánh giá:** chia tập train/val/test; đánh giá theo accuracy, precision/recall/F1, AUC (one-vs-rest), confusion matrix, và đặc biệt là QWK (Quadratic Weighted Kappa) cho bài toán phân loại theo mức độ.
- **Phân tích kết quả:** phân tích các trường hợp phân loại sai, ảnh chất lượng kém; đánh giá tính phù hợp khi triển khai.

### 2.5. Ý nghĩa khoa học và thực tiễn

**Ý nghĩa khoa học:**

- Củng cố kiến thức về CNN, DenseNet, học chuyển giao và tối ưu mô hình cho dữ liệu y tế.
- Hệ thống hóa quy trình tiền xử lý ảnh đáy mắt và đánh giá mô hình theo các chỉ số phù hợp bài toán phân loại theo cấp độ.

**Ý nghĩa thực tiễn:**

- Tạo nguyên mẫu (prototype) hệ thống hỗ trợ sàng lọc DR, giúp người dùng tải ảnh và nhận kết quả nhanh.
- Đề xuất hướng tích hợp cơ chế “độ bất định” (uncertainty) để cảnh báo khi mô hình kém chắc chắn, giảm rủi ro tin tưởng mù quáng vào AI.

**Tuyên bố sử dụng (khuyến nghị đưa vào báo cáo):**
Hệ thống chỉ hỗ trợ tham khảo; mọi quyết định y khoa cần được thực hiện bởi bác sĩ có chuyên môn.

---

## 3. Tổng quan cơ sở lý thuyết

### 3.1. Nghiên cứu tổng quan (các công trình liên quan trong 5 năm gần đây)

Trong 5 năm gần đây, các hướng nghiên cứu nổi bật cho bài toán DR grading gồm:

- Mạng CNN hiện đại và học chuyển giao (EfficientNet, DenseNet, ResNet, ConvNeXt).
- Tối ưu cho dữ liệu mất cân bằng lớp (class weight, focal loss, oversampling).
- Kỹ thuật tăng cường dữ liệu (augmentation), cân bằng màu/ánh sáng, crop vùng fundus.
- Học biểu diễn và mô hình lai (CNN + Attention/Transformer).
- Đánh giá theo chỉ số phù hợp phân loại theo cấp độ: QWK, macro-F1, AUC đa lớp.

**Bảng tóm tắt công trình liên quan (bạn điền thông tin bài báo thật để đúng chuẩn trích dẫn):**

| STT | Năm  | Tác giả/nhóm | Phương pháp            | Dataset | Kết quả chính | Nhận xét |
| --- | ---- | ------------ | ---------------------- | ------- | ------------- | -------- |
| [1] | 2021 | [...]        | CNN/Transfer Learning  | [...]   | [...]         | [...]    |
| [2] | 2022 | [...]        | EfficientNet/Attention | [...]   | [...]         | [...]    |
| [3] | 2023 | [...]        | Ensemble / Calibration | [...]   | [...]         | [...]    |
| [4] | 2024 | [...]        | Transformer-based      | [...]   | [...]         | [...]    |
| [5] | 2025 | [...]        | Multitask / Ordinal    | [...]   | [...]         | [...]    |

**Gợi ý từ khóa để tìm bài (IEEE Xplore / PubMed / arXiv):**
“diabetic retinopathy grading 2021”, “fundus image classification uncertainty”, “quadratic weighted kappa DR”, “EfficientNet diabetic retinopathy”, “ordinal classification diabetic retinopathy”.

### 3.2. Phân tích hệ thống hiện có (điểm mạnh/yếu của các giải pháp tương tự)

**Một số dạng hệ thống/giải pháp phổ biến:**

- Công cụ hỗ trợ sàng lọc DR dựa trên mô hình học sâu (AI screening).
- Hệ thống chẩn đoán tích hợp bệnh viện hoặc nền tảng cloud.

**Điểm mạnh:**

- Tốc độ xử lý nhanh, có thể sàng lọc số lượng lớn.
- Độ chính xác cao nếu dữ liệu huấn luyện lớn và đa dạng.
- Có khả năng hỗ trợ phân luồng, giảm tải cho bác sĩ.

**Điểm yếu / thách thức:**

- Dữ liệu ảnh y tế nhạy cảm → yêu cầu cao về bảo mật và quyền riêng tư.
- Khác biệt thiết bị chụp, ánh sáng, chất lượng ảnh gây “domain shift”.
- Mất cân bằng lớp (thường nhiều ảnh mức 0–1 hơn mức 3–4).
- Thiếu khả năng giải thích, khó biết khi nào mô hình sai → cần cơ chế cảnh báo (uncertainty).

### 3.3. Cơ sở lý thuyết

**(1) Ảnh đáy mắt và phân loại DR 5 mức**

- Mức 0: Không bệnh
- Mức 1: Nhẹ
- Mức 2: Tiền tăng sinh nhẹ/trung bình
- Mức 3: Nặng
- Mức 4: Tăng sinh

**(2) Mạng nơ-ron tích chập (CNN) và học chuyển giao**

- CNN học đặc trưng hình ảnh qua các lớp convolution/pooling.
- Học chuyển giao: sử dụng mô hình pretrained (ImageNet), tinh chỉnh (fine-tune) cho bài toán DR để giảm thời gian huấn luyện và cải thiện hiệu năng khi dữ liệu hạn chế.

**(3) DenseNet-121 (tóm tắt)**

- DenseNet kết nối dày đặc (dense connections), giúp lan truyền gradient tốt hơn, giảm mất mát thông tin đặc trưng, phù hợp bài toán thị giác y tế.

**(4) Tiền xử lý ảnh**

- Cắt viền đen quanh vùng fundus để giảm nhiễu nền.
- Chuẩn hóa kích thước về 224×224 để tương thích đầu vào mạng.
- CLAHE (Contrast Limited Adaptive Histogram Equalization) trong không gian LAB để tăng tương phản cục bộ, giúp nổi bật chi tiết tổn thương vi mô.

**(5) Đo độ bất định (uncertainty) ở mức đơn giản**

- Từ phân phối xác suất softmax, có thể lấy:
  - `uncertainty = 1 - max(p)`
  - entropy Shannon để đo mức “phân tán” của xác suất.
- Ý nghĩa: nếu uncertainty cao, kết quả kém chắc chắn → cần bác sĩ xem lại.

**(6) Chỉ số đánh giá**

- Accuracy (tham khảo) nhưng có thể đánh lừa khi mất cân bằng lớp.
- Macro Precision/Recall/F1 để phản ánh hiệu năng đều các lớp.
- Confusion matrix để xem nhầm lẫn giữa các mức độ.
- QWK (Quadratic Weighted Kappa): phù hợp vì nhãn có thứ tự (0 gần 1 hơn 4).
- AUC one-vs-rest cho từng lớp (tùy chọn).

### 3.4. Công nghệ đã sử dụng

- Ngôn ngữ: Python (backend), HTML/CSS/JavaScript (frontend).
- Framework/backend: Flask, Flask-CORS (xây dựng REST API).
- AI/Deep Learning: TensorFlow/Keras (load và suy luận mô hình).
- Xử lý ảnh: OpenCV, NumPy (crop, resize, CLAHE).
- Môi trường huấn luyện: Notebook (Kaggle/Colab).
- Đóng gói triển khai (tùy chọn): Docker.

---

## 4. Nội dung và phương pháp thực hiện

### 4.1. Nội dung tổng quát

Xây dựng một hệ thống gồm 3 khối chính:

1. **Khối dữ liệu & tiền xử lý:** chuẩn hóa ảnh đầu vào phục vụ huấn luyện và suy luận.
2. **Khối mô hình AI:** mô hình DenseNet-121 phân loại 5 mức độ DR.
3. **Khối ứng dụng web:** backend API nhận ảnh và trả kết quả; frontend hiển thị kết quả cho người dùng.

### 4.2. Nội dung chi tiết

**(1) Chuẩn bị dữ liệu**

- Lựa chọn dataset công khai (ví dụ APTOS 2019).
- Làm sạch dữ liệu: kiểm tra ảnh lỗi/thiếu, kiểm tra nhãn.
- Chia dữ liệu: train/validation/test theo tỉ lệ phù hợp (ví dụ 70/15/15), ưu tiên chia có stratify theo nhãn.

**(2) Tiền xử lý và tăng cường dữ liệu**

- Crop viền đen.
- Resize 224×224.
- CLAHE để tăng tương phản.
- Augmentation nhẹ: lật (flip), xoay góc nhỏ, thay đổi sáng/tương phản.
- Giải quyết mất cân bằng lớp: class weight hoặc sampling.

**(3) Xây dựng mô hình và huấn luyện**

- Mô hình nền: DenseNet-121 pretrained ImageNet.
- Thay thế “head” phân loại phù hợp 5 lớp (softmax).
- Huấn luyện theo 2 giai đoạn:
  - Giai đoạn 1: freeze backbone, train head.
  - Giai đoạn 2: fine-tune một phần backbone với learning rate nhỏ.
- Dùng early stopping, reduce LR để tránh overfitting.
- Lưu mô hình tốt nhất theo QWK hoặc theo val_loss.

**(4) Xây dựng backend và API**

- API kiểm tra trạng thái mô hình (health check).
- API dự đoán: nhận ảnh (multipart/form-data), tiền xử lý, suy luận, trả JSON gồm:
  - lớp dự đoán (0–4), nhãn diễn giải,
  - xác suất từng lớp,
  - độ bất định (uncertainty/entropy),
  - (tùy chọn) ảnh đã xử lý (để hiển thị).

**(5) Xây dựng frontend**

- Chức năng tải ảnh kéo-thả, preview ảnh.
- Nút chẩn đoán gọi API.
- Hiển thị: mức độ DR, biểu đồ xác suất, cảnh báo nếu độ bất định cao.
- (Tùy chọn) lưu lịch sử chẩn đoán cục bộ.

**(6) Kiểm thử và đánh giá**

- Kiểm thử chức năng API (đúng định dạng, lỗi thiếu ảnh, sai định dạng ảnh).
- Đánh giá mô hình trên tập test theo các chỉ số đã chọn.
- Phân tích lỗi: lớp nào dễ nhầm, trường hợp ảnh mờ/thiếu sáng.

### 4.3. Phương pháp thực hiện

- Phương pháp phát triển: kết hợp SDLC (phân tích–thiết kế–cài đặt–kiểm thử) với quy trình thực nghiệm ML (data → model → evaluation → iteration).
- Nguyên tắc triển khai:
  - Ưu tiên chạy cục bộ để đảm bảo dữ liệu không rời khỏi máy.
  - Thiết kế API đơn giản, rõ ràng, dễ mở rộng.
  - Lưu vết thí nghiệm huấn luyện (tham số, kết quả) để tái lập.

---

## 5. Kết quả dự kiến và đánh giá

### 5.1. Sản phẩm

- Mô hình đã huấn luyện cho bài toán phân loại 5 mức DR (file mô hình).
- Ứng dụng web chạy cục bộ:
  - Backend API phục vụ suy luận.
  - Frontend giao diện người dùng.
- Báo cáo:
  - mô tả dữ liệu, phương pháp,
  - kết quả đánh giá (bảng số liệu + hình: confusion matrix, ROC/PR nếu có),
  - phân tích lỗi và thảo luận.
- Mã nguồn và tài liệu hướng dẫn chạy.

### 5.2. Đánh giá kết quả

**So sánh với mục tiêu ban đầu:**

- Có phân loại đúng 5 mức độ DR.
- Có giao diện web và API hoạt động ổn định.
- Có minh bạch xác suất từng lớp và cảnh báo bất định.

**Chỉ số đo lường đề xuất:**

- Macro F1, macro recall (ưu tiên vì mất cân bằng lớp).
- QWK (ưu tiên vì nhãn có thứ tự).
- Confusion matrix chuẩn hóa theo hàng (tỷ lệ đúng/sai từng lớp).
- Thời gian suy luận trung bình/ảnh (ms hoặc s) trên CPU.

**Tiêu chí chấp nhận (đề xuất, bạn có thể chỉnh):**

- QWK trên tập test đạt ≥ [điền mục tiêu, ví dụ 0.70] hoặc cải thiện rõ so với baseline.
- Thời gian xử lý 1 ảnh ≤ [ví dụ 3–5 giây] trên máy cấu hình trung bình.
- Hệ thống xử lý đúng các trường hợp lỗi đầu vào (thiếu file, sai định dạng, ảnh lỗi).

**Giới hạn và rủi ro (nên nêu trong báo cáo):**

- Dataset công khai không đại diện hoàn toàn cho dữ liệu bệnh viện thực tế.
- Chưa có kiểm chứng lâm sàng; AI có thể sai trong trường hợp ảnh chất lượng kém.
- Domain shift do khác thiết bị chụp, góc chụp, ánh sáng.

---

## 6. Kế hoạch thực hiện (Gantt Chart)

> Bạn có thể điều chỉnh theo lịch học thực tế (ví dụ 8–12 tuần).

| Giai đoạn | Công việc                                              | Sản phẩm đầu ra                        | Thời gian dự kiến |
| --------- | ------------------------------------------------------ | -------------------------------------- | ----------------- |
| 1         | Khảo sát tài liệu, xác định yêu cầu, chọn dataset      | Đề cương + danh mục tài liệu           | Tuần 1            |
| 2         | Khảo sát dữ liệu, tiền xử lý cơ bản                    | Pipeline tiền xử lý + thống kê dữ liệu | Tuần 2–3          |
| 3         | Xây dựng baseline model + thử nghiệm                   | Baseline + kết quả ban đầu             | Tuần 4            |
| 4         | Tối ưu mô hình (fine-tune, augmentation, class weight) | Model tốt hơn + log thí nghiệm         | Tuần 5–6          |
| 5         | Xây dựng backend API suy luận                          | API predict/health hoạt động           | Tuần 7            |
| 6         | Xây dựng frontend hiển thị kết quả                     | UI tải ảnh + hiển thị kết quả          | Tuần 8            |
| 7         | Tích hợp hệ thống, kiểm thử end-to-end                 | Bản demo chạy ổn định                  | Tuần 9            |
| 8         | Đánh giá, phân tích lỗi, hoàn thiện báo cáo            | Bảng/hình kết quả + báo cáo            | Tuần 10–11        |
| 9         | Hoàn thiện, đóng gói, chuẩn bị bảo vệ                  | Final demo + slide                     | Tuần 12           |

**Phân công công việc:**

- [Bạn] – Dữ liệu, mô hình, backend, báo cáo.
- [Nếu có nhóm] – Frontend, test, tài liệu hóa, slide.

---

## 7. Tài liệu tham khảo (chuẩn IEEE)

> Lưu ý: Mục “công trình liên quan 5 năm” ở phần 3.1 cần bạn điền bài báo thật (tác giả/năm/tạp chí/DOI). Dưới đây là khung IEEE + vài nguồn kỹ thuật có thể trích.

[1] [Tác giả], “Tên bài báo,” _Tên tạp chí/hội nghị_, vol. x, no. y, pp. xx–xx, năm, doi: ...

[2] [Tác giả], “Tên bài báo,” _Proceedings of ..._, năm, pp. xx–xx.

[3] APTOS 2019 Blindness Detection (Kaggle Competition), [Online]. Available: https://www.kaggle.com/c/aptos2019-blindness-detection. Accessed: 2026-03-17.

[4] TensorFlow, “TensorFlow Documentation,” [Online]. Available: https://www.tensorflow.org/. Accessed: 2026-03-17.

[5] Flask, “Flask Documentation,” [Online]. Available: https://flask.palletsprojects.com/. Accessed: 2026-03-17.

[6] OpenCV, “OpenCV Documentation,” [Online]. Available: https://docs.opencv.org/. Accessed: 2026-03-17.

---

## Phụ lục (tùy chọn, nếu giáo viên yêu cầu)

- Mô tả API (request/response).
- Hình minh họa kiến trúc hệ thống.
- Bảng tham số huấn luyện (epochs, learning rate, batch size).
- Một số ví dụ đúng/sai để phân tích lỗi.
