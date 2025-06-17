import fitz  # PyMuPDF
import docx2txt

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text(file_path, file_type):
    if file_type == 'pdf':
        return extract_text_from_pdf(file_path)
    elif file_type == 'docx':
        return extract_text_from_docx(file_path)
    elif file_type == 'txt':
        with open(file_path, 'r') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")
