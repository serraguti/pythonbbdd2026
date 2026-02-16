import oracledb
from models import hospital as models

class ServiceHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user="system"
                                    , password="oracle"
                                    , dsn="localhost/freepdb1")
                
    #Metodo para recuperar todos los hospitales
    def getHospitales(self):
        cursor = self.connection.cursor()
        sql = "select * from HOSPITAL"
        cursor.execute(sql)
        listaHospitales = []
        for row in cursor:
            hospital = models.Hospital()
            hospital.idHospital = row[0]
            hospital.nombre = row[1]
            hospital.direccion = row[2]
            hospital.telefono = row[3]
            hospital.camas = row[4]
            listaHospitales.append(hospital)
        cursor.close()
        return listaHospitales