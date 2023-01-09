import yaml
from housing.exception import HousingException
import os,sys


def read_yaml_file(file_path:str) ->dict:
    """
    read yaml file and returns the content as dictionary
    file path:str
    """
    
    try:
        with open(config_file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise HousingException(e,sys) from e
        
    