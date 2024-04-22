import os
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

home_dir = os.path.expanduser("~")
glitter_dir = os.path.join(home_dir, ".glitter")
glitter_config_file_path = os.path.join(glitter_dir, "glitter_config.json")
cache_dir = os.path.join(glitter_dir, ".glitter_cache")


def create_glitter_dir() -> str | os.PathLike:
    if not os.path.exists(glitter_dir):
        os.makedirs(glitter_dir)
        os.makedirs(cache_dir)
    return glitter_dir


def create_glitter_config() -> str | os.PathLike:

    config_data = {
        'projects':{}
    }
    
    with open(glitter_config_file_path, 'w') as file:
        json.dump(config_data, file)
    
    return glitter_config_file_path

def update_glitter_config( key: str, value:any) -> None:
    
    with open(glitter_config_file_path, 'r') as file:
            config_data = json.load(file)
    
    config_data[key] = value
    
    with open(glitter_config_file_path, 'w') as file:
        json.dump(config_data, file, indent=4)

def get_glitter_config() -> dict:
    with open(glitter_config_file_path, 'r') as file:
            config_data = json.load(file)
    return config_data

def get_glitter_dir_path():
     return glitter_dir


def glitter_init() -> None:
    create_glitter_dir()
    config_file_path = create_glitter_config(glitter_dir)
    logger.info("Glitter directory created at: %s", glitter_dir)
    logger.info("Glitter config file created at: %s", config_file_path)
