import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user = 'root',
            password = '',
        )
        if connection.is_connected():
            print('Connection Success')
            return connection

    except Error as e:
        print (f"Error '{e}'")
        return None
        