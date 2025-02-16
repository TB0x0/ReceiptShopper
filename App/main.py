# TB0x0 2024
# Receipt Shopper Main

import pytesseract as pt
import preprocess

TEST_IMAGE = 'C:/proj/ReceiptShopper/Tests/testR1.jpg'
# OCR

def ocrCore(img):
    receipt, edges, thresh = preprocess.ImgPP(img)
    return pt.image_to_string(img.fromarray(thresh))

print(ocrCore(TEST_IMAGE))