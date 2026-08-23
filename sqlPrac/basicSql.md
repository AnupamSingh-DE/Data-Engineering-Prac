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


### Task 2
