# test_api.py
import requests

# Define the URLs for the API endpoints
IMAGE_URL = 'http://127.0.0.1:5000/convert-image'
PDF_URL = 'http://127.0.0.1:5000/convert-pdf'

# Test image conversion
def test_convert_image(image_path):
    with open(image_path, 'rb') as img_file:
        files = {'file': img_file}
        response = requests.post(IMAGE_URL, files=files)
        print("Image Conversion Response:")
        print(response.json())

# Test PDF conversion
def test_convert_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        files = {'file': pdf_file}
        response = requests.post(PDF_URL, files=files)
        print("PDF Conversion Response:")
        print(response.json())

# Example usage
if __name__ == '__main__':
    # Replace 'path/to/your/image.jpg' and 'path/to/your/document.pdf' with your actual file paths
    test_convert_image('main.jpg')
    test_convert_pdf('test.pdf')
