import os.path
from pathlib import Path
import yaml
import base64
from yoloDetector import logger
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml_file(file_path: Path) -> ConfigBox:
    try:
        with open(file_path, "rb") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logger.info(f"yaml file: {file_path} saved successfully")

    except Exception as e:
        logger.exception(e)
        raise e
    

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

    
    