from flask import Flask, request, jsonify
from flask_cors import CORS

from pathlib import Path
from werkzeug.utils import secure_filename

# Import linh hoạt để chạy được cả:
# - từ thư mục gốc: `python -m backend.app`
# - từ thư mục backend/: `python app.py`
try:
    from utils.image_processing import preprocess_image
    from utils.ai_inference import predict
except Exception:
    from backend.utils.image_processing import preprocess_image
    from backend.utils.ai_inference import predict

app = Flask(__name__)
CORS(app) # Cho phép Frontend (HTML) gọi được API

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
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
        processed_img = preprocess_image(filepath)
        
        # BƯỚC 2: Gọi pipeline AI
        response_data = predict(processed_img)
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)