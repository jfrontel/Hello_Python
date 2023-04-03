# Diccionario en Python

'''Un diccionario es una colección de tipos de datos no ordenados, modificables (mutables) emparejados (clave: valor).

Creación de un diccionario
Para crear un diccionario usamos corchetes, {} o la función integrada dict() .

# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}'''

person = {
    'nombre':'Jorge',
    'apellido':'Frontela',
    'edad':39,
    'pais':'Spain',
    'casado':True,
    'lenguajes':['C', 'C++', 'Cobol', 'Labview', 'Python'],
    'Direccion':{
        'calle':'Pasaje Miramar',
        'codigo_postal':'29017'
        }
    }

# Acceso a elementos del diccionario
#Podemos acceder a los elementos del diccionario haciendo referencia a su nombre clave.
print(person['nombre'])
print(person['lenguajes'][2])
print(person['casado'])
print(person['Direccion']['calle'])
#print(person['city'])
'''Acceder a un elemento por nombre de clave genera un error si la clave no existe. 
Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get. 
El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.'''
print(person.get('apellido'))
print(person.get('city'))

#Adición de elementos a un diccionario
person['Profesion'] = 'Ingeniero'
person['lenguajes'].append('HTML')
person['Direccion']['numero'] = 17
print(person)

#Modificación de elementos en un diccionario
person['nombre'] = 'Jorgito'
person['edad'] = 40
person['casado'] = False
person['Direccion']['calle'] = 'Heroes de Sostoa'
print(person)

#Comprobación de claves en un diccionario
print('nombre' in person)

#Eliminación de pares de clave y valor de un diccionario
'''pop(clave) : elimina el elemento con el nombre de clave especificado:
popitem() : elimina el último elemento
del : elimina un elemento con el nombre de clave especificado'''
person.pop('Profesion')
person.popitem()
del person['casado']
print(person)

#Cambio de diccionario a una lista de elementos --> items()
print(person.items())

#Borrar un diccionario --> clear()
print(person.clear())

#Eliminación de un diccionario --> del
del person

#Copiar un diccionario --> copy() 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct_copy)

#Obtener claves de diccionario como una lista --> keys()
keys = dct.keys()
print(keys)

#Obtener valores de diccionario como una lista --> values()
values = dct.values()
print(values)


#       EJERCICIOS DIA_9 
'''
1._Crea un diccionario vacío llamado perro
2._Agregue nombre, color, raza, patas, edad al diccionario de perros
3._Cree un diccionario para estudiantes y agregue nombre, apellido, sexo, edad, estado civil, 
    habilidades, país, ciudad y dirección como claves para el diccionario.
4._Obtener la longitud del diccionario del estudiante
5._Obtenga el valor de las habilidades y verifique el tipo de datos, debe ser una lista
6._Modifique los valores de las habilidades agregando una o dos habilidades
7._Obtenga las claves del diccionario como una lista
8._Obtenga los valores del diccionario como una lista
9._Cambie el diccionario a una lista de tuplas usando el método items()
10._Eliminar uno de los elementos del diccionario
11._Eliminar uno de los diccionarios'''

perro = {}
perro['nombre'] = 'calcetines'
perro['color'] = 'blanco'
perro['raza'] = 'doberman'
perro['edad'] = 1
print(perro.keys())
print(perro.values())
print(perro)

estudiantes = {
    'nombre': 'Jorge',
    'sexo': 'Hombre',
    'edad': '40',
    'estado_civil': 'casado',
    'habilidades': ['creativo', 'inteligente', 'racional', 'justo'],
    'pais' : 'Andalucia',
    'ciudad': 'El Palo'
}
print(len(estudiantes))
print(len(perro))
estudiantes['habilidades'].append('trabajador')
print(type(estudiantes['habilidades']))
print(estudiantes.keys())
print(estudiantes.values())
print(estudiantes.items())
del estudiantes['habilidades']
print(estudiantes)
del estudiantes