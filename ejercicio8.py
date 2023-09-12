"""
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

diccionario = {}

lista = [ ]


palabras = input("Palabras: ")

#En la siguiente linea de codigo voy a convertir el string (palabras) en una lista, separando ese string justo en donde esta la (,) y cada elemento de la lista sera el par palabra-traduccion:
lista_palabras = palabras.split(",")

#En el siguiente ciclo for recorro cada uno de los elementos de la lista, cada par palabra-traduccion:
for par in lista_palabras:
    #En la siguiente linea de codigo creo una nueva lista, llamada lista_par, la cual solo va a existir dentro del ciclo y va a guardar la "division" de cada par de la lista lista_palabras. O sea, par.split(":"), me va a dividir cada par palabra-traduccion, para hacerlos independientes y que cada uno sea un elemento de la lista.
    lista_par = par.split(":")
    #En la siguiente linea de codigo, utilizo la funcion extend para agregar a la lista vacia que cree arriba  la nueva lista lista_par, que es la que contiene cada elemento palabra-traduccion ya separado.
    lista.extend(lista_par)


#En la siguiente linea de codigo creo una sublista keys que va a contener solo las palabras en espaniol, lo hago utilizando sus indices. 
keys = lista[0::2]
#print(keys)

#En la siguiente linea de codigo creo una sublista values que va a contener solo las palabras en ingles (traducciones), lo hago utilizando sus indices. 
values = lista[1::2]
#print(values)


#En el siguiente ciclo, tomo los valores de la lista keys y de la lista values para crear el diccionario que me va a contener el par llave-valor.
# Para cada valor de la lista keys: 
for k in keys:
    #Creo la variable contador dentro del primer ciclo para que empiece a existir a partir de ahi, ya que si le creo afuera del ciclo, no va a existir al ejecutarse el segundo ciclo, este segundo ciclo debe iniciar ya con esa variable valiendo 0. 
    contador = 0
    #Se ejecuta el segundo ciclo que va a recorrer todas los valores de la lista keys. 
    for v in values:
        #Ahora le asigno a la variable diccionario que se declaro al inicio, sus llaves con sus respectivos valores. 
        diccionario[keys[contador]] = values[contador]
        #Voy sumando a contador un 1, en cada vuelta del ciclo for, para ir recorriendo las listas keys y value e ir agregando los valores del diccionario.
        contador += 1
#OJO - VARIABLE CONTADOR DECLARADA EN EL PRIMER CICLO -> Esto se debe a que en los ciclos anidados, se ejecuta el primer ciclo una primera vuelta y entra a ejecutarse el segundo ciclo dependiendo del primero, este segundo ciclo solo va a existir dentro del primero, todo lo que este fuera del primero no existe para el segundo.

#print(diccionario)



#PARTE_2:
#Pido la frase al usuario:
frase = input("Frase a traducir: ")
#Transformo la frase en una lista, cada palabra de la frase pasa a ser cada elemento de la nueva lista frase.
frase = frase.split(" ")



#Por medio del siguiente ciclo anidado voy a recorrer primero los elementos de la lista frase (frase del usuario)...:
for p in frase:
    #...Luego los key y value del diccionario en donde se encuentran las palabras espaniol-ingles: 
    for key, value in diccionario.items():
        #Ahora, si p es igual a key, imprime el value de esa key.
        if p == key:
            print(value,end=" ")
            #Si p no esta en diccionario, imprime simplemente p.
        elif p not in diccionario:
            print(p, end=" ")
            #Coloco el break para que no me imprima cada vez que recorre el diccionario buscado las coincidencias. El ciclo del diccionario toma la p de frase, la analiza ve si esta o no, y ejecuta segun lo que corresponda, rompe (break) con esa palabra y pasa a la otra p de la frase que le da el primer ciclo.
            break



#PALABRAS: hola:hi,dia:day,azul:blue,casa:house,rojo:red,carro:car,helado:icecream,zapato:shoes,amarillo:yellow,mesa:table,libro:book,oso:bear,franela:t-shirt,dia:day,casa:house,rojo:red,helado:icecream,amarillo:yellow,mesa:table,libro:book,oso:bear,franela:t-shirt,es:is,la:the,el:the

#(diccionario[key]) -> Da el value de esa key. 

#(diccionario.keys())-> Da las keys.

#(diccionario.values())-> Da las values.

#(diccionario.items())-> Da keys y values.

#(diccionario.get(usuario, "La divisa no esta en el diccionario."))-> Si no existe, no da key error. 