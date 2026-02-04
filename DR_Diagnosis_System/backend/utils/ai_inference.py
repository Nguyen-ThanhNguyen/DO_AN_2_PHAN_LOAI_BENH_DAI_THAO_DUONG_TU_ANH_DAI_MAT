"""AI inference pipeline.

File này là khung (scaffold) cho pipeline:
CNN feature extractor -> SVD reducer -> Gaussian Process classifier.

Hiện tại `predict()` trả về kết quả giả lập để bạn test end-to-end.
Khi có model thật, bạn thay phần thân của `predict()` và/hoặc bổ sung load model.
"""

from __future__ import annotations

import numpy as np


def predict(processed_img: np.ndarray) -> dict:
    """Nhận ảnh đã tiền xử lý (numpy array) và trả về kết quả dự đoán.

    processed_img: ảnh BGR/RGB sau CLAHE/resize... tuỳ pipeline của bạn.
    """
    # Placeholder: tạo độ bất định giả lập dựa trên độ sáng trung bình.
    mean_val = float(np.mean(processed_img)) if processed_img is not None else 0.0
    uncertainty = float(np.clip((255.0 - mean_val) / 255.0, 0.0, 1.0))

    return {
        "diagnosis": "Mức 2: Tiền tăng sinh trung bình",
        "uncertainty": round(uncertainty, 4),
        "is_high_uncertainty": uncertainty > 0.5,
        "heatmap_url": "",
    }


def run_inference(image_path: str) -> dict:
    """Giữ lại API cũ: nhận đường dẫn ảnh và trả kết quả."""
    # Import muộn để tránh lỗi import vòng và để app chạy được dù người dùng đổi cấu trúc.
    try:
        from .image_processing import preprocess_image
    except Exception:
        from utils.image_processing import preprocess_image

    processed_img = preprocess_image(image_path)
    return predict(processed_img)
