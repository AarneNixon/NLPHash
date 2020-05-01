# NLPHash
Using Natural Language Processing tools to aid password recovery across formats and circumstances. (incomplete)

# Dependencies

PyPDF2, nltk, passlib, bcrypt, numpy. All are available via pip.

# Descriptions

encrypt_pdf.py is a tool made available for testing purposes. It will add a password to a pdf named output.pdf within the same directory.
hcrack.py is the tool itself. Absent any arguments, it will inform you of proper usage.

# Test
  Once you have python ready, pip installed the dependencies and the files downloaded into one directory, the test command using word-tokenization to search for a one-word password to a pdf is:
  
	python hcrack.py pdf output.pdf W possible_passwords

  The test command for md5 and sha hashes:

	python hcrack.py md5 md5hash W possible_passwords
	python hcrack.py sha512 sha512hash W possible_passwords
	python hcrack.py sha256 sha256hash W possible_passwords

  The test command for named entity recognition (only making attempts from names of people/organizations/etc from target file)

	python hcrack.py sha256 sha256hashNER NW namedEntity
