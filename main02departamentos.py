#Tenemos la posibilidad de poner un Alias
#a esto namespace
from services import service02oracledepartamentos as serv
print("Bienvenido a mi Servicio Departamentos")
#Creamos la clase del servicio
servicio = serv.ServiceDepartamentos()
print("Insertar departamento")
numero = int(input("Id departamento: "))
nombre = input("Nombre departamento: ")
localidad = input("Localidad: ")
reg = servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Insertados: {reg}")
print("Dime un departamento a eliminar")
id = int(input())
reg = servicio.eliminarDepartamento(id)
print(f"Eliminados: {reg}")
print("Fin de programa")
