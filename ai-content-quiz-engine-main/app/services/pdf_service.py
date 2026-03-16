import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)

    full_text = ""

    for page in doc:
        text = page.get_text()
        full_text += text + "\n"

    doc.close()

    return full_text