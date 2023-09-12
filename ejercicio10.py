"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente.

El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos. LISTO

2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. LISTO

3. Preguntar por el NIF del cliente y mostrar sus datos. LISTO

4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre. LISTO

5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre. LISTO

6. Terminar el programa. LISTO
"""
#nif -> 3 digitos
diccionario = {111: {"nombre":"Pedro",
                     "direccion":"Caracas",
                     "telefono":8532567,
                     "correo":"pedr0@gmail.com",
                     "preferente":True}, 
               112: {"nombre":"Luisa",
                     "direccion":"Valencia",
                     "telefono":7659437,
                     "correo":"luisa@gmail.com",
                     "preferente":False}, 
               113: {"nombre":"Eduardo",
                     "direccion":"Maracay",
                     "telefono":8762047,
                     "correo":"eduardo@gmail.com",
                     "preferente":True}, 
               114: {"nombre":"Sofia",
                     "direccion":"Barquisimeto",
                     "telefono":3863524,
                     "correo":"sofia@gmail.com",
                     "preferente":False}
               }

contador = 114
validador = "no"

while validador == "no":
    pregunta = input("Anadir, Eliminar, Mostrar cliente, Listar todos, Listar preferentes, Salir: ")
    if pregunta == "anadir":
        contador += 1
        nombre = input("Nombre: ")
        nombre = nombre.capitalize()
        direccion = input("Estado: ")
        direccion = direccion.capitalize()
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        preferente = input("Preferente: ")
        preferente = preferente.lower()
        if preferente == "true":
            preferente = True
        elif preferente == "false":
            preferente = False
        diccionario[contador] = {"nombre": nombre,
                                 "direccion": direccion,
                                 "telefono": telefono,
                                 "correo": direccion,
                                 "preferente": preferente
                                 }
    elif pregunta == "eliminar":
        eliminar = int(input("Llave a eliminar: "))
        del diccionario[eliminar]
    elif pregunta == "mostrar":
        mostrar = int(input("NIF del cliente: "))
        print(diccionario[mostrar])
    elif pregunta == "listar todos":
        #Cree una lista con los nif antes de entrar a un ciclo for que me va a iterar cada elemento de esa lista, esos elementos seran los nif.
        nif = list(diccionario.keys())
        for lista in nif:
            nombre = diccionario[lista]["nombre"]
            print(lista, nombre)
    elif pregunta == "listar preferentes":
        nif = list(diccionario.keys())
        for lista in nif:
            preferente = diccionario[lista]["preferente"]
            nombre = diccionario[lista]["nombre"]
            if preferente == True:
                print(lista, nombre, preferente)
    elif pregunta == "salir":
        validador = "si" 


print(diccionario)



#OPCION LISTAR PREFERENTES ->
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.


#OPCION SALIR ->
# Terminar el programa.



#print(diccionario)
#print(diccionario.items())
#print(diccionario.keys())
#print(diccionario.values())

#(diccionario[key]) -> Da el value de esa key. 
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 

