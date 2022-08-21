import sched, time
from datetime import datetime
from enums import *
import random
from date_generator import random_date
from config.connection import *

s = sched.scheduler(time.time, time.sleep)
COLUMNS  = 'temperature, unit, ocean_name, date_time'

class HardwareIoT:
    def read_temperature(sc):
        
        temperature = round(random.uniform(26, 35))
        date_time = random_date(
        "21/08/1980 13:40:41", 
        "21/08/2022 13:40:41", 
        DateFormat.DMY.value, 
        random.random()
        )
        
        VALUES = f'{temperature}, {Unit.Celsius.value}, {Ocean.SOUTHERN.value}, {date_time}'
        Connector.insert(COLUMNS, VALUES)
        # print(f'INSERT INTO tbl_temperature ({COLUMNS}) '
        #       f'VALUES({VALUES}) \n')
        
        sc.enter(4, 1, HardwareIoT.read_temperature, (sc,))

s.enter(4, 1, HardwareIoT.read_temperature, (s,))
s.run()