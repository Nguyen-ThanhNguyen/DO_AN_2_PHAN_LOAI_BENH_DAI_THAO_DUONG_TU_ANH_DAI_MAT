from __future__ import annotations

import cv2
import numpy as np

try:
    from tensorflow.keras.applications.densenet import preprocess_input as densenet_preprocess_input
except Exception:  # pragma: no cover
    densenet_preprocess_input = None


def _densenet_preprocess_fallback(x_rgb: np.ndarray) -> np.ndarray:
    """Fallback khi TensorFlow chưa được cài: normalize về [0, 1]."""
    return x_rgb.astype(np.float32) / 255.0


def _crop_black_borders(img_bgr: np.ndarray, threshold: int = 10) -> np.ndarray:
    """Crop viền đen xung quanh vùng võng mạc tròn."""
    if img_bgr is None or img_bgr.size == 0:
        return img_bgr

    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    mask = (gray > threshold).astype(np.uint8) * 255

    coords = cv2.findNonZero(mask)
    if coords is None:
        return img_bgr

    x, y, w, h = cv2.boundingRect(coords)
    if w <= 0 or h <= 0:
        return img_bgr

    return img_bgr[y : y + h, x : x + w]


def _apply_clahe_lab(img_bgr: np.ndarray, clip_limit: float = 2.0, tile_grid_size=(8, 8)) -> np.ndarray:
    """Tăng cường tương phản cục bộ trên kênh L của không gian LAB."""
    lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)


def preprocess_image(
    image_path: str,
    img_size: int = 224,
    return_visual: bool = False,
):
    """Đọc ảnh -> crop viền -> resize 224x224 -> CLAHE -> DenseNet preprocess_input.

    Returns:
        - model_input: np.ndarray float32 (H, W, 3)
        - (optional) clahe_vis: BGR uint8 dùng để hiển thị trên UI
    """
    img = cv2.imread(str(image_path))
    if img is None:
        raise ValueError("Không đọc được ảnh. Hãy kiểm tra đường dẫn/định dạng ảnh.")

    img = _crop_black_borders(img)
    img = cv2.resize(img, (img_size, img_size), interpolation=cv2.INTER_AREA)

    clahe_bgr = _apply_clahe_lab(img)

    # DenseNet expects RGB input
    clahe_rgb = cv2.cvtColor(clahe_bgr, cv2.COLOR_BGR2RGB)
    if densenet_preprocess_input is not None:
        model_input = densenet_preprocess_input(clahe_rgb.astype(np.float32))
    else:
        model_input = _densenet_preprocess_fallback(clahe_rgb)

    if return_visual:
        return model_input, clahe_bgr
    return model_input
