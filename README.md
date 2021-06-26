# Data_code_challenge
•	At ABC Company, each year every employee is given a percentage-based increment to their salaries based on the departments they belong to. 
•	You must write a script(s) using a scripting language (for example Python) to read from flat_data.csv and store into employees and department DB tables in the schema below.
Furthermore, you need to read tables from the database, calculate the updated salaries and write them back. Please note that you will need to create these tables using script or DDL and provide your code.

The database contains the following schemas:
     
employee: id: UUID, 
first name: Text, 
last name: Text, 
salary: numeric, 
department id: UUID, 
name: Text, 
salary increment: numeric
    
The salary increment column in department contains the percentage value for calculating the salary. 
The output of the process should be the following table

updated salaries: employee, updated salary.

All the tables must be created by script and have the necessary key relationships between them.
