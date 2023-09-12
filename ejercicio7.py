"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""
diccionario = {}

validador = "no"

while validador == "no":
    key = input("Articulo: ")
    value = input("Precio: ")
    diccionario[str(key)] = int(value)
    validador = input("Salir: ")
    if validador == "si":
        #debo agarrar los value y sumarlos. 
        tupla = tuple(diccionario.values())
        total = sum(tupla)
        print(total)

#Para sumar los values, los converti en tupla y los sume mediante la funcion sum().

#(diccionario[key]) -> Da el value de esa key.
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 