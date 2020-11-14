from InternalWorkingScripts.Components.ComponentsCreator import createComponents_txt
from ChangeDetectors.components_txt_detect import MonitorComponentsChanges
from InternalWorkingScripts.Gates.GateCodesGenerator import createGateCodes
import time

from pathlib import Path
import os


if __name__ == '__main__':
    createComponents_txt()
    MonitorComponentsChanges()
    #createGateCodes()
    pass
