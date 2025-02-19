# TB0x0 2024
# Receipt Shopper Main

import pytesseract as pt
import preprocess

TEST_IMAGE = 'C:/proj/ReceiptShopper/Tests/testR1.jpg'
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR

def ocrCore(img):
    receipt, edges, thresh = preprocess.ImgPP(img)
    return pt.image_to_string(thresh)


#test OCR
print(ocrCore(TEST_IMAGE))