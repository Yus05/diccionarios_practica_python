"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
diccionario = {}

validador = "no"

while validador == "no":
    key = input("Que valor deseas agregar: ")
    value = input("Cual es su "+ key +": ")
    diccionario[str(key)] = value
    print(diccionario)
    validador = input("Salir: ")

# Cree un validador que me va a permitir detener el ciclo mediante una condicion. Mientras validador sea igual a no, ejecuta el ciclo. / Creo las variables key y value, que me van a recibir los datos del usuario. / luego agrego al diccionario vacio los valores que me da el usuario. / Imprimo en cada vuelta el diccionario con cada valor nuevo ingresado. / Y finalmente le pregunto al usuario si desea continuar por medio del validador. 


#(diccionario[key]) -> Da el value de esa key.
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 




    




#Ok, ahora debo hacer el ciclo continuo y romperlo cuando sea necesario, e ir agregando de manera continua los valores al diccionario e imprimiendolo. 





#nombre = input("Nombre: ")
#nombre = nombre.capitalize()

#diccionario["Nombre"] = nombre
#print(diccionario)

# edad = input("Edad: ")
#diccionario["Edad"] = edad

#print(diccionario)



#En Python, es posible realizar modificaciones, y a su vez, agregar nuevos elementos a nuestros diccionarios con una sencilla sintaxis:

#diccionario[clave] = nuevo_valor
#-> Antes del igual va la clave cuyo valor queremos modificar o cuyo valor queremos agregar a nuestro diccionario. 

#dictionary = {"a": 1,
#              "b": 2,
#              "c": 3
#             }

#dictionary["a"] = 0

#--> Ahora "a" : 0

#Si escribo:

#dictionary["d"] = 4

#--> Se agrega ese nuevo valor al diccionario original, en el ultimo lugar. 

















#(diccionario[key]) -> Da el value de esa key.
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error.

