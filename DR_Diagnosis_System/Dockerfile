FROM python:3.11-slim

# Tránh prompt khi cài apt
ENV DEBIAN_FRONTEND=noninteractive

# Cài thư viện hệ thống cần cho OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxrender1 libxext6 libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements trước để tận dụng Docker cache
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy toàn bộ project
COPY . .

# HF Spaces yêu cầu port 7860
EXPOSE 7860

# Chạy Flask trên port 7860
CMD ["python", "-m", "backend.app"]