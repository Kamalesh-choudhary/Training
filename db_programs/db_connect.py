import pymysql

connection = pymysql.connect(user = 'root', password = 'root', port = 3306,database = 'Kamal_DB', charset = 'utf8', host = 'localhost')
print("Data Base connected....")

connection.close()
print("Data Base disconnected....")
