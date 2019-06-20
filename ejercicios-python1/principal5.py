"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellido": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellido": "Alvarez"}

lista = [diccionario, diccionario2]
#print("Imprimir diccionario")
for l in lista:
	midiccionario = l
	print("Mi nombre es: %s y mi apellido es: %s" % (midiccionario["nombre"]
		, midiccionario["apellido"]))


