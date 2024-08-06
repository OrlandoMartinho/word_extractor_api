# text_extractor/extractor.py
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os
# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

class TextExtractor:
    def extract_text_from_pdf(self, pdf_file):
        doc = fitz.open(stream=pdf_file, filetype='pdf')
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def extract_text_from_image(self, image_file):
        img = Image.open(io.BytesIO(image_file))
        text = pytesseract.image_to_string(img)
        return text
