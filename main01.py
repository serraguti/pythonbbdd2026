from services import service01prueba
print("Soy un Main")
texto = service01prueba.getSaludo()
pez = service01prueba.getMascota()
leona = service01prueba.getMascota2()
print(f"{pez.nombre}, Raza: {pez.raza}")
print(leona.nombre)
print(texto)
lista = service01prueba.getListaMascotas()
for dato in lista:
    print(dato.nombre)