from pypdf import PdfReader


def f():
    reader = PdfReader("pdf_files\example4.pdf")
    page_index = 0
    for page in reader.pages:
        count = 0
        for image_file_object in page.images:
            with open("extract_images\images\page{}_image{}_{}".format(page_index,
                                                                        count,
                                                                        image_file_object.name), "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
        page_index += 1
    

def main():
    f()

if __name__ == "__main__":
    main()