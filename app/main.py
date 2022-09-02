from IoT import HardwareIoT
import sched, time

import sys
sys.path.insert(0, 'C:\\Users\\pc\\OneDrive\\Documentos\\IoT-hardware-simulator\\config\\')
from config import *

S = sched.scheduler(time.time, time.sleep)

if __name__ == '__main__':
    S.enter(INTERVAL, 1, HardwareIoT.read_temperature, (S,))
    S.run()