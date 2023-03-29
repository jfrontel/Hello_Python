# LISTAS EN PYTHON

'''Hay cuatro tipos de datos de coleccion en Python:

--Tupla: es una coleccion ordenada e inmutable o inmodificable. Permite miembros duplicados.
--Conjunto: es una coleccion desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. 
    No se permiten miembros duplicados.
--Diccionario: es una coleccion desordenada, cambiable (modificable) e indexada. No hay miembros duplicados.

--Lista: es una coleccion ordenada y cambiable (modificable). Permite miembros duplicados.
Una lista es una coleccion de diferentes tipos de datos. 
Una lista puede estar vacia o puede tener diferentes elementos de tipo de datos.'''

# Como Crear una lista
lst = list()
lst_1 = []

# Listas con valores iniciales. Usamos len() para encontrar la longitud de una lista.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print(len(fruits))

# Las listas pueden tener elementos de diferentes tipos de datos
lst_2 = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] 


# Acceder a los elementos de la lista mediante la indexacion positiva o negativa
print(fruits[0])
print(fruits[1])
print(fruits[len(fruits) - 1])
print(fruits[-1])
print(fruits[-4])

# Desempaquetar elementos de una lista
a, b, c, d = fruits
print(a)
print(c)
country = ['Spain', 'Germany', 'France', 'Canada', 'EE.UU', 'Angola', 'Etiopia']
Sp, Ge, Fr, Ca, Usa, An, Et = country
print(Usa)
print(Sp)

# Cortar elementos de una lista
print(country[0:3])
print(country[3:5])
print(country[5:])
print(country[-3: -1])
print(country[-3:])

# Revertir el orden
print(country[::-1])


# Modificacion de listas
country[0] = 'Espahna'
country[1] = 'Alemania'
country[2] = 'Francia'
print(country)

# Comprobacion de elementos en una lista
print('Francia' in country)


''' Adicion de elementos a una lista
Para agregar un elemento al final de una lista existente, usamos el metodo --> append(), syntax:
lst = list()
lst.append(item) '''
country.append('Italia')
print(country)

'''Insertar elementos en una lista en un indice especifico en una lista --> insert(), syntax:
lst = ['item1', 'item2']
lst.insert(index, item) '''
country.insert(3, 'Grecia')
print(country)
asia = ['China', 'Tailandia']
#country.append(asia)
#country.insert(-1, asia)
print(country)

# Eliminar elementos de una lista --> remove()
country.remove('Italia')
country.remove(country[0])
print(country)

# Eliminacion de elementos en indice deseado mediante pop()
country.pop(0)
print(country)

# Eliminacion de elementos mediante del: para eliminar por indice o rango
frutas = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print(frutas)
del frutas[0]
print(frutas)
del frutas[1:3]
print (frutas)

# Vaciar una lista
#frutas.clear()
#print(frutas)          --Solo para version de Python 3 en adelante--

# Copiar una lista
frutas_copy = frutas
print(frutas_copy)
del frutas_copy[0]
print(frutas)    #Si hacemos esta asignacion, lo que hagamos a la copia tb se hace a la original
# La forma correcto de hacerlo para tener dos listas independiente es:
#frut_copy = frutas.copy()       -- disponible desde Python 3.3. --
#print(frut_copy)

frutas_nueva = list(frutas)
del frutas_nueva[0]
print(frutas)
print(frutas_nueva)

# Unir o concatenar listas
positive_nb = [1, 2, 3, 4, 5]
zero = [0]
negative_nb = [-5,-4,-3,-2,-1]
print(positive_nb + zero + negative_nb)
all_nb = positive_nb + zero + negative_nb
print(all_nb)
print(frutas + country)

# Unirse usando el metodo extend() El metodo extend() permite agregar una lista en una lista.
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# Contar elementos de una lista --> count() devuelve el numero de veces que aparece un elemento en una lista
print(fruits.count('banana'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Encontrar indice de un elemento de la lista
print(fruits.index('Tomato'))
print(ages.index(24))          # Indice de la primera vez que ocurre

# Invertir el orden de una lista --> reverse() 
fruits.reverse()
print(fruits)
print(fruits[::-1])     #Otra forma de hacerlo

''' Ordenar listas 
Para ordenar listas, podemos usar el metodo sort() o las funciones integradas sorted(). 
El metodo sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. 
Si un argumento del metodo sort() reverse es igual a verdadero, ordenara la lista en orden descendente.
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]



#       EJERCICIOS DIA_5 --- NIVEL_1    
print('\t*** EJERCICIOS DE LISTA EN PYTHON ***')
# 1._ Declarar una lista vacia
# 2._ Declarar una lista con mas de 5 elementos
# 3._ Encuentra la longitud de tu lista
# 4._ Obtenga el primer elemento, el elemento del medio y el ultimo elemento de la lista
lst_ej1 = []
tabaco = ['Ducados', 'Camel', 'Fortuna', 'Marlboro', 'Chesterfield']
print(len(tabaco))
print(tabaco[0])
print(tabaco[2])
print(tabaco[4])
# 5._ Declare una lista y ponga su(nombre, edad, altura, estado civil, direccion)
lst_ej5 = ['Jorge', '39', '1.84', 'Casado', 'Melancolia'] 
print(lst_ej5)
# 6._ Modifica un elemento de la lista e imprime
tabaco[0] = 'Winston'
print(tabaco)
# 7._ Agrega elemento a la lista
tabaco.append('Ducados')
print(tabaco)
# 8._ Inserte elemento en el medio de la lista
tabaco.insert(len(tabaco)/2, 'Celtas')
print(tabaco)
# 9._ Cambiar uno de los nombres a mayusculas
tabaco[3] = tabaco[3].upper()
print(tabaco)
# 10._ Compruebe si en la lista existe un determinado elemento
print('Camel' in tabaco )
# 11._Ordenar una lista
number = [2, 7, -1, 7.1, 0, 9, 4, 100, 2]
number.sort()
print(number)
# 12._ Invierta la lista
numbe = [2, 7, -1, 7.1, 0, 9, 4, 100, 2]
#number.sort(reverse = True)
#print(number)
numbe.sort()            # Segunda forma de hacerlo
print(numbe[::-1])  
# 13._ Quita los dos primeros elementos y los dos ultimos
print(tabaco)
del tabaco[0:1]
print(tabaco)
del tabaco[len(tabaco) - 2: len(tabaco)]
print(tabaco)
# 14._ Une las siguientes listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#       EJERCICIOS DIA_5 --- NIVEL 2

# 1._ La siguiente es una lista de las edades de 10 estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
'''Ordena la lista y encuentra la edad minima y maxima
Agregue la edad minima y la edad maxima nuevamente a la lista
Encuentre la edad mediana (un elemento intermedio o dos elementos intermedios divididos por dos)
Encuentre la edad promedio (suma de todos los elementos dividida por su numero)
Encuentre el rango de las edades (max menos min)
Compare el valor de (min - promedio) y (max - promedio), use el metodo abs()'''
print(ages)
ages.sort()
print(ages[0])
print(ages[len(ages) - 1])
ages.append(ages[0])
ages.append(ages[len(ages) - 2])
print(ages)
sum_ages = sum(ages) / len(ages)
print(sum_ages)