# TB0x0
# Image pre-processing before attempting OCR

import cv2 as cv
import numpy as np

def ImgPP(img_path):
    # CV read img
    img = cv2.imread(img_path)
    original = img.copy()

    gscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussionBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADATPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2 
    )

    edges = cv2.Canny(thresh, 50, 150)
