import fitz
from docx import Document

pdf_path = "sample.pdf"
docx_path = "output.docx"

# PDF aç
doc = fitz.open(pdf_path)
word_doc = Document()

for page in doc:
    text = page.get_text("text")
    word_doc.add_paragraph(text)

word_doc.save(docx_path)
print(f"{docx_path} başarıyla oluşturuldu")
