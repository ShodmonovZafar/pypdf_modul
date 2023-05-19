from pypdf import PdfReader

reader = PdfReader("example3.pdf")

page = reader.pages[72]
count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1