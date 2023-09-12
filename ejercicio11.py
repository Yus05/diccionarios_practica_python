"""
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

"nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
"""

# NECESITO PASAR DE ESTO:
#"nif;nombre;email;teléfono;descuento\n
#01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n
#71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n
#63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n
#98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# A ESTO:
#diccionario = {'01234567L': {'nombre': 'Luis González',
#                              'email': 'luisgonzalez@mail.com',
#                              'teléfono': '656343576',
#                              'descuento': 12.5},
#               '71476342J': { 'nombre': 'Macarena Ramírez',
#                              'email': 'macarena@mail.com',
#                              'teléfono': '692839321',
#                              'descuento': 8.0},
#               '63823376M': { 'nombre': 'Juan José Martínez',
#                              'email': 'juanjo@mail.com',
#                              'teléfono': '664888233',
#                              'descuento': 5.2},
#               '98376547F': { 'nombre': 'Carmen Sánchez',
#                              'email': 'carmen@mail.com',
#                              'teléfono': '667677855',
#                              'descuento': 15.7}
#               }


#nif ; nombre ; email ; telefono ; descuento
directorio = "01234567L;Luis Gonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramirez;macarena@mail.com;692839321;8\n63823376M;Juan Jose Martinez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sanchez;carmen@mail.com;667677855;15.7"
#DEBO USAR EL METODO SPLIT. DEBO USARLO 2 VECES. PRIMERO PARA SEPARAR CADA CLIENTE Y LUEGO PARA SEPARAR CADA ELEMENTO DE CADA CLIENTE.

#A continuacion creo una lista a partir del string directorio, en donde cada elemento de la lista es cada cliente.
lista_directorio = directorio.split("\n")
#print(lista_directorio)

#A continuacion transformo esa lista en una string y le meto el ";" entre cada elemento de la lista anterior.
string_lista = ";".join(lista_directorio)
#print(string_lista)

#A continuacion vuelvo a convertir el string anterior en una lista y esta vez utilizo los ; como punto de ruptura.
lista_string = string_lista.split(";")
lista = lista_string
#print(lista)

#print(lista_string)

# -> Ya tengo absolutamente TODOS los elementos de los usuarios separados.

#Este for lo hice para revisar elemento por elemento. 
#for elemento in lista:
 #   print(elemento)


#AHORA DEBO ANIADIR LOS ELEMENTOS DE LA LISTA AL DICCIONARIO: 

# - ['01234567L', 'Luis Gonzalez', 'luisgonzalez@mail.com', '656343576', '12.5', '71476342J', 'Macarena Ramirez', 'macarena@mail.com', '692839321', '8', '63823376M', 'Juan Jose Martinez', 'juanjo@mail.com', '664888233', '5.2', '98376547F', 'Carmen Sanchez', 'carmen@mail.com', '667677855', '15.7']

#1-01234567L
#2-Luis Gonzalez
#3-luisgonzalez@mail.com
#4-656343576
#5-12.5
#6-71476342J
#7-Macarena Ramirez
#8-macarena@mail.com
#9-692839321
#10-8
#11-63823376M
#12-Juan Jose Martinez
#13-juanjo@mail.com
#14-664888233
#15-5.2
#16-98376547F
#17-Carmen Sanchez
#18-carmen@mail.com
#19-667677855
#20-15.7

#A continuacion estoy obteniendo los nif:
lista_nif = lista[0:20:5]
#print(lista_nif)

lista_nombre = lista[1::5]
#print(lista_nombre)

lista_mail = lista[2::5]
#print(lista_mail)

lista_phone = lista[3::5]
#print(lista_phone)

lista_descuento = lista[4::5]
#print(lista_descuento)

#Despues de hacer las sublistas con indices,trata de hacerlo con un ciclo for en prueba.py

#AHORA DEBO AGREGA CADA ELEMENTO DE ESAS DIFERENTES LISTAS AL DICCIONARIO.

diccionario = {
              }


contador = 0
for nif in lista_nif:
    diccionario[nif] = {}
    for nombre in lista_nombre:
        diccionario[nif]["nombre"] = lista_nombre[contador]
    for mail in lista_mail:
        diccionario[nif]["mail"] = lista_mail[contador]
    for mail in lista_phone:
        diccionario[nif]["phone"] = lista_phone[contador]
    for mail in lista_descuento:
        diccionario[nif]["descuento"] = lista_descuento[contador]    
    contador += 1


print(diccionario)