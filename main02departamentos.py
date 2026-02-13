#Tenemos la posibilidad de poner un Alias
#a esto namespace
from services import service02oracledepartamentos as serv
print("Bienvenido a mi Servicio Departamentos")
#Creamos la clase del servicio
servicio = serv.ServiceDepartamentos()
#Si queremos un menu simple
print("--------Menu de viernes-----")
print("1.- Insertar departamento")
print("2.- Mostrar departamentos")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    #Codigo de insertar
    print("Insertar departamento")
    numero = int(input("Id departamento: "))
    nombre = input("Nombre departamento: ")
    localidad = input("Localidad: ")
    reg = servicio.insertarDepartamento(numero, nombre, localidad)
    print(f"Insertados: {reg}")
else:
    #Codigo de mostrar
    print("------Departamentos--------")
    lista = servicio.getListaDepartamentos()
    for dept in lista:
        print(f"{dept.idDepartamento} - {dept.nombre} - {dept.localidad}")




print("Buscar departamento")
numero = int(input("Id a buscar: "))
dato = servicio.getDepartamento(numero)
print(f"El nombre del departamento es {dato.nombre}")
print(f"La localidad es {dato.localidad}")








print("-------Modificar departamento------")
numero = int(input("Id departamento a modificar: "))
nombre = input("Nombre departamento: ")
localidad = input("Localidad: ")
reg = servicio.updateDepartamento(numero, nombre, localidad)
print(f"Modificados: {reg}")
print("Dime un departamento a eliminar")
id = int(input())
reg = servicio.eliminarDepartamento(id)
print(f"Eliminados: {reg}")
print("Fin de programa")
