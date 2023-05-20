import pdfplumber

def f(path: str):
    
    with pdfplumber.open(path) as f:

        for page in f.pages:
            print(page.extract_tables())
    

def main():
    path = "pdf_files\example5.pdf"
    f(path)

if __name__ == "__main__":
    main()