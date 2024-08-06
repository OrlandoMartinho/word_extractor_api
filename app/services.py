# app/services.py
from flask import jsonify
from text_extractor.extractor import TextExtractor

class TextExtractionService:
    def __init__(self):
        self.extractor = TextExtractor()

    def convert_image(self, file):
        if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
            text = self.extractor.extract_text_from_image(file.read())
            return jsonify({'text': text})
        else:
            return jsonify({'error': 'Invalid file format. Please upload a PNG, JPG, or JPEG image.'}), 400

    def convert_pdf(self, file):
        if file and file.filename.lower().endswith('.pdf'):
            text = self.extractor.extract_text_from_pdf(file.read())
            return jsonify({'text': text})
        else:
            return jsonify({'error': 'Invalid file format. Please upload a PDF file.'}), 400
