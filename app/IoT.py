import sched, time
from enums import *
import random
from date_generator import random_date
import sys
sys.path.insert(0, 'C:\\Users\\pc\\OneDrive\\Documentos\\IoT-hardware-simulator\\config\\')
from connection import Connector
from config import *

S = sched.scheduler(time.time, time.sleep)

class HardwareIoT:
    def read_temperature(sc):
        
        temperature = "{:.2f}".format(random.uniform(26, 35))

        date_time = random_date(
            "21/08/1980 13:40:41", 
            "21/08/2022 13:40:41", 
            DateFormat.DMY.value, 
            random.random()
        )

        if HardwareIoT.break_sensor():
            date_time = 'NULL'

        if HardwareIoT.break_sensor():
            temperature = 'NULL'

        VALUES = f"{temperature}, '{Unit.Celsius.value}', '{Ocean.PACIFIC.value}', '{date_time}'"
        Connector.insert(COLUMNS, VALUES)
        print(f'INSERT INTO tbl_temperature ({COLUMNS}) VALUES({VALUES}) \n')
        
        sc.enter(INTERVAL, 1, HardwareIoT.read_temperature, (sc,))

    def break_sensor():
        return round(random.uniform(0, 10)) == 9