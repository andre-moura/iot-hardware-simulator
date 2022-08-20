import mysql.connector
from config import config

class Connector:

    def insert(values):
        Connector.connect()

        insert_temperature = ('INSERT INTO tbl_temperature (date_time, ocean_name, temperature, unit)'
                              'VALUES (%s, %s, %s, %s)')
        cursor.execute(insert_temperature, values)

        Connector.commit()

    def connect():
        global cnx 
        global cursor

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

    def commit():
        cnx.commit()
        cursor.close()
        cnx.close()