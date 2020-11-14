from Checkers.modify_check import ifModified
from concurrent.futures import ProcessPoolExecutor as pool
from InternalWorkingScripts.Components.ComponentsCreator import fileMaker
from InternalWorkingScripts.Components.ComponentsCreator import comp_path

# Path to components.txt
filepath = comp_path

def content_length(filepath):
    with open(filepath, 'r') as fp:
        length = len(fp.read())
    return length

def detect_change(filepath):
    change = ifModified(filepath)
    return change

def ifCompChanged():
    '''Contineuously Monitor `components.txt` file for changes and take appropriate actions'''

    global filepath

    # Getting default user help message size
    file_size = content_length(filepath)

    with pool(max_workers=1) as p:
        while True:
            changed = p.submit(detect_change(filepath))
            
            if changed:
                # Get changes length
                new_length = content_length(filepath)

                if file_size < new_length: # Gates info added
                    print('`components.txt` modified')
                    # Add code to generate Netlist
    
                elif file_size == new_length: # No changes in the file contents
                    continue

                else:
                    # Creates file again, if new_length < original file_size
                    print('`components.txt` contents found wrong. Creating the file again.')
                    fileMaker()
            
            
        
    


