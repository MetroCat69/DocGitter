import os
from file_convertors.docs_convertor import convert_docx_to_markdown

conversion_config_dict = {".docx": convert_docx_to_markdown}


def convert_files(input_path, output_path):
    for root, _, files in os.walk(input_path):
        for file in files:

            input_file_path = os.path.join(root, file)
            relative_output_path = os.path.relpath(input_file_path, input_path)
            output_file_path = os.path.join(output_path, relative_output_path)

            conversion_func = conversion_config_dict.get(
                os.path.splitext(input_file_path)[1]
            )

            if conversion_func:

                output_file_dir = os.path.dirname(output_file_path)
                output_file_basename = os.path.splitext(
                    os.path.basename(output_file_path)
                )[0]
                output_file_path = os.path.join(output_file_dir, output_file_basename)

                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)

                if os.path.exists(output_file_path):
                    os.remove(output_file_path)

                conversion_func(input_file_path, output_file_path)
