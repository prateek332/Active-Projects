from pathlib import Path
import json
import time

from Checkers.pathCheck import checkPath
#import os #Remove later

Gate_Codes = {
    'and' : ['a',1],
    'or' : ['o',1],
    'not' : ['n',1],
    'nand': ['na',1],
    'nor' : ['no',1],
    'xor' : ['xo',1],
    'xnor': ['xn',1]
}

#gate_codes_file_path = Path(str(Path.cwd()) + '/VLSI_Python/InternalWorkingScripts/Gate_Codes.json')
#os.remove(gate_codes_file_path) # Remove later

gate_codes_file_path = Path(str(Path('.').absolute()) + '/DataFiles/gate_codes.json')

def createGateCodes():
    global gate_codes_file_path

    if checkPath(gate_codes_file_path):
        checkPath(gate_codes_file_path, create_dir=True)
        print("done")
        time.sleep(5)

    try:
        with open(gate_codes_file_path,'x') as gc:
            json.dump(Gate_Codes,gc)

    except FileExistsError as e:
        print(f"Remove `Gate_Codes.json` file from: {str(gate_codes_file_path)}")
        print("Run the main_script again")
        exit()
            