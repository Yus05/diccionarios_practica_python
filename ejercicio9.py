"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.

Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 

El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.

Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 

Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.

Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

diccionario = {102:1500,
               204:25,
               103:2000,
               206:2000,
               205:95,
               176:105,
              }
#Validador que me ayuda a activar el ciclo y a salirme del mismo, segun lo que disponga el ususario.
validador = "no"
#Mientras el validador sea igual a no:
while validador == "no":
    #El ciclo empieza con el valor de no para el validador. Se dan las dos primeras opciones.
    pregunta = input("Agregar o Pagar? : ")
    #Si decide agregar se pide el numero de factura (la key) y el monto de la misma (el value).
    if pregunta == "agregar":
        factura = int(input("Factura: "))
        monto = int(input("Monto: "))
        #Se agrega al diccionario los nuevos valores: 
        diccionario[factura] = monto
        #Convertimos los value del diccionario a una lista para despues poder sumar esos valores y el resultado de esa suma es el total de lo que falta por pagar.
        value = list(diccionario.values())
        total = sum(value)
        #Imprimimos ese total.
        print("Falta por pagar", total)
        #Preguntamos si deseamos continuar en el ciclo por medio de validador:
        validador = input("Salir: ")
        #Si en la pregunta el usuario desea pagar:
    elif pregunta == "pagar":
        #Se crea la nueva variable pago que es donde se almacena la factura a pagar.
        pago = int(input("Numero de factura a pagar: "))
        #Y se imprime el valor de la factura a pagar:
        print("Se han pagado",diccionario[pago])
        #Eliminamos del diccionario esa factura a pagar: 
        del diccionario[pago]
        #Volvemos a ejecutar el validador.
        validador = input("Salir: ")
        
print(diccionario)

#VALIDADOR -> variable que me va a ayudar a agregar constantemente valores al diccionario. Me ayuda a mantenerme dentro del diccionario, del ciclo.




