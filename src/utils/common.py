import os 
from src.logging.logging import Logger
from src.exception.exception import CustomException
from pathlib import Path
# from ensure import ensure_annotations
import yaml
from dotmap import DotMap



#read Yaml file
# @ensure_annotations
def read_yaml(filepath:Path):
    with open(filepath,"r") as f:
        data=yaml.safe_load(f)
        Logger.info("Yaml file has been read Successfully...")
        filedata=DotMap(data)
        return filedata
    


## make the directory and files
# @ensure_annotations
def make_dir(filepath:Path):
    dirpath,file_name=os.path.split(filepath)
    os.makedirs(dirpath,exist_ok=True)
    Logger.info(f"New Directory has been created on the Location {dirpath}.")
    

