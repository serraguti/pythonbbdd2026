import mssql_python
#SQL_CONNECTION_STRING="Server=<server_name>;Database={<database_name>};Encrypt=yes;TrustServerCertificate=no;Authentication=ActiveDirectoryInteractive"
connection = mssql_python.connect('Server=sqlpaco3430.database.windows.net;Database=AZURETAJAMAR;Encrypt=yes;UID=adminsql;PWD=Admin123;TrustServerCertificate=yes')
print("Funciona SQL Server")

cursor = connection.cursor()
sql = "select * from EMP"
cursor.execute(sql)
for row in cursor:
    print(f"Apellido {row[1]}, Oficio: {row[2]}")
cursor.close()