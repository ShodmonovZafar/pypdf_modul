from pypdf import PdfReader

reader = PdfReader("pdf_files\example4.pdf")

def f():
    for name, content_list in reader.attachments:
        for i, content in enumerate(content_list):
            with open(f"{name}-{i}", "wb") as fp:
                fp.write(content)
    

def main():
    f()

if __name__ == "__main__":
    main()
