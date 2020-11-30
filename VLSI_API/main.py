from InternalWorkingScripts import createComponents_txt
from ChangeDetectors import MonitorComponentsChanges
from InternalWorkingScripts import createGateCodes
from InternalWorkingScripts import parse_all_nets
from ChangeDetectors import MonitorNetlistChanges

from concurrent.futures import ProcessPoolExecutor as pool
from multiprocessing import cpu_count
import time

if __name__ == '__main__':
    createComponents_txt()

    with pool(max_workers=cpu_count()) as p:
        p.submit(MonitorComponentsChanges)
        p.submit(MonitorNetlistChanges)

    