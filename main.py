from app.IoT import HardwareIoT
from config.configuration import INTERVAL
import time

if __name__ == '__main__':
    print('Reading temperature...\n')

    while True:
        HardwareIoT.read_temperature()
        time.sleep(INTERVAL)