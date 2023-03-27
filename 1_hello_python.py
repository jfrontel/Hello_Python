#Comprobar version de python (python --version) en terminal

"""Entrar en Shell interactivo de python (Escribir Python en Terminal)
Para salir exit()
Podemos escribir 1 linea de comentario con #
Podemos escribir varias lineas de comentario con Triple comilla simple o doble
"""

#Imprimir por pantalla hola pyton
print("hello python")

#Imprimir tipo de variable
print(type("hello"))
print(type(1984))
print(type(10.45))

#Hagamos algunas operaciones matemáticas básicas
print(2 + 3)
print(5 - 2)
print(2 * 3)
print(10 / 3)
print(5 % 2) #Resto
print(10 // 3) #Division eliminado el resto

#Podemos escribir un string con comillas simples o dobles
print("Hola Python")
print('Hola Python')
#Podemos concatenar argumentos en el print
print("Hola","Python","!")


'''Lista en Python: es una colección ordenada que permite almacenar diferentes tipos de elementos de datos.
[0, 1, 2, 3, 4, 5]
['Finland','Estonia', 'Sweden','Norway']
['Banana', 10, False, 9.81]
'''
print("[0, 1, 2, 3, 4, 5]") #Imprime una cadena
print([0, 1, 2, 3, 4, 5])   #Imprime una lista
print(max([0, 1, 2, 3, 4, 5])) #Coge el max de la lista 5

print(type("[0, 1, 2, 3, 4, 5]"))
print(type([0, 1, 2, 3, 4, 5]))


'''Diccionario en Pyton
Un objeto de diccionario de Python es una colección desordenada de datos 
en un formato de par de valores clave'''
{
'Nombre':'Jorge',
'Apellido':'Frontela',
'Pais':'Spain', 
'age':39, 
'Estado_Civil_Casado':True,
'Lenguajes de programacion':['C', 'Cobol', 'C++', 'Python']
}

'''Tupla en Python
Una tupla es una colección ordenada de diferentes tipos de datos como una lista, pero 
las tuplas no se pueden modificar una vez que se crean. Son inmutables.'''

('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury')

'''Set en Python 
A diferencia de list y tuple, set no es una colección ordenada de elementos '''
{2, 4, 3, 5}
{3.14, 9.81, 2.7}

#Comprobar tipos de datos: type()
type(10)
print(type(10))     #int
type(3.1416)        
print(type(3.1416)) #float
print(type(1 + 4j)) #complex
print(type('Soy Jorge'))    #str
print(type({'nombre': 'jorge', 'Apellido': 'Frontela'})) #diccionario
print(type([1, 2, 5, 8])) #lista
print(type(('uno', 'dos', 'tres'))) #tupla
print(type({2, 4, 3, 5})) #set