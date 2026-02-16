from services import service03oraclehospitales as services

#Creamos nuestro servicio de Oracle
service = services.ServiceHospitales()
print("------CRUD Hospitales------")
print("1.- Mostrar hospitales")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Listado de hospitales")
    lista = service.getHospitales()
    for h in lista:
        print(f"Id: {h.idHospital} - {h.nombre} - Camas: {h.camas}")

print("Fin de programa")