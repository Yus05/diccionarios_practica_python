"""
EJERCICIO_11 sin notas:
"""

directorio = "01234567L;Luis Gonzalez;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramirez;macarena@mail.com;692839321;8\n63823376M;Juan Jose Martinez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sanchez;carmen@mail.com;667677855;15.7"

lista_directorio = directorio.split("\n")
string_lista = ";".join(lista_directorio)
lista_string = string_lista.split(";")

lista = lista_string
lista_nif = lista[0:20:5]
lista_nombre = lista[1::5]
lista_mail = lista[2::5]
lista_phone = lista[3::5]
lista_descuento = lista[4::5]

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












