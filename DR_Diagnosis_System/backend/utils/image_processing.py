import cv2
import numpy as np

def preprocess_image(image_path):
    # 1. Đọc ảnh
    img = cv2.imread(image_path)
    # 2. Cắt viền đen (Crop) - Code rút gọn
    # ... (Code tìm contour và crop)
    
    # 3. Resize về kích thước model (ví dụ 299x299 cho InceptionV3)
    img_resized = cv2.resize(img, (299, 299))
    
    # 4. Áp dụng CLAHE (Tăng độ tương phản cục bộ)
    lab = cv2.cvtColor(img_resized, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    final_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    return final_img