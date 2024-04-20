import os
from git import Repo
import logging
from src.config import update_glitter_config, glitter_init

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_new_project_from_remote_url(remote_url: str, glitter_project_path: str) -> str:
    project_name = remote_url.split('/')[-1].split('.')[0]
    project_dir = os.path.join(glitter_project_path, project_name)
    
    if not os.path.exists(project_dir):
        glitter_init()
    
    Repo.clone_from(remote_url, project_dir)
    update_glitter_config(os.path.join(project_dir, "glitter_config.json"), remote_url)
    
    logger.info("New project directory created at: %s", project_dir)
    logger.info("Remote repository with URL: %s", remote_url)
    return project_dir