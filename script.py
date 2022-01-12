from PyPDF2 import PdfFileReader,PdfFileWriter
import sys

inputs = sys.argv[1:]

def pdf_watermarker(pdf_file, watermark):
    file1 = PdfFileReader(open(pdf_file, 'rb'))
    file2 = PdfFileReader(open(watermark, 'rb'))
    page_quantity = file1.getNumPages()
    output = PdfFileWriter()
    for i in range(page_quantity):
        page = file1.getPage(i)
        page.mergePage(file2.getPage(0))
        output.addPage(page)

    with open('new_file.pdf', "wb") as outputStream:
        output.write(outputStream)

pdf_watermarker(inputs[1], inputs[2])


