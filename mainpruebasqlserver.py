import mssql_python

connection = mssql_python.connect("")
sql = "select * from EMP"
cursor = connection.cursor()
cursor.execute(sql)
for row in cursor:
    print(f"{row[1]}")
cursor.close()
connection.close()
print("Fin de programa")
