const uploadForm = document.getElementById("uploadForm");
const originalImage = document.getElementById("originalImage");
const adjustedImage = document.getElementById("adjustedImage");

const sliders = ["brightness", "contrast", "saturation", "blur", "sharpen"];
const sliderValues = {};

sliders.forEach(id => {
    const slider = document.getElementById(id);
    const span = document.getElementById(id + "Val");
    slider.addEventListener("input", () => {
        span.innerText = slider.value;
        sliderValues[id] = slider.value;
        processImage();
    });
});

document.getElementById("edge").addEventListener("change", processImage);

uploadForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const file = document.getElementById("imageInput").files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    fetch("/upload", { method: "POST", body: formData })
    .then(res => res.text())
    .then(() => {
        const reader = new FileReader();
        reader.onload = e => originalImage.src = e.target.result;
        reader.readAsDataURL(file);
        processImage();
    });
});

function processImage() {
    if (!originalImage.src) return;

    const formData = new FormData();
    sliders.forEach(id => formData.append(id, document.getElementById(id).value));
    formData.append("edge", document.getElementById("edge").checked);

    fetch("/process", { method: "POST", body: formData })
    .then(res => res.blob())
    .then(blob => {
        adjustedImage.src = URL.createObjectURL(blob);
    });
}

// Download
document.getElementById("downloadBtn").addEventListener("click", () => {
    if (!adjustedImage.src) return;
    const link = document.createElement("a");
    link.href = adjustedImage.src;
    link.download = "adjusted_image.png";
    link.click();
});
