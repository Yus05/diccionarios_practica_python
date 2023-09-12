"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""
fecha = input("Fecha dd/mm/aaaa: ")

fecha_lista = fecha.split("/")
# Metodo split -> Nos permite generar una lista a partir de un string.

diccionario = {"dia": fecha_lista[0],
               "mes": {1: "Enero",
                       2: "Febrero",
                       3: "Marzo",
                       4: "Abril",
                       5: "Mayo",
                       6: "Junio",
                       7: "Julio",
                       8: "Agosto",
                       9: "Septiembre",
                       10: "Octubre",
                       11: "Noviembre",
                       12:"Diciembre"              
                      },
                "ano": fecha_lista[2]
              }

mes = int(fecha_lista[1])

dia = diccionario["dia"]
mes = diccionario["mes"][mes]
ano = diccionario["ano"]
print("El", dia, "del mes de", mes, "del anio", ano)


#(diccionario[key]) -> Da el value de esa key.
#(diccionario.keys())-> Da las keys.
#(diccionario.values())-> Da las values.
#(diccionario.items())-> Da keys y values.
#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 