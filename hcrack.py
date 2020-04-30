import nltk
import sys
import fileinput
import hashlib
from PyPDF2 import PdfFileReader, PdfFileWriter
#from nltk.corpus import brown
#nltk.download('brown')
nltk.download('punkt')
#brown.words()
#from nltk.book import *
#from nltk.tokenize import sent_tokenize, word_tokenize
#text = "t e x t  t e s t."
if len(sys.argv) > 2:
	print 'format', sys.argv[1]
	format = sys.argv[1]
	print 'target file', sys.argv[2]
	target_file = sys.argv[2]
	print 'nlp options', sys.argv[3]
	print 'source file', sys.argv[4]
	source_file = sys.argv[4]
	useTokenize=False
	useLemmatize=False
	usePOS=False
	for char in sys.argv[3]:
		if char == 'W':
			print 'Will attempt every distinct word from target file'
			useTokenize=True;
		elif char == 'L':
			print 'Will attempt words similar to the every word from the target file'
			useLemmatize=True;
#		elif char == 'P':
#			print 'Part of speech tagging will limit word types used from target file, allowing:'
#			for char in sys.argv[4]:
#			useLemmatize=True;
	found_answer = 0
	if format == "pdf":
		tgt_pdf = PdfFileReader(target_file)
		if tgt_pdf.isEncrypted:
			print "is encrypted"
		else:
			print "is unencrypted"
		for i in fileinput.input(source_file):
			for j in nltk.word_tokenize(i):
				if useLemmatize:
					if found_answer == 1:
						break
					tgt_pdf.decrypt(j)
					try:
						x=tgt_pdf.getNumPages()
						print('solved, answer is: ' + j)
						found_answer=1
						break
					except:
						print('tested ' + j)
				elif usePOS:
					if found_answer == 1:
						break
					tgt_pdf.decrypt(j)
					try:
						x=tgt_pdf.getNumPages()
						print('solved, answer is: ' + j)
						found_answer=1
						break
					except:
						print('tested ' + j)
				else:
					if found_answer == 1:
						break
					tgt_pdf.decrypt(j)
					try:
						x=tgt_pdf.getNumPages()
						print('solved, answer is: ' + j)
						found_answer=1
						break
					except:
						print('tested ' + j)
	elif format == "md5":
		hashfile = open(target_file, "r")
		k = hashfile.read().strip()
#		k = fileinput.input(target_file)
		print('k is ' + k)
#		print('tested ' + j + ' which hashed to ' + rez)
		for i in fileinput.input(source_file):
			for j in nltk.word_tokenize(i):
				if useTokenize:
					rez = hashlib.md5(j).hexdigest()
					if found_answer == 1:
						break
					if k == rez:
						print('solved, answer is: ' + j)
						found_answer=1
					else:
						print('tested ' + j + ' which hashed to ' + rez)
#						print('tested ' + j + ' which hashed to ' + rez + '. vs' + k + '.')
				if useLemmatize:
					rez = hashlib.md5(j).hexdigest()
					if found_answer == 1:
						break
					if k == rez:
						print('solved, answer is: ' + j)
						found_answer=1
					else:
						print('tested ' + j + ' which hashed to ' + rez)
				elif usePOS:
					rez = hashlib.md5(j).hexdigest()
					if found_answer == 1:
						break
					if k == rez:
						print('solved, answer is: ' + j)
						found_answer=1
					else:
						print('tested ' + j + ' which hashed to ' + rez)
				else:
					pass
#					rez = hashlib.md5(j).hexdigest()
#					if found_answer == 1:
#						break
#					if k == rez:
#						print('solved, answer is: ' + j)
#						found_answer=1
#					else:
#						print('tested ' + j + ' which hashed to ' + rez)
else:
#	print 'usage: python hcrack.py target_file source_file'
	print 'usage: python hcrack.py [format] target_file [nlp options] source_file'
#	print 'Prefix and Suffix are prepended/appended respectively to every attempt, type  for empty prefix'
	print '[format] list:'
	print '		pdf'
	print '		md5'
	print '[nlp options] list:'
	print '		W	word-level tokenization'
#	print '		L	lemmatization used to find different forms of the attempted word'
#	print '		P	POS tagging will accept an additional argument at the end of the command with the first letters of noun categories of words to try. Nouns, Adjectives, Verbs supported, Adverbs using letter X'
#	print '		L	lemmatization used to find different forms of the attempted word'

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
