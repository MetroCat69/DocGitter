import mammoth

def convert_docx_to_markdown(input_file_path,output_file_path):

    with open(input_file_path, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
        markdown = result.value

    with open(output_file_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown)