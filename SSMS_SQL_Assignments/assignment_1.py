#creating a table called emp
create table emp(firstName varchar(30),middleName varchar(30),lastName varchar(30),dob int, gender char(1),salary int )

#inserting values into the table
insert into emp values('James','','Smith',03011998,'M',3000)
insert into emp values('Michael','Rose','',10011998,'M',20000)
insert into emp values('Robert','','Williams',02012000,'M',3000)
insert into emp values('Maria','Annie','Jones',03011998,'F',11000)
insert into emp values('Jen','Mary','Brown',04101998,'F',10000)

select * from emp

#selecting firstName,lastName,Salary column from the table emp
select firstName,lastName,salary from emp

#adding new column Country,Department,Age to the table emp
alter table emp add Country varchar(20)

alter table emp add Department varchar(20)

alter table emp add age int

#updating the salary column value by incrementing it to 1000
update emp set salary=salary+1000

#creating a new salary column which has salary incremented by a value of 5000
select *,salary+5000 as new_salary from emp

#renaming the firstName, middleName, lastName as firstPosition,secondPosition,thirdPosition respectively.
exec sp_RENAME 'emp.firstName','firstPosition','column'

exec sp_RENAME 'emp.middleName','secondPosition','column'

exec sp_RENAME 'emp.lastName','thirdPosition','column'

#printing the firstName,middleName,lastName of the emp who is getting the highest salary
select firstPosition,secondPosition,thirdPosition from emp where salary in (select max(salary) from emp)

#dropping the columns aege and department from the table emp
alter table emp drop column age
alter table emp drop column department

#selecting distinct values of column dob from emp table
select distinct dob from emp

#selecting distinct values of column salary from emp table
select distinct salary from emp

#changing the datatype of dob and salary column to string
alter table emp alter column dob varchar(10)

alter table emp alter column salary varchar(10)
#to view the data type of columns in a table emp
select * from information_schema.columns where table_name='emp'