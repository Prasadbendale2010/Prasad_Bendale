import os
from docx2pdf import convert

word_folder = r'C:\Users\Avinash Matre\Documents\iLovePDF_Output\ilovepdf-pdf-to-word (2) - Copy'
pdf_output_folder = r'C:\Users\Avinash Matre\Documents\iLovePDF_Output\PDF'

# Create output folder if it doesn't exist
os.makedirs(pdf_output_folder, exist_ok=True)

# Convert all docx files in the word_folder to pdfs in the pdf_output_folder
convert(word_folder, pdf_output_folder)
