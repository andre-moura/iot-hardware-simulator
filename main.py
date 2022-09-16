from app.iot import HardwareIoT
import sched, time
from config.configuration import INTERVAL

S = sched.scheduler(time.time, time.sleep)
if __name__ == '__main__':
    S.enter(INTERVAL, 1, HardwareIoT.read_temperature, (S,))
    S.run()