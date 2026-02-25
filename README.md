# FPCV Image Explorer 🖼️

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight **web-based image editing tool** built with **Flask** that allows users to upload images and apply interactive adjustments in real time. The interface provides a clear **side-by-side comparison** between the original and edited versions.

---

## ✨ Overview

**FPCV Image Explorer** is a simple yet practical image manipulation application demonstrating fundamental computer vision operations through an intuitive browser interface.

Users can modify visual properties such as brightness, contrast, saturation, blur, sharpening, and edge detection — all without page reloads.

---

## 📸 Demo

![Demo](demo.png)

---

## 🚀 Features

✔ Upload images directly from the browser  
✔ Real-time image adjustments using sliders  

Available controls:

- **Brightness**
- **Contrast**
- **Saturation**
- **Blur**
- **Sharpen**
- **Edge Detection Toggle**

✔ Instant visual feedback  
✔ Original vs edited comparison view  
✔ Download edited images  
✔ Clean, responsive UI  

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SaakshiMV/FPCV_ImageExplorer.git
cd FPCV_ImageExplorer
````

---

### 2️⃣ Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🧭 Usage

1. Launch the Flask server
2. Upload an image
3. Adjust sliders to modify image properties
4. Enable edge detection if desired
5. Download the edited image

---

## 📂 Project Structure

```
FPCV_ImageExplorer/
│
├── app.py              # Flask application entry point
├── utils.py            # Image processing logic
├── requirements.txt    # Dependencies
├── README.md
├── .gitignore
├── demo.png
├── demo.gif
│
├── templates/
│   └── index.html      # Frontend UI
│
├── static/
│   ├── style.css       # Styling
│   └── script.js       # Client-side interactions
│
└── venv/               # Virtual environment (ignored)
```

---

## 🔮 Potential Improvements

* Live histogram visualization
* Additional filters (grayscale, sepia, invert, etc.)
* Drag-and-drop uploads
* Batch image processing
* Performance optimizations

---

## 📜 License

This project is licensed under the **MIT License**.
