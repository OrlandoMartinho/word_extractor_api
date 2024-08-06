# app/routes.py
from flask import Blueprint, request, jsonify
from app.services import TextExtractionService

bp = Blueprint('main', __name__)
service = TextExtractionService()

@bp.route('/convert-image', methods=['POST'])
def convert_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
    
    file = request.files['file']
    return service.convert_image(file)

@bp.route('/convert-pdf', methods=['POST'])
def convert_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400
    
    file = request.files['file']
    return service.convert_pdf(file)
