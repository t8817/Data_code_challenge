# my sql connect
import mysql.connector
#csv reader
import csv

try:
    connection = mysql.connector.connect(host='localhost', database="companyabc", user='root', password='root')
    cursor = connection.cursor(prepared=True)
    cursor.execute("""
                    create table updated_salaries(
                        emp_id int primary key, 
                        updated_salary int   
                    )
                    """)
    insertStmt = """ INSERT INTO updated_salaries
                       (emp_id, updated_salary) VALUES (%s,%s)"""
    cursor.execute("select emp_id, salary, salary_increment from employee")
    for empData in cursor.fetchall():
      updatedSalary = (empData[2]*empData[1]/100) + empData[1]
      cursor.execute(insertStmt, [empData[0], updatedSalary])
    connection.commit()
except Exception as error:
    print(error)
