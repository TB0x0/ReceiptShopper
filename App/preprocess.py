# TB0x0
# Image pre-processing before attempting OCR

import cv2
import numpy as np

def order_points(pts):
    #Sort points to TL, BR, TR, BL
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # Top-left
    rect[2] = pts[np.argmax(s)]  # Bottom-right
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # Top-right
    rect[3] = pts[np.argmax(diff)]  # Bottom-left
    return rect

def four_point_transform(image, pts):
    # Transform perspective to top down view
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

# Image Pre-Processing Main
def ImgPP(img_path):
    # CV read img
    img = cv2.imread(img_path)
    original = img.copy()

    gscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gscale, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10 
    )

    edges = cv2.Canny(thresh, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    receipt_contour = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:
            receipt_contour = approx
            break

    if receipt_contour.any():
        receipt = four_point_transform(original, receipt_contour.reshape(4, 2))
        return receipt, edges, thresh
    else:
        return None, edges, thresh
    

# Test the function
image_path = "C:/proj/ReceiptShopper/Tests/testR1.jpg"  # Replace with your image path
receipt, edges, thresh = ImgPP(image_path)

if receipt.any():
    cv2.imshow("Warped Receipt", receipt)
    cv2.imshow("Edges", edges)
    cv2.imshow("Thresholded", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()