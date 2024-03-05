import argparse
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import PyPDF2

def extract_text_and_images_from_pdf(pdf_file, output_file=None):
    # Extract text using PyPDF2
    text = ""
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Extract images using pdf2image
    images = convert_from_path(pdf_file,poppler_path=r'C:\Users\X\Desktop\poppler-24.02.0\Library\bin') #poppler path'i gösteriyorsun

    # Extract text from images using OCR
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'       #tesseract path'i gösteriyorsun
    image_texts = []
    for image in images:
        image_text = pytesseract.image_to_string(image)
        image_texts.append(image_text)

    # Combine text from PDF and images
    full_text = text + '\n'.join(image_texts)

    # If output file is provided, write the text to the file
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(full_text)
            print(f"Text extracted from PDF and saved to {output_file}")
    else:
        print(full_text)

if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='Extract text and images from PDF file.')
    
    # Add arguments
    parser.add_argument('-p', '--pdf', type=str, required=True, help='Path to the PDF file')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Extract text and images from PDF
    extract_text_and_images_from_pdf(args.pdf, args.output)
