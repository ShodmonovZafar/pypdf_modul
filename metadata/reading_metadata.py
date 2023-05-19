from pypdf import PdfReader

reader = PdfReader("metadata\example.pdf")

meta = reader.metadata

print("Number of Pages: ", len(reader.pages))

# All of the following could be None!
print("Author: ", meta.author)
print("Creator: ", meta.creator)
print("Producer: ", meta.producer)
print("Subject: ", meta.subject)
print("Title: ", meta.title)