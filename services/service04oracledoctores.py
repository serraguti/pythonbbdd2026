import oracledb
from models import doctor as models

class ServiceDoctores:
    def __init__(self):
        self.connection = oracledb.connect(user="system"
                                           ,password="oracle"
                                        , dsn="localhost/freepdb1")
    
    def getDoctores(self):
        cursor = self.connection.cursor()
        sql = "select * from DOCTOR"
        cursor.execute(sql)
        listaDoctores = []
        for row in cursor:
            doc = models.Doctor()
            doc.idDoctor = row[1]
            doc.apellido = row[2]
            doc.especialidad = row[3]
            doc.salario = row[4]
            doc.idHospital = row[0]
            listaDoctores.append(doc)
        cursor.close()
        return listaDoctores
    
    #Vamos a crear un doctor, pero NO vamos a enviar el ID
    #Nuestro método generará un ID máximo para el Doctor
    def insertarDoctor(self, apellido, especialidad, salario, hospital):
        cursor = self.connection.cursor()
        sql = "select max(DOCTOR_NO) + 1 as MAXIMO from DOCTOR"
        cursor.execute(sql)
        row = cursor.fetchone()
        id = row[0]
        sql = "insert into DOCTOR values (:hos,:id,:ape,:esp,:sal)"
        cursor.execute(sql, (hospital,id,apellido, especialidad,salario,))
        self.connection.commit()
        cursor.close()
    
    def updateDoctor(self, id, ape, espe, sal, hosp):
        cursor = self.connection.cursor()
        sql = """
            update DOCTOR set APELLIDO=:ape, ESPECIALIDAD=:espe,
            SALARIO=:sal, HOSPITAL_COD=:hosp
            where DOCTOR_NO=:id
        """
        cursor.execute(sql, (ape, espe, sal, hosp, id,))
        self.connection.commit()
        cursor.close()
    
    def deleteDoctor(self, id):
        cursor = self.connection.cursor()
        sql = "delete from DOCTOR where DOCTOR_NO=:id"
        cursor.execute(sql, (id, ))
        self.connection.commit()
        cursor.close()
        