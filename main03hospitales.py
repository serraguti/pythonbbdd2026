from services import service03oraclehospitales as services

#Creamos nuestro servicio de Oracle
service = services.ServiceHospitales()
print("------CRUD Hospitales------")
print("1.- Mostrar hospitales")
print("2.- Insertar hospital")
print("3.- Modificar hospital")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Listado de hospitales")
    lista = service.getHospitales()
    for h in lista:
        print(f"Id: {h.idHospital} - {h.nombre} - Camas: {h.camas}")
elif (opcion == 2):
    id = int(input("Id del nuevo hospital: "))
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    tlf = input("Telefono: ")
    camas = int(input("Número de camas: "))
    service.insertarHospital(id, nombre, direccion, tlf, camas)
    print("Insertado OK")
elif (opcion == 3):
    id = int(input("Hospital a modificar: "))
    nombre = input("Nuevo nombre: ")
    dir = input("Nueva dirección: ")
    tlf = input("Teléfono: ")
    cam = int(input("Camas: "))
    service.updateHospital(id, nombre,dir, tlf,cam)
    print("Hospital modificado OK")
print("Fin de programa")