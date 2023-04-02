# Set (Conjuntos) en Python

'''Conjunto es una colección de elementos distintos desordenados y no indexados. 
En Python, el conjunto se usa para almacenar elementos únicos, y es posible encontrar la unión, la intersección,
la diferencia, la diferencia simétrica, el subconjunto, el superconjunto y el conjunto disjunto entre conjuntos.'''

# Crear Conjuto (Set)
'''Usamos corchetes, {} para crear un conjunto o la función integrada set() .

Crear un conjunto vacío
st = {}
st = set()

Creación de un conjunto con elementos iniciales
st = {'item1', 'item2', 'item3', 'item4'}'''

frutas = {'manzana', 'pera', 'platano', 'melocoton'}
print(len(frutas))

#Acceder a elementos en un conjunto
#Usamos bucles para acceder a los elementos. Veremos esto en la sección de bucle.

#Comprobación de un elemento del conjunto
print("Tenemos manzana como fruta?", 'manzana' in frutas)

#Adición de elementos a un conjunto
'''Una vez que se crea un conjunto, no podemos cambiar ningún elemento pero podemos agregar elementos adicionales.'''

#Agrega un elemento usando add()
frutas.add('Fresitas')
frutas.add('mango')
print(frutas)
#Agregar múltiples elementos usando update() 
frutas.update(['melon', 'sandia', 'cerezas'])
print(frutas)
verduras = {'tomate', 'patata', 'pepino'}
frutas.update(verduras)
print(frutas)

#Eliminación de elementos de un conjunto
'''Podemos eliminar un elemento de un conjunto usando el método remove(). 
Si no se encuentra el elemento, el método remove() generará errores, por lo que es bueno verificar si el elemento existe en el conjunto dado. 
Sin embargo, el método discard () no genera ningún error.'''
if ('manzana' in frutas):
    frutas.remove('manzana')
print(frutas)
frutas.discard('naranja') #Aunque no este en el conjunto no genera errores
print(frutas)
#El método pop() elimina un elemento aleatorio de un conjunto y devuelve el elemento eliminado.
frutas.pop()
frutas.pop()
print(frutas)

#Borrado de artículos en un conjunto clear()
frutas.clear()
print(frutas)  # set vacio --> set()

#Eliminación de un conjunto
del frutas
#print(frutas)  #provoca error al no existir ningún conjunto llamado frutas

#Convertir lista en conjunto
num = ['uno', 'dos', 'tres', 'cuatro']
print(num)
num = set(num)
print(num)

#Unión de conjuntos --> Podemos unir dos conjuntos usando el método union() o update().
num_1 = {'cinco', 'seis', 'siete'}
print(num.union(num_1))
num_2 = num.union(num_1)
print(num_2)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

#Búsqueda de elementos de intersección
#La intersección devuelve un conjunto de elementos que están en ambos conjuntos. Ver el ejemplo
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3 = st1.intersection(st2) # {'item3', 'item2'}
print(st3)

#Comprobación de subconjunto y superconjunto
'''Un conjunto puede ser un subconjunto o superconjunto de otros conjuntos:
Subconjunto: issubset()
Súper conjunto: essuperconjunto'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True

#Comprobar la diferencia entre dos conjuntos
#Devuelve la diferencia entre dos conjuntos.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

#Hallar diferencias simétricas entre dos conjuntos
'''Devuelve la diferencia simétrica entre dos conjuntos. Significa que devuelve un conjunto que contiene
todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos, 
matemáticamente: (A\B) ∪ (B\A)'''
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

#Unión de conjuntos
'''Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos. 
Podemos verificar si dos conjuntos son conjuntos o disjuntos usando el método isdisjoint() .'''
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False


#       EJERCICIOS DIA_7 --- NIVEL_1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
'''
1._ Encuentre la longitud del conjunto it_companies
2._ Agregar 'Twitter' a it_companies
3._ Inserte varias empresas de TI a la vez en el conjunto it_companies
4._ Eliminar una de las empresas del conjunto it_companies
5._ ¿Cuál es la diferencia entre eliminar y descartar?'''

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
comp = {'Tinder', 'HBO'}
it_companies.update(comp)
print(it_companies)
it_companies.remove('HBO')
print(it_companies)
it_companies.clear()
del it_companies


#       EJERCICIOS DIA_7 --- NIVEL_2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
'''
1._ Une A y B
2._ Encuentra una intersección B
3._ es un subconjunto de B
4._ ¿Son A y B conjuntos disjuntos?
5._ ¿Cuál es la diferencia simétrica entre A y B?
6._ Eliminar los conjuntos por completo'''

print(A.union(B))
print(A.intersection(B))
print(B.issubset(A))
print(B.isdisjoint(A))
print(B.symmetric_difference(A))
del A
del B


#       EJERCICIOS DIA_7 --- NIVEL_3
age = [22, 19, 24, 25, 26, 24, 25, 24]
'''
1._ Convierta las edades en un conjunto y compare la longitud de la lista y el conjunto, ¿cuál es más grande?
2._ Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y conjunto
3._ Soy profesora y me encanta inspirar y enseñar a la gente. ¿Cuántas palabras únicas se han usado en la oración? 
Use los métodos de división y configure para obtener las palabras únicas.'''
age_set = set(age)
print(len(age))
print(len(age_set))