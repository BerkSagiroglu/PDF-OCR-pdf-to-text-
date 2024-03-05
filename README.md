# PDF-OCR-pdf-to-text-
A python script that extracts all the text and images in the PDF to .txt format.


You need the download Poppler For Windows & Tesseract For Windows and add in the file paths in the .py file which is;

Reference for Tesseract : https://github.com/tesseract-ocr/tesseract/releases/

Reference for Poppler : https://github.com/oschwartz10612/poppler-windows/releases/

Line 17:    images = convert_from_path(pdf_file,poppler_path=r'C:\PATH TO POPPLER\poppler-24.02.0\Library\bin') ## Change the path poppler path.

Line 20:    pytesseract.pytesseract.tesseract_cmd = r'C:\PATH TO TESSERACT\Tesseract-OCR\tesseract.exe'       # Change the path Tesseract path.

You can type -h for help.

Example : python.exe .\PdfOCR.py -p PATH-TO-PDF-FILE -o PATH-TO-OUTPUT.txt
