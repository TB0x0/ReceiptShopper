# ReceiptShopper

Milestones:

1. Preprocessing the Receipt Image - [x]
    - Image Enhancement: Improve readability using OpenCV (e.g., grayscale conversion, noise removal, contrast enhancement).
    - Text Alignment: Correct distortions using perspective transformation.
    - Text Region Detection: Use edge detection and contouring to isolate text areas.
2. Optical Character Recognition (OCR) - [ ]
    - Use Tesseract OCR: Extract text from the receipt.
    - Post-processing: Remove artifacts and correct errors using spell-checking or regex filtering.
3. Item Classification - [ ]
    - Keyword Matching: Map extracted text to known product categories.
    - Named Entity Recognition (NER): Use NLP techniques to identify product names, prices, and categories.
4. Structuring Data - [ ]
    - Organize extracted data into structured formats like JSON or CSV.
