#Tenemos la posibilidad de poner un Alias
#a esto namespace
from services import service02oracledepartamentos as serv
print("Bienvenido a mi Servicio Departamentos")
#Creamos la clase del servicio
servicio = serv.ServiceDepartamentos()
print("Buscar departamento")
numero = int(input("Id a buscar: "))
dato = servicio.getDepartamento(numero)
print(f"El nombre del departamento es {dato.nombre}")
print(f"La localidad es {dato.localidad}")







print("Insertar departamento")
numero = int(input("Id departamento: "))
nombre = input("Nombre departamento: ")
localidad = input("Localidad: ")
reg = servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Insertados: {reg}")
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
