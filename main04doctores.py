from services import service04sqlserverdoctores as sd
#Creamos un objeto de este servicio para las consultas
service = sd.ServiceDoctores()

print("CRUD de Doctores")
print("1.- Mostrar doctores")
print("2.- Insertar doctor")
print("3.- Update doctor")
print("4.- Delete doctor")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    print("Listado de doctores")
    lista = service.getDoctores()
    for doc in lista:
        print(f"{doc.apellido} - {doc.especialidad} - {doc.salario}")
elif (opcion == 2):
    ape = input("Apellido del doctor: ")
    espe = input("Especialidad: ")
    salario = int(input("Salario del doctor: "))
    hospital = int(input("Código de hospital: "))
    service.insertarDoctor(ape, espe, salario, hospital)
    print("Doctor insertado OK")
elif (opcion == 3):
    id = int(input("Id del doctor a modificar: "))
    ape = input("Apellido: ")
    espe = input("Especialidad: ")
    sal = int(input("Salario: "))
    hosp = int(input("Id hospital: "))
    service.updateDoctor(id, ape, espe, sal, hosp)
    print("Doctor modificado OK")
elif (opcion == 4):
    id = int(input("Id del doctor a eliminar: "))
    service.deleteDoctor(id)
    print("Doctor eliminado")
print("Fin de programa")