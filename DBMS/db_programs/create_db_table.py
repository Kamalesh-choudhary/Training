import pymysql
import db_connect2 as dbc

def create_db():
    query = 'create database if not exists Kamal_DB'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Databsase created successfully')
        else:
            print('Databsase already exists')
    except Exception as e:
        print('Error while creating the database : ',e)

def create_table():
    #query = 'create table if not exists in Employees(id int primary key auto_increment, name varchar(255) not null, age int, department varchar(255),designation varchar(255), salary float, comission float default 0, years_of_experience tinyint, phone_no bignint unique)'
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null,designation varchar(255), salary float, phone_no bigint unique)'
    try:
        connection = dbc.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc.db_disconnect(connection)
        if result == 1:
            print('Table created successfully')
        else:
            print('Table already exists')
    except Exception as e:
        print('Error while creating the Table : ',e)

create_db()
create_table()
