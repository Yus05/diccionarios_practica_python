"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70"""

diccionario = {"Platano": 1.35,
               "Manzana": 0.80,
               "Pera": 0.85,
               "Naranja": 0.70
               }

fruta = input("Fruta: ")
fruta = fruta.capitalize()
kilos = int(input("Kilos: "))

if fruta not in diccionario:
    print("La fruta no esta disponible.")
else:
    valor = diccionario[fruta] * kilos
    print("Debes pagar un total de ",valor, "pesos por", kilos, "kilos de", fruta)

#(diccionario[key]) -> Da el value de esa key.
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 
