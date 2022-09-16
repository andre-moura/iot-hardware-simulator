from app.enums import DateFormat, Unit
from config.connection import Connector
from config.configuration import INTERVAL, COLUMNS, TABLE
import random
from datetime import datetime

class HardwareIoT:
    def read_temperature(sc):
        temperature = "{:.2f}".format(random.uniform(21, 31))

        if HardwareIoT.break_sensor():
            date_time = 'NULL'

        if HardwareIoT.break_sensor():
            temperature = 'NULL'

        VALUES = f"{temperature}"
        Connector.insert(COLUMNS, VALUES)
        print(f'INSERT INTO {TABLE} ({COLUMNS}) \nVALUES({VALUES}) \n')
        
        sc.enter(INTERVAL, 1, HardwareIoT.read_temperature, (sc,))

    def break_sensor():
        return round(random.uniform(0, 10)) == 9