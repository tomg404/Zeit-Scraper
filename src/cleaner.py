# Cleans the xml-temp directory if there are files which couldn't be parsed
from os import listdir, remove, path
from src.vars import XML_DIR

def clean():
    if len(listdir(XML_DIR)) == 0:
        pass
    else:
        for f in listdir(XML_DIR):
            remove(path.join(XML_DIR, f))
