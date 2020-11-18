from pathlib import Path
from os import rmdir
from shutil import rmtree

def checkPath(filepath, create_dir = False):
    '''Checks if a filepath exists, returns `True` if does, otherwise `False`.
     Creates filepath directory (not the file) if 2nd optional argument set `True` & returns `None`'''
    if type(filepath) is str:
        filepath = Path(filepath)
    if not create_dir:
        print(filepath)
        if Path.exists(filepath):
            return True
        else:
            return False
    else:
        if Path.exists(filepath):
            rmtree(filepath)
        Path.mkdir(filepath.parent)
