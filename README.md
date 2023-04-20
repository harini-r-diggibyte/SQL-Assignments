# SQL-Assignments #

This repository contains SQL Assignments done using Spark and SSMS.

## SQL Assignments using Spark ##

The Directories (SQL_1, SQL_2, SQL_3) contains Spark SQL Assignments respectively.

### SQL Assignment 1  (SQL_1) ###

Create a table with data in the below structure:
{"firstname":"James","middlename":"","lastname":"Smith"},"03011998","M",3000

  - Column1 : name - {"firstname":"James","middlename":"","lastname":"Smith"}
  - Column2 : dob - "03011998"
  - Column3 : gender - "M"
  -Column4 : Salary - 3000
  
Perform the below tasks in the created table :
  
  
  - Select firstName,lastName and salary from dataFrame.
  
  - Add Country, department, and age column in the dataframe. 

  - Change the value of salary column. 

  - Change the data types of DOB and salary to String  

  - Derive new column from salary column. 

  - Rename nested column( Firstname -> firstposition, middlename -> secondposition, lastname -> lastposition) 

  - Filter the name column whose salary in maximum.  

  - Drop the department and age column. 

  - List out distinct value of dob and salary 
  
  
### SQL Assignment 2 (SQL_2) ###

Create a non-nested dataframe with product, amount and country fields. 

        ("Banana",1000,"USA")
        ("Carrots",1500,"India")
        ("Beans",1600,"Sweden")
        ("Orange",2000,"UK")
        ("Orange",2000,"UAE")
        ("Banana",400,"China")
        ("Carrots",1200,"China")
        
Perform the below tasks on the created table :

  -  Find total amount exported to each country of each product. 

  -  Perform unpivot function on output of above question. 
  
  
### SQL Assignment 3 (SQL_3) ###

Create a data frame with employee_name, department and salary. 

Perform below tasks on the created dataFrame

  - Select first row from each department group. 

  - Create a Dataframe from Row and List of tuples. 

  - Apply Schema while creating a Dataframe. 

  - Retrieve Employees who earns the highest salary. 

  - Select the highest, lowest, average, and total salary for each department group.  


## SQL Assignment using SSMS ##

SSMS_SQL_Assignments directory contains SQL Assignments done using SSMS setup.
