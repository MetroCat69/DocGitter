import os
import tempfile
from src.file_convertors.docs_convertor import convert_docx_to_markdown
from docx import Document

def test_convert_docx_to_markdown():
    temp_dir = tempfile.TemporaryDirectory()
    input_file_path = os.path.join(temp_dir.name, "input.docx")
    output_file_path = os.path.join(temp_dir.name, "output.md")

    doc = Document()

    doc.add_paragraph("Sample docx content")

    doc.save(input_file_path)

    convert_docx_to_markdown(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.getsize(output_file_path) > 0

    with open(output_file_path, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()
        assert md_content.strip() == "Sample docx content"
