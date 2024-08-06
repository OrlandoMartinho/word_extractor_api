
# Text Extraction API

A Flask API for extracting text from image and PDF files using PyMuPDF and Tesseract OCR.

## Project Structure

```
your_project/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── services.py
│
├── text_extractor/
│   ├── __init__.py
│   └── extractor.py
│
├── tests/
│   ├── __init__.py
│   └── test_app.py
│
├── requirements.txt
├── .env
└── run.py
```

## Prerequisites

- Python 3.7 or higher
- Tesseract OCR installed
- Microsoft Visual C++ 14.0 (required for Tesseract)

## Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd your_project
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Tesseract path**:

   - Download and install Tesseract OCR from [this link](https://tenet.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-3.02.02-win32-lib-include-dirs.zip?viasf=1). Follow the instructions provided by the installer to complete the installation.
   - Place the Tesseract installation in the `includes` folder of your project, such as `includes\Tesseract-OCR`.

   Create a `.env` file in the root directory of the project with the following content:

   ```
   TESSERACT_CMD=includes\Tesseract-OCR\tesseract.exe
   ```

   Adjust the path if your Tesseract installation directory is different.

4. **Install Microsoft Visual C++ 14.0**:

   Tesseract requires Microsoft Visual C++ 14.0. You can download and install it from the [Microsoft website](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

5. **Run the Flask application**:

   ```bash
   python run.py
   ```

## API Endpoints

### Convert Image

- **Endpoint**: `/convert-image`
- **Method**: `POST`
- **Form Data**: `file` (image file with extensions `png`, `jpg`, or `jpeg`)
- **Response**: JSON object containing the extracted text or an error message.

### Convert PDF

- **Endpoint**: `/convert-pdf`
- **Method**: `POST`
- **Form Data**: `file` (PDF file)
- **Response**: JSON object containing the extracted text or an error message.

## Testing

To test the API, create a file named `test_api.py` and use the following script to send requests to the API:

```python
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
    test_convert_image('path/to/your/image.jpg')
    test_convert_pdf('path/to/your/document.pdf')
```

Run the test script with:

```bash
python test_api.py
```



