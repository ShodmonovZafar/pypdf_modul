from pypdf import PdfReader, PdfWriter

reader = PdfReader("metadata\example.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add the metadata
writer.add_metadata(
    {
        "/Author": "Shodmonov Zafar",
        "/Producer": "Shodmonov Zafar",
    }
)

# Save the new PDF to a file
with open("metadata\meta-pdf.pdf", "wb") as f:
    writer.write(f)