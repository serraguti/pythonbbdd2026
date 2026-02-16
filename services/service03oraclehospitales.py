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
    
    def insertarHospital(self, id, nombre, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "insert into HOSPITAL values (:id,:nom,:dir,:tlf,:cam)"
        cursor.execute(sql, (id, nombre, dir, tlf, camas,))
        self.connection.commit()
        cursor.close()
        
    def updateHospital(self, id, nom, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "update HOSPITAL set NOMBRE=:nom, DIRECCION=:dir "\
            ", TELEFONO=:tlf, NUM_CAMA=:cam "\
            " where HOSPITAL_COD=:id"
        cursor.execute(sql, (nom, dir, tlf, camas, id,))
        self.connection.commit()
        cursor.close()