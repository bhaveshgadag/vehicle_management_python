import mysql.connector
from mysql.connector import Error


class Database:
    connection = None
    cursor = None

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='service_management',
                                                      user='bhavesh',
                                                      password='root')
            self.cursor = self.connection.cursor()
            print("cursor made")
        except Error as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.connection.close()
        print("connection closed")