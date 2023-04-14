from SQL_3.core3.utils_sql3 import *
#creating a sparkSession
spark=sparkSession()

#creating the dataFrame
df_new=dataFrame_creation(spark)
df_new.show()
#getting the first row each department wise
firstRow=first_row_dept_wise(df_new)
firstRow.show()

#each department wise printing the hightest salary
high_sal=highest_sal_dept_wise(df_new)
high_sal.show()

#calculating highest salary, lowest salary, average Salary, finding total salary for each department
aggregation_values=high_low_avg_totSal(df_new)
aggregation_values.show()
