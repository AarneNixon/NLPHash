from PyPDF2 import PdfFileReader, PdfFileWriter
#with open("output.pdf", "rb") as in_file:
output_pdf = PdfFileWriter()
#in_file)
#output_pdf = PdfFileWriter('output.pdf')
#	output_pdf.appendPagesFromReader(input_pdf)
output_pdf.encrypt("password")
with open("output.pdf", "wb") as out_file:
        output_pdf.write(out_file)
