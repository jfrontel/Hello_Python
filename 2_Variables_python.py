# Variables en Python

''' Funciones integradas
Etán disponibles globalmente para su uso, se puede hacer uso de ellas sin importarlas ni configurarlas. 
Algunas funciones integradas de Python más utilizadas son: print(), len(), type(),  int(), float(), str(),
input() , list() , dict() , min() , max() , sum() , sorted() , open() , file() , help() y dir(). 
'''

print(len("Hola Mundo")) # Nos dirá el tamaño de la cadena
print(type("Hola Mundo"))
print(max([1, 2, 5, 19])) # Max numero en la lista
print(type([1, 2, 5, 19]))

#Podemos convertir un tipo de dato en otro
print(int(10)) #Sera entero
print(float(10)) #Sera flotante
print(str('10')) #Sera una cadena
print(complex(10)) #Sera un nº complejo

'''Con help('keywords') en Python interactivo (recordemos escribir python en terminal, exit() para salir)
mostrará las Keywords de Python; Usaremos help() para pedir información '''
#print(help('keywords'))
#print(help('for'))

print(min([1, 4, 9, 100]))
print(min(1, 4, 9, 100))
print(sum([1, 2, 3, 4]))


'''Variables en Python
Las variables almacenan datos en la memoria de una computadora.
Una variable se refiere a una dirección de memoria en la que se almacenan los datos.
Cuando asignamos un determinado tipo de datos a una variable, se llama declaración de variable.
El signo igual es un operador de asignación. Asignar significa almacenar datos en la variable. 
El signo igual en Python no es la igualdad como en Matemáticas.
'''

nombre = 'Jorge'
apellido = 'Frontela'
pais = 'Spain'
ciudad = 'Palencia'
edad = 39
casado = True
lenguajes = ['HTML', 'CSS', 'C', 'Cobol', 'Python']
inf_personal = {
   'nombre':'Jorge',
   'apellido':'Frontela',
   'country':'Spain',
   'ciudad':'Malaga'
   }

print(inf_personal) #ya veremos como sacar cada variables del diccionario
print(len(nombre))
print(len(apellido))
print(lenguajes)


'''Pedir informacion al usurio con input()'''
name = input('Cual es tu nombre?')
print(name)
age = input('Cual es tu edad?')
print(age)