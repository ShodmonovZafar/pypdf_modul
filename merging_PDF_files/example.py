from pypdf import PdfWriter


def merging_pdf_files(merged_pdf_name: str, list_of_pdf_file_names: list[str]):
    # from pypdf import PdfWriter
    merger = PdfWriter()

    for pdf in list_of_pdf_file_names:
        merger.append(pdf)

    merger.write(merged_pdf_name)
    merger.close()

def main():
    # merging_PDF_files\\merging_pdf_files_example\\
    list_of_pdf_file_names = ["merging_PDF_files\merging_pdf_files_example\file1.pdf",
                               "merging_PDF_files\merging_pdf_files_example\file2.pdf", 
                               "merging_PDF_files\merging_pdf_files_example\file3.pdf"]
    merged_pdf_name = "merging_PDF_files\merging_pdf_files_example\merged_pdf.pdf"
    merging_pdf_files(list_of_pdf_file_names, merged_pdf_name)

if __name__ == "__main__":
    main()
