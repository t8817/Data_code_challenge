# my sql connect
import mysql.connector
#csv reader
import csv

try:
    connection = mysql.connector.connect(host='localhost', database="companyabc", user='root', password='root')
    cursor = connection.cursor(prepared=True)
    cursor.execute("""
                    create table employee(
                        emp_id int auto_increment primary key,
                        first_name text,
                        last_name text,
                        salary int,
                        dept_name text,
                        salary_increment int   
                    )
                    """)
    insertStmt = """ INSERT INTO employee
                       (first_name, last_name, salary, dept_name, salary_increment) VALUES (%s,%s,%s,%s, %s)"""
    with open("flat_data.csv") as flatData:
        flatDataReader = csv.reader(flatData, delimiter=",")
        k = 0
        for row in flatDataReader:
            if(k!=0):
                cursor.execute(insertStmt, row)
            k+=1
    connection.commit()
except Exception as error:
    print(error)
