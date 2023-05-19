from pypdf import PdfReader

reader = PdfReader("example.pdf")
page = reader.pages[0]
#print(page.extract_text())

# extract only text oriented up
#print(page.extract_text(0))

# extract text oriented up and turned left
print(page.extract_text())