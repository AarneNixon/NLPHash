# NLPHash
Using Natural Language Processing tools to aid password recovery across formats and circumstances. (incomplete)

# Dependencies

PyPDF2, nltk. Both available via pip.

# Descriptions

encrypt_pdf.py is a tool made available for testing purposes. It will add a password to a pdf named output.pdf within the same directory.
hcrack.py is the tool itself. Absent any arguments, it will inform you of proper usage.

# Test
  Once you have python ready, pip installed the dependencies and the files downloaded into one directory, the test command using word-tokenization to search for a one-word password is:
  
  python hcrack.py output.pdf possible_passwords
