import pymysql

def db_connect():
    connection = 1
    try:
        connection = pymysql.connect(user = 'root', password = 'root', port = 3306,database = 'Kamal_DB', charset = 'utf8', host = 'localhost')
        print("Data Base connected....")
    except Exception as e:
        print('DataBase connection failed')          

    return connection

def db_disconnect(connection):
    try:
        connection.close();
        print("Database disconnected...")
    except:
        print("Database disconnection Failed.....")

connection = db_connect()
db_disconnect(connection)

