from Checkers.modify_check import ifModified
from concurrent.futures import ProcessPoolExecutor as pool
from InternalWorkingScripts.Components.ComponentsCreator import fileMaker
from InternalWorkingScripts.Components.ComponentsCreator import comp_path
from InternalWorkingScripts.Components.ComponentsParser import parseComponents
from InternalWorkingScripts.PopUpMessage.popUp import popUp

# Path to components.txt
filepath = comp_path

def content_length(filepath):
    with open(filepath, 'r') as fp:
        length = len(fp.read())
    return length

def detect_change(filepath):
    change = ifModified(filepath)
    return change

def stopMonitoringCallback():
    print("Stopping Monitoring of 'UserFiles/components.txt'")

def MonitorComponentsChanges():
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
                    print('`components.txt` modified, parsing components')
                    parseComponents()
    
                elif file_size == new_length: # No changes in the file contents
                    continue

                else:
                    # Creates file again, if new_length < original file_size
                    print('`components.txt` contents found wrong. Creating the file again.')
                    popUp("`Components.txt` Created Again", "`Components.txt` file contents were found wrong. File created again.")
                    fileMaker()
        changed.add_done_callback(MonitorComponentsChanges)
        changed.cancel()
        
            
        
    


