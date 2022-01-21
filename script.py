from PyPDF2 import PdfFileReader,PdfFileWriter
import sys
import io

inputs = sys.argv[1:]

def pdf_watermarker(pdf_file, watermark):
    with open(pdf_file, 'rb') as file1:
        bytes_obj = io.BytesIO(file1.read())
    file1 = PdfFileReader(bytes_obj, 'rb')
    file2 = PdfFileReader(open(watermark, 'rb'))
    page_quantity = file1.getNumPages()
    output = PdfFileWriter()
    for i in range(page_quantity):
        page = file1.getPage(i)
        page.mergePage(file2.getPage(0))
        output.addPage(page)

    with open(pdf_file, "wb") as outputStream:
        output.write(outputStream)

pdf_watermarker(inputs[0], inputs[1])


