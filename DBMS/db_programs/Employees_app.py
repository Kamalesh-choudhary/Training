import pymysql
import db_connect2 as dbc2
import sys

def create_db():
    query = 'create database if not exists Kamal_DB'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Databsase created successfully')
        else:
            print('Databsase already exists')
    except Exception as e:
        print('Error while creating the database : ',e)

def create_table():
    #query = 'create table if not exists in Employees(id int primary key auto_increment, name varchar(255) not null, age int, department varchar(255),designation varchar(255), salary float, comission float default 0, years_of_experience tinyint, phone_no bignint unique)'
    query = 'create table if not exists employees(id int primary key auto_increment, name varchar(255) not null,age int not null, salary float, phone_number bigint unique)'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        cursor.close()
        #connection.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Table created successfully')
        else:
            print('Table already exists')
    except Exception as e:
        print('Error while creating the Table : ',e)

def insert_into_emp():
    query = 'insert into employees(name, age, salary, phone_number) values(%s, %s, %s, %s)'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        salary = float(input('Enter salary: '))
        phone = int(input('Enter phone: ')) 
        values = (name, age, salary, phone)
        result = cursor.execute(query, values)
        connection.commit()
        cursor.close()
        dbc2.db_disconnect(connection)
        if result == 1:
            print('Record inserted')
        else:
            print('Record insertion failed')
    except Exception as e:
        print('Record insertion failed', e)

def update_employee_salary():
    query = 'update employees set salary = %s where id = %s;'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        id = input('Enter employee id to update salary: ')
        salary = float(input('Enter new salary: '))
        values = (salary, id)
        result = cursor.execute(query, values)
        connection.commit()
        if result == 1:
            print('Salary updated')
        else:
            print('Salary update failed')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Salary update failed', e)

def delete_employee():
    query = 'delete from employees where id = %s;'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        id = input('Enter employee id to delete: ')
        value = (id,)
        result = cursor.execute(query, value)
        connection.commit()
        if result == 1:
            print('Employee deleted')
        else:
            print('Employee deletion failed')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Employee deletion failed', e)

def search_employee():
    query = 'select * from employees where id = %s;'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        name = input('Enter id to search: ')
        value = (name,)
        cursor.execute(query, value)
        result = cursor.fetchone()
        if result is not None:
            print('Employee found: ', result)
        else:
            print('Employee not found')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Search failed', e)

def list_all_employees():
    query = 'select * from employees;'
    try:
        connection = dbc2.db_connect()
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            print('-'*60)
            print('%-5s %-20s %-5s %-10s %-15s'%('Id','Name','Age','Salary','Phone Number'))
            print('-'*60)
            for row in results:
                print('%-5s %-20s %-5s %-10s %-15s'%(row[0], row[1], row[2], row[3], row[4]))
            print('-'*60)
        else:
            print('No employees found')
        cursor.close()
        dbc2.db_disconnect(connection)
    except Exception as e:
        print('Failed to list employees', e)

def menu(choice):
    match choice:
        case 1:
            insert_into_emp()
        case 2:
            update_employee_salary()
        case 3:
            delete_employee()
        case 4:
            search_employee()
        case 5:
            list_all_employees()
        case 6:
            sys.exit("End of the Execution")
        case _:
            print("Invalid choice")
            
def run_employee_app():
    while True:
        print('1. Insert Employee')
        print('2. Update Employee salary')
        print('3. Delete Employee')
        print('4. Search Employee')
        print('5. List all Employees')
        print('6. Exit')
        choice = int(input('Enter your choice: '))
        menu(choice)
        
create_db()
create_table()
run_employee_app()

