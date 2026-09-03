### Task
<!-- 
create a database - bank_db
created a table - employees
    emp_id
    name
    desig
    dept

emp_id column should not allow duplicate and null values
value of column should be increamental 
name column should not have null value
desig column should have defauls value as 'Probation' 
                                -->

### querry MYSQL

CREATE DATABASE bank_db;

SHOW DATABASES;

USE bank_db;

CREATE TABLE employees(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(60) NOT NULL,
    desig VARCHAR(20) DEFAULT 'PROBATION',
    dept VARCHAR(30) NOT NULL
)


### Task 2 Display the data, Update the data, delete data

    SELECT emp_id , name 
    FROM employees 
    WHERE emp_id = ID;

    SELECT * FROM employees 
    WHERE emp_id = ID;

    SELECT * FROM employees 
    WHERE dept = 'GIVEN_DEPT';

    UPDATE employees 
    SET dept = 'NEW_DEPT'
    WHERE emp_id = ID;

    DELETE 
    FROM employees
    WHERE emp_id = ID;

 ### Task 3 use string function  

    SELECT CONCAT_WS(':',emp_id, fname, desig, dept ) FROM employees;

    SELECT CONCAT_WS(':',emp_id, CONCAT_WS(fname, ' ' , lname), desig, dept) FROM employees;

    SELECT CONCAT_WS(':',emp_id, fname, UPPER(desig), dept) FROM employees;

    SELECT CONCAT_WS(LEFT(dept, 1), emp_id,' ' , fname) FROM employees

### Task 4 
1. Find different type of departments in database?
    
    select distinct dept From employees

2. Display record with High-low salary

    SELECT * FROM employees 
    ORDER BY salary DESC

3. How to see only top 3 records from table?

    SELECT * FROM employees 
    ORDER BY salary DESC
    LIMIT 3

4. Show records where first name start with letter 'A'

    SELECT * FROM emplyees 
    WHERE fname ilike '%A'

5. Show records where length on lname is 4 character?

    

    