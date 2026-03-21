"""AI inference pipeline — end-to-end DenseNet-121 classifier.

Artifact: `backend/models/dr_classifier.h5`
"""

from __future__ import annotations

from pathlib import Path
import os

import numpy as np

try:
    import tensorflow as tf
except Exception:  # pragma: no cover
    tf = None


CLASS_LABELS_VI = {
    0: "Mức 0 - Không bệnh",
    1: "Mức 1 - Nhẹ",
    2: "Mức 2 - Tiền tăng sinh nhẹ/trung bình",
    3: "Mức 3 - Nặng",
    4: "Mức 4 - Tăng sinh",
}

_classifier = None


def _mock_enabled() -> bool:
    return os.getenv("DR_ALLOW_MOCK", "0").strip() in {"1", "true", "TRUE", "yes", "YES"}


def _models_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "models"


def _load_model():
    global _classifier
    if _classifier is not None:
        return _classifier

    if tf is None:
        raise RuntimeError("Thiếu TensorFlow. Hãy cài `tensorflow` đúng phiên bản.")

    classifier_path = _models_dir() / "dr_classifier.h5"

    if not classifier_path.exists():
        raise FileNotFoundError(
            "Thiếu file model: backend/models/dr_classifier.h5. "
            "Sau khi train xong, hãy copy file này vào đúng thư mục."
        )

    if classifier_path.stat().st_size == 0:
        raise FileNotFoundError(
            "File model rỗng (0 bytes): backend/models/dr_classifier.h5. "
            "Hãy export/copy lại file model sau khi train."
        )

    _classifier = tf.keras.models.load_model(str(classifier_path))
    return _classifier


def check_model_ready() -> dict:
    """Used by /health endpoint."""
    try:
        _load_model()
        return {"ready": True, "mock_enabled": _mock_enabled()}
    except Exception as e:
        return {"ready": False, "error": str(e), "mock_enabled": _mock_enabled()}


def _soft_uncertainty_from_proba(proba: np.ndarray) -> tuple[float, float]:
    """Return (uncertainty_maxprob, entropy)."""
    proba = np.asarray(proba, dtype=np.float64)
    proba = np.clip(proba, 1e-12, 1.0)
    proba = proba / np.sum(proba)
    maxp = float(np.max(proba))
    uncertainty = float(1.0 - maxp)
    entropy = float(-np.sum(proba * np.log(proba)))
    return uncertainty, entropy


def predict(model_input: np.ndarray) -> dict:
    """Run inference on ONE preprocessed image.

    model_input: np.ndarray float32, shape (H, W, 3) after preprocess_input.
    """
    try:
        classifier = _load_model()
    except Exception as e:
        if _mock_enabled():
            mean_val = float(np.mean(model_input)) if model_input is not None else 0.0
            uncertainty = float(np.clip((1.0 - (mean_val / 255.0)), 0.0, 1.0))
            return {
                "predicted_class": 2,
                "diagnosis": CLASS_LABELS_VI.get(2, "Mức 2"),
                "probabilities": [0.05, 0.1, 0.6, 0.2, 0.05],
                "uncertainty": round(float(uncertainty), 6),
                "entropy": 0.0,
                "is_high_uncertainty": bool(uncertainty > 0.5),
                "heatmap_url": "",
                "mock": True,
                "mock_reason": str(e),
            }
        raise

    if model_input is None:
        raise ValueError("Ảnh đầu vào rỗng.")

    x = np.asarray(model_input, dtype=np.float32)
    if x.ndim != 3 or x.shape[-1] != 3:
        raise ValueError(f"Sai shape ảnh đầu vào: {x.shape}. Kỳ vọng (H,W,3).")

    x_batch = np.expand_dims(x, axis=0)  # (1, H, W, 3)

    proba = classifier(tf.constant(x_batch), training=False).numpy()[0]
    proba = np.asarray(proba, dtype=np.float64)
    if proba.ndim != 1 or proba.shape[0] != 5:
        raise RuntimeError(f"Output classifier không đúng: shape={proba.shape}, kỳ vọng (5,)")

    pred_class = int(np.argmax(proba))
    uncertainty, entropy = _soft_uncertainty_from_proba(proba)

    return {
        "predicted_class": pred_class,
        "diagnosis": CLASS_LABELS_VI.get(pred_class, f"Mức {pred_class}"),
        "probabilities": [float(p) for p in proba],
        "uncertainty": round(float(uncertainty), 6),
        "entropy": round(float(entropy), 6),
        "is_high_uncertainty": bool(uncertainty > 0.5),
        "heatmap_url": "",
    }


def run_inference(image_path: str) -> dict:
    """Backward-compatible helper: path -> preprocessing -> predict."""
    try:
        from .image_processing import preprocess_image
    except Exception:
        from utils.image_processing import preprocess_image

    model_input = preprocess_image(image_path)
    return predict(model_input)
