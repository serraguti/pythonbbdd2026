from models import mascota
#Vamos a tener un simple metodo
#para llamarlo desde el main
def getSaludo():
    return "Hoy es juernes"

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza = "Pez"
    dato.edad = 22
    return dato
def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Nala"
    dato.raza = "Leona"
    dato.edad = 18
    return dato

def getListaMascotas():
    listaMascotas = []
    leona = mascota.Mascota()
    leona.nombre = "Nala"
    leona.raza = "Leona"
    leona.edad = 18
    listaMascotas.append(leona)
    leon = mascota.Mascota()
    leon.nombre = "Simba"
    leon.raza = "Leon"
    leon.edad = 18   
    listaMascotas.append(leon) 
    cosa = mascota.Mascota()
    cosa.nombre = "Olaf"
    cosa.raza = "Cosa"
    cosa.edad = 14   
    listaMascotas.append(cosa)
    return listaMascotas 


