from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from titanic.logging import logger
import os

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads the yaml file and returns the config box for the content of the file

    Agrs:
        path_to_yaml (str) : path like input

    Raises:
        ValuesError: if the yaml file is empty
        e: Empty File

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError('yaml file is empty')
    
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_dir:list, verbose=True):
    """
    create list of directories

    Args:
        path_to_dir (list): lost of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False

    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
        
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"