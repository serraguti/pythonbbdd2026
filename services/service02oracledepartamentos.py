import oracledb

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user="system",
                                           password="oracle"
                                    , dsn="LOCALHOST/FREEPDB1")
    
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.connection.cursor()
        sql = "insert into DEPT values (:num,:nom, :loc)"
        cursor.execute(sql, (numero, nombre, localidad,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def eliminarDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "delete from DEPT where DEPT_NO=:id"
        cursor.execute(sql, (id,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
        