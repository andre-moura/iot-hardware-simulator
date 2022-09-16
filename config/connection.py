import mysql.connector
from config.configuration import CONFIG, TABLE

class Connector:

    def insert(columns, values):
        if values and columns:
            Connector.connect()
            insert_temperature = (f'INSERT INTO {TABLE} ({columns}) '
                                   f'VALUES({values})')
            cursor.execute(insert_temperature)
            Connector.commit()

    def connect():
        global cnx 
        global cursor

        cnx = mysql.connector.connect(**CONFIG)
        cursor = cnx.cursor()

    def commit():
        cnx.commit()
        cursor.close()
        cnx.close()