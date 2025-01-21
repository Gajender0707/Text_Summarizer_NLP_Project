import os 
from pathlib import Path


list_of_files=[
    "src/__init__.py",

    #Logger and Exception
    "src/logging/__init__.py",
    "src/logging/logging.py",
    "src/exception/__init__.py",
    "src/exception/exception.py",

    #utils
    "src/utils/__init__.py",
    "src/utils/common.py",

    "params.yaml",
    "Dockerfile",
    
]

for files in list_of_files:
    files=Path(files)
    dirname,filename=os.path.split(files)


    if dirname!="":
        os.makedirs(dirname,exist_ok=True)

    if (not os.path.exists(files)) or (os.path.getsize(files)==0):
        with open(files,"w") as f:
            pass



    