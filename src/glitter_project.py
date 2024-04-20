import os
from git import Repo
import logging
from config import update_glitter_config, glitter_init,glitter_config_path
from exception import ProjectExistsError
import mammoth
import shutil
import json
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_new_project_from_remote_url(remote_url: str, glitter_project_path: str) -> str:
    project_name = remote_url.split('/')[-1].split('.')[0]
    project_dir = os.path.join(glitter_project_path, project_name)
    config_path = glitter_config_path(glitter_project_path)

    if os.path.exists(project_dir):
        logger.warning(f"Project '{project_name}' already exist. at {project_dir}")
        return None
    if not os.path.exists(glitter_project_path):
        glitter_init()
    
    Repo.clone_from(remote_url, project_dir)
    update_glitter_config(config_path, remote_url)
    
    logger.info("New project directory created at: %s", project_dir)
    logger.info("Remote repository with URL: %s", remote_url)
    return project_dir


def delete_project_and_remove_config(project_name: str, glitter_project_path: str):
    project_dir = os.path.join(glitter_project_path, project_name)
    config_path = glitter_config_path(glitter_project_path)

    if not os.path.exists(project_dir):
        logger.warning(f"Project '{project_name}' does not exist.")
        return None

    try:
        shutil.rmtree(project_dir)
        logger.info(f"Project directory '{project_dir}' has been deleted.")
    except Exception as e:
        logger.error(f"Failed to delete project directory '{project_dir}': {e}")
        return

    # Update the Glitter configuration
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)

        config['projects'] = {key: value for key, value in config['projects'].items() if key != project_name}

        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        logger.info(f"Project '{project_name}' has been removed from the Glitter configuration.")
    except Exception as e:
        logger.error(f"Failed to update Glitter configuration: {e}")

def list_created_projects(glitter_project_path: str):
     config_path = glitter_config_path(glitter_project_path)
     with open(config_path, 'r') as f:
            config = json.load(f)
     return [p for p in config['projects'].keys()]





def convert_docx_to_md(input_path,saved_file_path):
    # Create the cache directory if it doesn't exist
    cache_dir = Path.home() / ".glitter"
    cache_dir.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(input_path):
        # Create the corresponding directory structure in the cache
        relative_path = os.path.relpath(root, input_path)
        cache_root = cache_dir / relative_path

        # Create the directory if it doesn't exist
        cache_root.mkdir(parents=True, exist_ok=True)

        for file in files:
            if file.endswith(".docx"):
                input_file = os.path.join(root, file)
                output_file = os.path.join(cache_root, os.path.splitext(file)[0] + ".md")

                # Convert the .docx file to Markdown
                with open(input_file, "rb") as docx_file:
                    result = mammoth.convert_to_markdown(docx_file)
                    markdown = result.value

                # Save the Markdown content to a file
                with open(output_file, "w", encoding="utf-8") as md_file:
                    md_file.write(markdown)

                print(f"Converted {input_file} to {output_file}")