# Tuplas en python

'''Una tupla es una colección de diferentes tipos de datos ordenados e inmutables. Las tuplas se escriben con (). 
Una vez que se crea una tupla, no podemos cambiar sus valores. 
No podemos usar métodos de agregar, insertar, eliminar en una tupla porque no es modificable (mutable). 
A diferencia de list, tuple tiene pocos métodos. Métodos relacionados con las tuplas:

tuple(): para crear una tupla vacía
count (): para contar el número de un elemento específico en una tupla
index (): para encontrar el índice de un elemento específico en una tupla
operador: unir dos o más tuplas y crear una nueva tupla'''

# Crear Tupla

#Tupla vacía: creación de una tupla vacía
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

#Tupla con valores iniciales
# syntax
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon', 'fresa', 'apple')

# Longitud de una Tupla
print(len(fruits))

# Acceso a elementos de una Tupla
# usamos indexación positiva o negativa para acceder a elementos de tupla.
print(fruits[0])
print(fruits[len(fruits) - 1])
print(fruits[-1])

# División de Tuplas en Nueva tupla
'''Podemos dividir una subtupla especificando un rango de índices donde comenzar y terminar, 
el valor devuelto será una nueva tupla con los elementos especificados'''
tupla_new = fruits[0:3]
tp_new = fruits[-3:]
print(tupla_new)
print(tp_new)

# Cambiar Tuplas a listas y listas a tuplas
'''Podemos cambiar tuplas por listas y listas por tuplas. 
Una Tupla es inmutable si queremos modificar una tupla debemos cambiarla a una lista.'''
lst_fruits = list(fruits)
print(lst_fruits)
lst_fruits[0] = 'platano'
print(lst_fruits)
print(type(lst_fruits))
lst_fruits.insert(3, 'melocoton') # ¿?¿? No puedo insertar elementos a la lista?

# Comprobar elementos en una Tupla
print('banana' in fruits)

# Union de 2 Tuplas en una nueva
vegetales = ('Tomato', 'potato', 'Carrot')
fr_veg = fruits + vegetales
print(fr_veg)

# Eliminación de Tuplas
'''No es posible eliminar un solo elemento en una tupla, 
pero es posible eliminar la tupla en sí usando del'''
print(vegetales)
del vegetales
#print(vegetales) el interprete nos dice que no existe la tupla vegetales



#       EJERCICIOS DIA_6 --- NIVEL 1
print('\tEJERCICIOS DIA_6')
'''
1._Crear una tupla vacía
2._Crea una tupla que contenga los nombres de amigos y otro de amigas
3._Unir tuplas de amigos y amigas y asignarlas a amigos
4._¿Cuántos hermanos tiene usted?
5._Modifique la tupla de hermanos y agregue el nombre de su padre y madre y asígnelo a family_members
6._Desempaquetar amigos separados de padres'''
tp_vacia = ()
print(tp_vacia)
amigos = ('Escandar', 'Sergio', 'Javi', 'Jesus', 'Tomás', 'Ruicillo')
amigas = ('Patricia', 'Elena', 'Raquel', 'Noemi')
amigos = amigos + amigas
print(amigos)
print(len(amigos))
lst_amig = list(amigos)
family = ['papa', 'mama']
family = family + lst_amig
print(family)
family_members = tuple(family)
print(family_members)
padres = family_members[0:2]
amiguitos = family_members[2:]
print(padres)
print(amiguitos)

#       EJERCICIOS DIA_6 --- NIVEL 2
'''
1._ Cree tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
2._ Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
3._ Rebane el artículo o artículos del medio de la tupla food_stuff_tp o la lista food_stuff_lt.
4._ Cortar los primeros tres elementos y los últimos tres elementos de la lista food_staff_lt
5._ Eliminar completamente la tupla food_staff_tp
7._ Compruebe si existe un elemento en la tupla:
        a) Comprobar si 'manzana' es una fruta
        b) Comprobar si 'manzana' es un vegetal'''
        
frutas = ('manzana', 'pera', 'platano', 'melocoton')
verdur = ('Tomate', 'Patata', 'Zanahoria')
prod_animal = ('Ternera', 'Lechazo', 'Cochinillo')
food_stuff = frutas + verdur + prod_animal
print(food_stuff)
lst_food = list(food_stuff)
print(type(lst_food))
new_food_tp = food_stuff[4:7]
print(new_food_tp)
print(lst_food[0:3])
print(lst_food[-3:])
del food_stuff
print('manzana' in frutas)
print('manzana' in verdur)