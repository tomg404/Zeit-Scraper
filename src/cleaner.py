# Cleans the xml-temp directory if there are files which couldn't be parsed
from os import listdir, remove, path
from src.vars import XML_DIR

def clean():
    if len(listdir(str(XML_DIR))) == 0:
        pass
    else:
        for f in listdir(str(XML_DIR)):
            remove(str(XML_DIR.joinpath(f)))
