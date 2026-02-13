# utils.py
import cv2
import numpy as np

def adjust_brightness_contrast(img, brightness=0, contrast=0):
    """
    Adjust brightness and contrast.
    brightness: -100 to 100
    contrast: -100 to 100
    """
    img = img.astype(float)
    img = img * (1 + contrast / 100.0) + brightness
    return np.clip(img, 0, 255).astype(np.uint8)

def adjust_saturation(img, saturation=0):
    """
    Adjust image saturation.
    saturation: -100 to 100
    """
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV).astype(float)
    h, s, v = cv2.split(img_hsv)
    s = np.clip(s * (1 + saturation / 100.0), 0, 255)
    img_hsv = cv2.merge([h, s, v])
    return cv2.cvtColor(img_hsv.astype(np.uint8), cv2.COLOR_HSV2RGB)

def apply_blur(img, ksize=0):
    """
    Apply Gaussian blur.
    ksize: 0 → no blur, higher → more blur
    """
    if ksize > 0:
        k = ksize * 2 + 1
        return cv2.GaussianBlur(img, (k, k), 0)
    return img

def apply_sharpen(img, intensity=0):
    """
    Apply sharpening filter.
    intensity: 0 → no sharpen, higher → stronger sharpen
    """
    if intensity > 0:
        kernel = np.array([[0, -1, 0],
                           [-1, 5 + intensity, -1],
                           [0, -1, 0]])
        return cv2.filter2D(img, -1, kernel)
    return img

def apply_edge(img, edge_on=False):
    """
    Apply edge detection (Canny).
    edge_on: True/False
    """
    if edge_on:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return img
