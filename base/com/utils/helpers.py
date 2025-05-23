import os
import fitz

def extract_text_from_pdf(file_path):
    print("file is ", file_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return ""
    
    doc = fitz.open(file_path)
    text = ""

    for page_number in range(len(doc)):
        page = doc[page_number]
        text += page.get_text()

    doc.close()
    return text