from pypdf import PdfReader, PdfWriter

def decrypt(path: str, path_new: str, password: str):
    reader = PdfReader(path)
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt(password)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open(path_new, "wb") as f:
        writer.write(f)

def f(p: str, pdf_file: str):
    a = p.split("\\")
    del a[-1]
    a.append(pdf_file)
    b = "\\".join(a)
    return b

def main():
    p = __file__
    x = f(p, "pdf_files\\example.pdf")
    y = f(p, "pdf_files\\new.pdf")
    decrypt(x, y, "12345678")

if __name__ == "__main__":
    main()
    