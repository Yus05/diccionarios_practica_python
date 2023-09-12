"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

diccionario = {'Euro':'€',
               'Dollar':'$',
               'Yen':'¥'}

usuario = input("Escribe una divisa: ")
usuario = usuario.capitalize()

print(diccionario.get(usuario, "La divisa no esta en el diccionario."))


#Diferencias entre cada uno: 
#print(diccionario[usuario])
#print(diccionario.keys())
#print(diccionario.values())
#print(diccionario.items())

        
        
    
    








    

    
