from pypdf import PdfReader, PdfWriter

# PDF-ga parol qo'shing (shifrlash):
def encrypt(path: str, path_new: str, password: str):
    reader = PdfReader(path)
    writer = PdfWriter()

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Add a password to the new PDF
    writer.encrypt(password)

    # Save the new PDF to a file
    with open(path_new, "wb") as f:
        writer.write(f)


def main():
    p = "pdf_files\example4.pdf"
    pn = "encryption_and_decryption_of_PDFs\pdf_files\example.pdf"
    password = "12345678"
    encrypt(p, pn, password)

if __name__ == "__main__":
    main()