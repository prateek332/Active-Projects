from InternalWorkingScripts import filePath
from Checkers import ifModified
from InternalWorkingScripts import parse_all_nets

from time import sleep

filepath = filePath().netlist_txt_path()

def detect_change(filepath):
    change = ifModified(filepath)
    return change


def MonitorNetlistChanges():
    '''Continuously Monitor `netlist.txt` file for changes and take appropriate actions'''

    global filepath

    while True:
        changed = detect_change(filepath)
        if changed:
            parse_all_nets()
        else:
            sleep(1)
