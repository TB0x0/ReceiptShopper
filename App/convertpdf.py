# -*- coding: utf-8 -*-

from pdf2image import convert_from_path as PDFConv
import sys

def ConvertPDF(pdf_path, poppler_path = "poppler-22.04.0/Library/bin", saveas_seed = "PDF2IMG"):
    converted_imgs = PDFConv(pdf_path, poppler_path=poppler_path)
    
    for i in range(len(converted_imgs)):
        converted_imgs[i].save('page'+ str(i) + saveas_seed + '.jpg', 'JPEG')
        



