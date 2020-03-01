import nltk
import sys
import fileinput
from PyPDF2 import PdfFileReader, PdfFileWriter
#from nltk.corpus import brown
#nltk.download('brown')
nltk.download('punkt')
#brown.words()
#from nltk.book import *
#from nltk.tokenize import sent_tokenize, word_tokenize
#text = "t e x t  t e s t."
if len(sys.argv) > 2:
	print 'target file', sys.argv[1]
	print 'source file', sys.argv[2]
#	with open(sys.argv[1], "rb") as target:
#		print(target)
#		tgt_pdf = PdfFileReader(target)
	tgt_pdf = PdfFileReader(sys.argv[1])
	if tgt_pdf.isEncrypted:
		print "is encrypted"
	else:
		print "is unencrypted"
	found_answer = 0
	for i in fileinput.input(sys.argv[2]):
#			for j in i.split():
		for j in nltk.word_tokenize(i):
			if found_answer == 1:
				break
			tgt_pdf.decrypt(j)
			try:
				print("num pages ",tgt_pdf.getNumPages())
				print("solved, answer is {}", j)
				found_answer=1
				break
			except:
				print('tested ',j)
#				print "failed."
else:
	print 'usage: python hcrack.py target_file source_file'
#output_pdf = PdfFileWriter()
#output_pdf.appendPagesFromReader(input_pdf)
#output_pdf.encrypt("password")
#with open("output.pdf", "wb") as out_file:
#        output_pdf.write(out_file)
'''
#with open("input.pdf", "rb") as in_file:
#    input_pdf = PdfFileReader(in_file)

output_pdf = PdfFileWriter()
#output_pdf.appendPagesFromReader(input_pdf)
output_pdf.encrypt("password")

with open("output.pdf", "wb") as out_file:
        output_pdf.write(out_file)
'''
