import os
from git import Repo
import git
import logging
from config import update_glitter_config, glitter_init,get_glitter_dir_path,get_glitter_config
from exception import ProjectExistsError
import shutil
from file_conversion_handler import convert_files
from typing import List,Tuple
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_glitter_exists_and_eror():
    glitter_path = get_glitter_dir_path()
    if not os.path.exists(glitter_path):
        logger.error(f"No Glitter dir exists please create a project or init first")
        return True
    else:
        return False



def create_new_project_from_remote_url(remote_url: str) -> str:
    glitter_path = get_glitter_dir_path()
    project_name = remote_url.split('/')[-1].split('.')[0]
    project_dir = os.path.join(glitter_path, project_name)
    config = get_glitter_config()

    if os.path.exists(project_dir):
        logger.warning(f"Project '{project_name}' already exist. at {project_dir}")
        return None
    if not os.path.exists(glitter_path):
        glitter_init()
    
    Repo.clone_from(remote_url, project_dir)

    projects_value = config['projects']
    projects_value[project_name] = {'remote_url': remote_url}

    update_glitter_config('projects',projects_value)
    update_glitter_config('current project',project_name)
    
    logger.info("New project directory created at: %s", project_dir)
    logger.info("Remote repository with URL: %s", remote_url)
    return project_dir


def delete_project_and_remove_config(project_name: str) -> None:
    glitter_path = get_glitter_dir_path()
    project_dir = os.path.join(glitter_path, project_name)

    if not os.path.exists(project_dir):
        logger.error(f"Project '{project_name}' does not exist.")
        return 

    try:
        shutil.rmtree(project_dir)
        logger.info(f"Project directory '{project_dir}' has been deleted.")
    except Exception as e:
        logger.error(f"Failed to delete project directory '{project_dir}': {e}")
        return

    # Update the Glitter configuration
    try:
        config = get_glitter_config()

        projects = {key: value for key, value in config['projects'].items() if key != project_name}
        update_glitter_config('projects',projects)

        if config.get('current project','') == project_name:
            update_glitter_config('current project','none')

        logger.info(f"Project '{project_name}' has been removed from the Glitter configuration.")
    except Exception as e:
        logger.error(f"Failed to update Glitter configuration: {e}")


def list_created_projects() -> Tuple[str,List[str]]:
     
    if check_glitter_exists_and_eror():
        return None,None
    
    config = get_glitter_config()
    projects = [p for p in config['projects'].keys()]
    current_project =  config.get('current project', 'none')     
    return current_project,projects


def add_and_update_files(input_path):
    """
    I know if a file was delete I will add it and if it changed path I want removed the og one. this is by design
    """
    
    if check_glitter_exists_and_eror():
        return 
        
    config = get_glitter_config()

    if config['current project'] == 'none':
        logger.error('no current project set')
        return
    
    current_project = config['current project']
    project_name = current_project

    glitter_path = get_glitter_dir_path()
    output_path = os.path.join(glitter_path, project_name)
    
    convert_files(input_path, output_path)
   
    repo = Repo(output_path)

    try:
        repo.git.add(A=True)
        repo.index.commit("Updated files")
        origin = repo.remote(name='origin')
        origin.push()
    except git.exc.GitCommandError as e:
        logger.error("Error occurred while processing Git commands: %s", e)

def move_current_project(project_name):

    if check_glitter_exists_and_eror():
        return 

    config = get_glitter_config()

    if project_name not in config['projects'].keys():
        logger.error('''project name doesn't exist try creating new project''')

    if config['current project'] == project_name:
        return
    update_glitter_config('current project',project_name)
    