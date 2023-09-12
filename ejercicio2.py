"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
#diccionario = {}

nombre = (input("Nombre: ")).capitalize()
edad = int(input("Edad: "))
direccion = (input("Direccion: ")).capitalize()
telefono = int(input("Telefono: "))

diccionario = {"nombre": nombre,
               "edad": edad,
               "direccion": direccion,
               "telefono": telefono}


print(diccionario["nombre"], "tiene", diccionario["edad"],"anios.", "Vive en", diccionario["direccion"], "y su numero de telefono es",diccionario["telefono"])

