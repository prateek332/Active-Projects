import os, time
from pathlib import Path
from Checkers.pathCheck import checkPath
from concurrent.futures import ThreadPoolExecutor as pool


# Components.txt file path for creation, for user interactions
comp_path = Path(str(Path('.').absolute()) + '/UserFiles/components.txt')

sample_data_mssg = "" # Will save sample_data text

def components_mssg_find():
    global sample_data_mssg
    comp_mssg_path = Path(str(Path('.').absolute()) + '/DataFiles/comp_mssg.txt')
    print(comp_mssg_path)
    if Path.exists(comp_mssg_path):
        with open(comp_mssg_path,'r') as cm:
            sample_data_mssg = cm.read()
    else:
        print("File 'DataFiles/comp_mssg.txt' is missing or corrupt. Please reinstall the program.")
        exit()

def fileMaker():
    global sample_data_mssg
    # Create File Path, if it doesn't exists
    if Path.exists(comp_path):
        pass
    else:
        checkPath(comp_path, True)
    with open(comp_path,'w') as cp:
        cp.writelines(sample_data_mssg)


def createComponents_txt():
    # Find components sample message
    components_mssg_find()
    # Creates `components.txt`
    fileMaker()
    print("'UserFiles/components.txt' created. Open it for furthur instructions.")

    