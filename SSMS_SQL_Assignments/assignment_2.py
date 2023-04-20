#creating table fruit_details
create table fruit_details(product varchar(20),amount int, Country varchar(20) )

#inserr=ting values into the fruit_details table
insert into fruit_details values('Banana', 1000, 'USA')

insert into fruit_details values('Carrots', 1500, 'India')

insert into fruit_details values('Beans', 1600, 'Sweden')

insert into fruit_details values('Orange', 2000, 'UK')

insert into fruit_details values('Orange', 2000, 'UAE')

insert into fruit_details values('Banana', 400, 'China')

insert into fruit_details values('Carrots', 1200, 'China')

#pivot columns operation on the table fruit_table
SELECT * from fruit_details
pivot( sum(amount) for Country in (USA,India,Sweden,UK,UAE,China)) as PivotTable

#unPivot columns operation on the table fruit_table
SELECT *
FROM
(
SELECT * FROM fruit_details
PIVOT
(
SUM(amount) FOR Country IN (USA,India,Sweden,UK,UAE,China)
) AS PivotTable
) P
UNPIVOT
(
Price FOR Country IN (USA,India,Sweden,UK,UAE,China)
)
AS UnpivotTable

