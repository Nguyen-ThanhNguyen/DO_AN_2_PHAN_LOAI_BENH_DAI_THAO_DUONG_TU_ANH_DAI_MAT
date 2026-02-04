async function uploadImage() {
  const fileInput = document.getElementById("imageInput");
  const file = fileInput.files[0];

  if (!file) {
    alert("Vui lòng chọn ảnh đáy mắt!");
    return;
  }

  // Hiển thị ảnh xem trước
  const previewImg = document.getElementById("previewImg");
  previewImg.src = URL.createObjectURL(file);
  document.getElementById("resultArea").style.display = "block";

  // Gửi ảnh sang Backend Python
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    // Hiển thị kết quả lên màn hình
    document.getElementById("lblResult").innerText = data.diagnosis;
    document.getElementById("lblUncertainty").innerText =
      (data.uncertainty * 100).toFixed(1) + "%";

    // Xử lý cảnh báo độ bất định
    const warningBox = document.getElementById("warningBox");
    if (data.is_high_uncertainty || data.uncertainty > 0.5) {
      warningBox.style.display = "block";
      warningBox.style.color = "red";
    } else {
      warningBox.style.display = "none";
    }
  } catch (error) {
    console.error("Lỗi:", error);
    alert("Có lỗi kết nối đến Server AI!");
  }
}
