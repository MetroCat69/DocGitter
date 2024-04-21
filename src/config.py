import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_glitter_dir() -> str | os.PathLike:
    home_dir = os.path.expanduser("~")
    glitter_dir = os.path.join(home_dir, ".glitter")
    cache_dir = os.path.join(glitter_dir, ".glitter_cache")

    if not os.path.exists(glitter_dir):
        os.makedirs(glitter_dir)
        os.makedirs(cache_dir)
    return glitter_dir


def create_glitter_config(dir_path: str | os.PathLike) -> str | os.PathLike:
    file_name = "glitter_config.json"
    file_path = os.path.join(dir_path, file_name)
    config_data = {
        'projects':{}
    }
    
    with open(file_path, 'w') as file:
        json.dump(config_data, file)
    
    return file_path

def update_glitter_config(config_file_path: str | os.PathLike, key: str, value:any) -> None:
    project_name = remote_url.split('/')[-1].split('.')[0]
    
    with open(config_file_path, 'r') as file:
            config_data = json.load(file)
    
    config_data[key] = value
    
    with open(config_file_path, 'w') as file:
        json.dump(config_data, file, indent=4)

def get_glitter_config_data(config_file_path: str | os.PathLike) -> dict:
    with open(config_file_path, 'r') as file:
            config_data = json.load(file)
    return config_data



def get_glitter_config_path(dir_path):
    return os.path.join(dir_path, "glitter_config.json")


def glitter_init() -> None:
    glitter_dir = create_glitter_dir()
    config_file_path = create_glitter_config(glitter_dir)
    logger.info("Glitter directory created at: %s", glitter_dir)
    logger.info("Glitter config file created at: %s", config_file_path)
