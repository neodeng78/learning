"""

读取PDF文件

Version: 0.1
Author: Neo


"""
#import PyPDF2
from PyPDF2 import PdfFileReader

with open('./upintheair.pdf', 'rb') as f:
	reader = PdfFileReader(f, strict=False)
	print(reader.numPages)
	if reader.isEncrypted:
		reader.decrypt('')
	current_page = reader.getPage(5)
	print(current_page)
	print(current_page.extractText())
	#print(pdfFileReader.numPages)

f.close()
