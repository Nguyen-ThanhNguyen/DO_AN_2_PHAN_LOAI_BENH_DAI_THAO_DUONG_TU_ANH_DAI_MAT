from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from pathlib import Path
import base64
import cv2
from werkzeug.utils import secure_filename

# Import linh hoạt để chạy được cả:
# - từ thư mục gốc: `python -m backend.app`
# - từ thư mục backend/: `python app.py`
try:
    from utils.image_processing import preprocess_image
    from utils.ai_inference import predict as predict_image
    from utils.ai_inference import check_model_ready
except Exception:
    from backend.utils.image_processing import preprocess_image
    from backend.utils.ai_inference import predict as predict_image
    from backend.utils.ai_inference import check_model_ready

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
CORS(app, resources={r"/api/*": {"origins": "*"}})

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


@app.route("/")
def index():
    return send_from_directory(str(FRONTEND_DIR), "index.html")


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def _encode_bgr_to_base64_jpg(img_bgr) -> str:
    """Encode a BGR numpy image to base64 JPEG string (no data: prefix)."""
    if img_bgr is None:
        return ""
    ok, buf = cv2.imencode(".jpg", img_bgr)
    if not ok:
        return ""
    return base64.b64encode(buf.tobytes()).decode("utf-8")


@app.route('/api/health', methods=['GET'])
def health():
    status = check_model_ready()
    http_code = 200 if status.get("ready") else 503
    return jsonify(status), http_code


@app.route('/api/predict', methods=['POST'])
def predict_route():
    if 'file' not in request.files:
        return jsonify({'error': 'Không tìm thấy file ảnh'}), 400
    
    file = request.files['file']
    if not file or not file.filename:
        return jsonify({'error': 'Chưa chọn file ảnh'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Định dạng không hợp lệ (png/jpg/jpeg)'}), 400

    filename = secure_filename(file.filename)
    filepath = UPLOAD_FOLDER / filename
    file.save(str(filepath))

    try:
        # BƯỚC 1: Tiền xử lý (CLAHE)
        model_input, clahe_vis = preprocess_image(str(filepath), return_visual=True)
        
        # BƯỚC 2: Gọi pipeline AI
        response_data = predict_image(model_input)

        # Kèm ảnh đã xử lý để frontend hiển thị (tuỳ UI dùng hay không)
        response_data["processed_image_base64_jpg"] = _encode_bgr_to_base64_jpg(clahe_vis)
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=False)