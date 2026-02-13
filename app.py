# app.py
from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
from utils import adjust_brightness_contrast, adjust_saturation, apply_blur, apply_sharpen, apply_edge
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Store uploaded image in memory
original_img = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global original_img
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    img_bgr = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    original_img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return "ok"

@app.route('/process', methods=['POST'])
def process():
    global original_img
    if original_img is None:
        return "No image uploaded", 400

    # Get slider values from frontend
    brightness = int(request.form.get('brightness', 0))
    contrast = int(request.form.get('contrast', 0))
    saturation = int(request.form.get('saturation', 0))
    blur = int(request.form.get('blur', 0))
    sharpen = int(request.form.get('sharpen', 0))
    edge = request.form.get('edge', 'false') == 'true'

    # Apply adjustments
    img = adjust_brightness_contrast(original_img, brightness, contrast)
    img = adjust_saturation(img, saturation)
    img = apply_blur(img, blur)
    img = apply_sharpen(img, sharpen)
    img = apply_edge(img, edge)

    # Convert to PNG for sending
    pil_img = Image.fromarray(img)
    buf = BytesIO()
    pil_img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
