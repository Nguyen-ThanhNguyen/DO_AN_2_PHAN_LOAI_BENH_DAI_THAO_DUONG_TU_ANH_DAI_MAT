/* ============================================================
   DR Diagnosis System — Frontend Logic
   ============================================================ */

// ─── Constants ──────────────────────────────────────────────────
const GRADE_COLORS = ["#22c55e", "#84cc16", "#f59e0b", "#ef4444", "#9f1239"];
const GRADE_TAGS = ["Grade 0", "Grade 1", "Grade 2", "Grade 3", "Grade 4"];
const MEDICAL_INFO = [
  "Không có dấu hiệu bệnh võng mạc đái tháo đường. Nên tiếp tục theo dõi và khám mắt định kỳ hàng năm. Kiểm soát tốt đường huyết và huyết áp để ngăn ngừa tiến triển.",
  "Giai đoạn nhẹ — xuất hiện một vài microaneurysm nhỏ ở võng mạc. Nên khám mắt mỗi 12 tháng và kiểm soát chặt đường huyết, lipid máu, huyết áp.",
  "Giai đoạn vừa — microaneurysm, xuất huyết điểm, xuất tiết cứng. Nên điều trị nội khoa tích cực và khám mắt mỗi 3–6 tháng để theo dõi tiến triển.",
  "Giai đoạn nặng — xuất huyết nhiều tầng, dải tĩnh mạch, IRMA. Nguy cơ tiến triển sang tăng sinh rất cao. Cần điều trị và khám chuyên khoa mắt trong vòng 4 tuần.",
  "Giai đoạn tăng sinh — tân sinh mạch máu bất thường, nguy cơ mất thị lực cao. Cần điều trị khẩn cấp: laser quang đông, tiêm nội nhãn, hoặc phẫu thuật cắt dịch kính.",
];
const HISTORY_KEY = "dr_history";
const HISTORY_MAX = 10;

// ─── Init ────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  setupDropzone();
  checkServerStatus();
  loadHistory();
});

// ─── Server status ───────────────────────────────────────────────
async function checkServerStatus() {
  const dot = document.getElementById("statusDot");
  const txt = document.getElementById("statusText");
  try {
    const res = await fetch("/api/health", {
      signal: AbortSignal.timeout(5000),
    });
    const data = await res.json();
    if (data.ready) {
      dot.className = "status-dot online";
      txt.textContent =
        "Server sẵn sàng" + (data.mock_enabled ? " (Mock)" : "");
    } else {
      dot.className = "status-dot offline";
      txt.textContent = "Model chưa sẵn sàng";
    }
  } catch {
    dot.className = "status-dot offline";
    txt.textContent = "Không kết nối được";
  }
}

// ─── Dropzone ────────────────────────────────────────────────────
function setupDropzone() {
  const zone = document.getElementById("dropzone");
  const input = document.getElementById("imageInput");

  zone.addEventListener("dragover", (e) => {
    e.preventDefault();
    zone.classList.add("drag-over");
  });
  zone.addEventListener("dragleave", (e) => {
    if (!zone.contains(e.relatedTarget)) zone.classList.remove("drag-over");
  });
  zone.addEventListener("drop", (e) => {
    e.preventDefault();
    zone.classList.remove("drag-over");
    const file = e.dataTransfer.files[0];
    if (file) setFile(file);
  });

  input.addEventListener("change", () => {
    if (input.files[0]) setFile(input.files[0]);
  });
}

function handleDropzoneClick() {
  if (document.getElementById("dzPreview").style.display !== "none") return;
  document.getElementById("imageInput").click();
}

function setFile(file) {
  const allowed = ["image/png", "image/jpeg"];
  if (!allowed.includes(file.type)) {
    showToast("Định dạng không hợp lệ. Vui lòng chọn PNG hoặc JPG.", "error");
    return;
  }
  if (file.size > 10 * 1024 * 1024) {
    showToast("Ảnh quá lớn (tối đa 10 MB).", "error");
    return;
  }

  const reader = new FileReader();
  reader.onload = (e) => {
    document.getElementById("previewThumb").src = e.target.result;
  };
  reader.readAsDataURL(file);

  document.getElementById("dzFname").textContent = file.name;
  document.getElementById("dzFsize").textContent = formatBytes(file.size);
  document.getElementById("dzIdle").style.display = "none";
  document.getElementById("dzPreview").style.display = "flex";
  document.getElementById("btnDiagnose").disabled = false;

  // Attach file to input
  const dt = new DataTransfer();
  dt.items.add(file);
  document.getElementById("imageInput").files = dt.files;
}

function clearFile(event) {
  if (event) event.stopPropagation();
  document.getElementById("imageInput").value = "";
  document.getElementById("dzIdle").style.display = "flex";
  document.getElementById("dzPreview").style.display = "none";
  document.getElementById("btnDiagnose").disabled = true;
  document.getElementById("resultCard").style.display = "none";
}

// ─── Main upload & predict ───────────────────────────────────────
async function uploadImage() {
  const input = document.getElementById("imageInput");
  const file = input.files[0];
  if (!file) {
    showToast("Vui lòng chọn ảnh trước!", "error");
    return;
  }

  // Store original image preview URL
  const origSrc = document.getElementById("previewThumb").src;
  document.getElementById("resultOrigImg").src = origSrc;

  showLoading(true);

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("/api/predict", {
      method: "POST",
      body: formData,
    });
    const data = await response.json();

    if (!response.ok || data.error) {
      throw new Error(data.error || `HTTP ${response.status}`);
    }

    renderResults(data, origSrc);
    saveToHistory(data, origSrc);
    loadHistory();
    showToast("Chẩn đoán hoàn tất!", "success");

    document
      .getElementById("resultCard")
      .scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (err) {
    console.error("Predict error:", err);
    showToast("Lỗi kết nối đến server AI: " + err.message, "error");
  } finally {
    showLoading(false);
  }
}

// ─── Render results ──────────────────────────────────────────────
function renderResults(data, origSrc) {
  const grade = data.predicted_class ?? 0;
  const color = GRADE_COLORS[grade] ?? "#888";

  // Show result card
  document.getElementById("resultCard").style.display = "block";

  // Severity banner
  const banner = document.getElementById("severityBanner");
  banner.dataset.grade = grade;
  document.getElementById("sevGrade").textContent = grade;
  document.getElementById("sevName").textContent = data.diagnosis ?? "---";
  const sevTag = document.getElementById("sevTag");
  sevTag.textContent = GRADE_TAGS[grade] ?? `Grade ${grade}`;
  sevTag.style.color = color;

  // Images
  document.getElementById("resultOrigImg").src = origSrc;
  const procImg = document.getElementById("resultProcImg");
  const clahePanel = document.getElementById("clahePanel");
  if (data.processed_image_base64_jpg) {
    procImg.src = "data:image/jpeg;base64," + data.processed_image_base64_jpg;
    clahePanel.style.display = "block";
  } else {
    clahePanel.style.display = "none";
  }

  // Probability bars
  renderProbaBars(data.probabilities ?? [], grade, color);

  // Uncertainty
  const unc = data.uncertainty ?? 0;
  const uncPct = (unc * 100).toFixed(1) + "%";
  document.getElementById("uncValue").textContent = uncPct;
  document.getElementById("uncValue").style.color =
    unc > 0.5 ? "#ef4444" : unc > 0.25 ? "#f59e0b" : "#22c55e";
  setTimeout(() => {
    document.getElementById("uncFill").style.width = unc * 100 + "%";
  }, 80);

  // Warning
  const warn = document.getElementById("alertWarn");
  warn.style.display = data.is_high_uncertainty || unc > 0.5 ? "flex" : "none";

  // Medical info
  document.getElementById("medText").textContent = MEDICAL_INFO[grade] ?? "---";
}

function renderProbaBars(probs, activeGrade, activeColor) {
  const labels = [
    "Mức 0 — Không bệnh",
    "Mức 1 — Nhẹ",
    "Mức 2 — Vừa",
    "Mức 3 — Nặng",
    "Mức 4 — Tăng sinh",
  ];

  const grid = document.getElementById("probaGrid");
  grid.innerHTML = "";

  probs.forEach((p, i) => {
    const pct = (p * 100).toFixed(1);
    const color = GRADE_COLORS[i] ?? "#888";
    const row = document.createElement("div");
    row.className = "proba-row" + (i === activeGrade ? " active" : "");

    row.innerHTML = `
      <span class="proba-name">${labels[i] ?? "Mức " + i}</span>
      <div class="proba-track">
        <div class="proba-fill" id="bar-${i}" style="background:${color};width:0%"></div>
      </div>
      <span class="proba-pct" style="color:${i === activeGrade ? color : ""}">${pct}%</span>
    `;
    grid.appendChild(row);
    // Animate bar after DOM insertion
    setTimeout(
      () => {
        document.getElementById("bar-" + i).style.width = p * 100 + "%";
      },
      80 + i * 60,
    );
  });
}

// ─── History (localStorage) ──────────────────────────────────────
function saveToHistory(data, thumbSrc) {
  const history = getHistory();
  const entry = {
    id: Date.now(),
    date: formatDate(new Date()),
    diagnosis: data.diagnosis ?? "---",
    grade: data.predicted_class ?? 0,
    uncertainty: data.uncertainty ?? 0,
    thumb: thumbSrc,
  };
  history.unshift(entry);
  while (history.length > HISTORY_MAX) history.pop();
  localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
}

function getHistory() {
  try {
    return JSON.parse(localStorage.getItem(HISTORY_KEY) ?? "[]");
  } catch {
    return [];
  }
}

function loadHistory() {
  const history = getHistory();
  const wrap = document.getElementById("historyWrap");
  const list = document.getElementById("historyList");

  if (!history.length) {
    wrap.style.display = "none";
    return;
  }
  wrap.style.display = "block";
  list.innerHTML = "";

  history.forEach((item) => {
    const color = GRADE_COLORS[item.grade] ?? "#888";
    const unc = (item.uncertainty * 100).toFixed(0) + "% uncertainty";
    const div = document.createElement("div");
    div.className = "history-item";
    div.innerHTML = `
      <img class="hist-thumb" src="${item.thumb}" alt="" />
      <div class="hist-info">
        <p class="hist-diag">${item.diagnosis}</p>
        <p class="hist-meta">${item.date} &nbsp;·&nbsp; ${unc}</p>
      </div>
      <span class="hist-grade" style="color:${color};border-color:${color}20;background:${color}18">
        ${GRADE_TAGS[item.grade] ?? "G" + item.grade}
      </span>
    `;
    list.appendChild(div);
  });
}

function clearHistory() {
  localStorage.removeItem(HISTORY_KEY);
  document.getElementById("historyWrap").style.display = "none";
  showToast("Đã xóa lịch sử chẩn đoán.", "info");
}

// ─── Lightbox ────────────────────────────────────────────────────
function openLightbox(img) {
  const lb = document.getElementById("lightbox");
  document.getElementById("lightboxImg").src = img.src;
  lb.classList.add("open");
}
function closeLightbox() {
  document.getElementById("lightbox").classList.remove("open");
}

// ─── Loading overlay ──────────────────────────────────────────────
function showLoading(visible) {
  document.getElementById("loadingOverlay").style.display = visible
    ? "flex"
    : "none";
}

// ─── Toast notifications ──────────────────────────────────────────
function showToast(message, type = "info") {
  const container = document.getElementById("toastContainer");
  const icons = { success: "✅", error: "❌", info: "ℹ️" };
  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `<span>${icons[type] ?? "•"}</span><span>${message}</span>`;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transition = "opacity 0.3s";
    setTimeout(() => toast.remove(), 320);
  }, 3500);
}

// ─── Utilities ────────────────────────────────────────────────────
function formatBytes(bytes) {
  if (bytes < 1024) return bytes + " B";
  if (bytes < 1048576) return (bytes / 1024).toFixed(1) + " KB";
  return (bytes / 1048576).toFixed(1) + " MB";
}

function formatDate(d) {
  const pad = (n) => String(n).padStart(2, "0");
  return `${pad(d.getDate())}/${pad(d.getMonth() + 1)}/${d.getFullYear()} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}
