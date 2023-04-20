#creating a table employee_details
create table employee_details (emp_name varchar(20),Department varchar(20),salary int)

#inserting values into the table employee_details
insert into employee_details values('James','Sales',3000)

insert into employee_details values('Michael','Sales',4600)

insert into employee_details values('Robert','Sales',4100)

insert into employee_details values('Maria','Finance',3000)

insert into employee_details values('Raman','Finance',3000)

insert into employee_details values('Scott','Finance',3300)

insert into employee_details values('Jen','Finance',3900)

insert into employee_details values('Jeff','Marketting',3000)

insert into employee_details values('Kumar','Marketting',2000)

select * from employee_details

#selecting first row from each department which contains all details of particular employee
SELECT emp_name,department,salary FROM (
  SELECT emp_name, department, salary,
         ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary asc) AS row_num
  FROM employee_details
) subquery
WHERE row_num = 1;

#selecting employee's who get highest salary from each department
SELECT emp_name,department,salary FROM (
  SELECT emp_name, department, salary,
         ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
  FROM employee_details
) subquery
WHERE row_num = 1;

#Displaying average salary in each department
SELECT department, avg(salary) as avg_salary
FROM employee_details
GROUP BY department;

#Displaying the total of all salaries in each department
SELECT department, sum(salary) as total_salary
FROM employee_details
GROUP BY department;

#Displaying minimum salary in each department
SELECT department, min(salary) as min_salary
FROM employee_details
GROUP BY department;

#Displaying maximum salary in each department
SELECT department, max(salary) as max_salary
FROM employee_details
GROUP BY department;

