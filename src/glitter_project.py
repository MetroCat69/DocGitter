import os
from git import Repo
import git
import logging
from config import update_glitter_config, glitter_init,get_glitter_config_path,get_glitter_config_data
from exception import ProjectExistsError
import shutil
from file_conversion_handler import convert_files
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_new_project_from_remote_url(remote_url: str, glitter_project_path: str) -> str:
    project_name = remote_url.split('/')[-1].split('.')[0]
    project_dir = os.path.join(glitter_project_path, project_name)
    config_path = get_glitter_config_path(glitter_project_path)

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
    config_path = get_glitter_config_path(glitter_project_path)

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
        config = get_glitter_config_data(config_path)

        projects = {key: value for key, value in config['projects'].items() if key != project_name}
        update_glitter_config(config_path,'projects',projects)

        logger.info(f"Project '{project_name}' has been removed from the Glitter configuration.")
    except Exception as e:
        logger.error(f"Failed to update Glitter configuration: {e}")

def list_created_projects(glitter_project_path: str):
     config_path = get_glitter_config_path(glitter_project_path)
     config = get_glitter_config_data(config_path)
     return [p for p in config['projects'].keys()]





def add_and_update_files(input_path, project_name, glitter_project_path):

    output_path = os.path.join(glitter_project_path, project_name)
    convert_files(input_path, output_path)
   
       # Initialize Git repository
    repo = Repo(output_path)

    try:
        # Add changes
        repo.git.add(A=True)
        # Commit changes
        repo.index.commit("Updated files")
        # Push changes to remote
        origin = repo.remote(name='origin')
        origin.push()
    except git.exc.GitCommandError as e:
        logger.error("Error occurred while processing Git commands: %s", e)