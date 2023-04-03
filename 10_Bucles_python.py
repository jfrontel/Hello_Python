# BUCLES EN PYTHON

'''La vida está llena de rutinas. En programación también hacemos muchas tareas repetitivas. 
Para manejar tareas repetitivas, los lenguajes de programación usan bucles. 
--> while loop
--> for loop '''

# while loop
'''Usamos la palabra reservada while para hacer un bucle while. Se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condición dada. 
Cuando la condición se vuelve falsa, las líneas de código después del ciclo continuarán ejecutándose.'''
# Break: Usamos break cuando queremos salir o detener el bucle.
a = 5
while a > 0:
    print("a = %d" %(a))
    a = a - 1
    if (a == 2):
        break
else:
    print('Hemos llegado a 0.')
    
# Continue: con la instrucción continuar podemos omitir la iteración actual y continuar con la siguiente:
'''
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1 ''' #NO FUNCIONA POR QUE?



# for loop
'''Una palabra clave for se usa para hacer un bucle for, similar a otros lenguajes de programación, pero con algunas diferencias de sintaxis. 
Loop se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena).'''

#Para bucle con lista
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#Para bucle con string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

#Para bucle con tupla
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    
#Bucle for con diccionario 
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)
    
# Bucles en Set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
    
# Break para bucle for
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") 
print('outside the loop')

# La función de rango
'''La función range() se utiliza como lista de números. El rango (inicio, fin, incremento).
De forma predeterminada, comienza desde 0 y el incremento es 1. 
La secuencia de rango necesita al menos 1 argumento (fin). Creando secuencias usando rango'''
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))   
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# Bucle For anidado
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
            
# For Else
# Si queremos ejecutar algún mensaje cuando finaliza el ciclo, usamos else.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
    
#Pass
'''En python, cuando se requiere una declaración (después del punto y coma), pero no nos gusta ejecutar ningún código allí, podemos escribir la palabra pass para evitar errores. 
También podemos usarlo como marcador de posición, para declaraciones futuras.'''
for number in range(6):
    pass


#       EJERCICIOS DIA_10 --- NIVEL 1
print("\n\tEJERCICIOS DIA_10 --- NIVEL 1")
# 1._ Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while.
print("Itere de 0 a 10 usando el bucle for")
for num in range(11):
    print(num)
print("Itere de 0 a 10 usando el bucle while")
x = 0
while x < 11:
    print("%d" %x)
    x = x + 1
# 2._ Escriba un bucle que haga siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
print("Escriba un bucle que haga siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:")
letra = '#'
x = 0
while x < 8:
    print("%s" %(x*letra))
    x = x + 1

# 3._ Use bucles anidados para crear lo siguiente:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
print("# 3._ Use bucles anidados para crear lo siguiente:")
letra
q = '#'
i = 0
j = 8
while i < 8:
    while j == 8:
        print("%s" %(j*q))
        break
    i = i + 1
    
#4._Imprime el siguiente patrón:
'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100'''

for w in range(11):
    print("%d x %d = %d" %(w, w, w*w))
    
#5._ Iterar a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprimir los elementos.
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for x in lista:
    print(x)
    
#6._ Use for loop para iterar de 0 a 100 e imprimir solo números pares

for g in range(101):
    if g % 2 == 0:
        print(g)
        

#       EJERCICIOS DIA_10 --- NIVEL 2
print("\n\tEJERCICIOS DIA_10 --- NIVEL 2")

#1._ Use for loop para iterar de 0 a 100 e imprimir la suma de todos los números.
r = 0
for s in range(101):
    r = r + s
print("La suma total es %d" %(r ))

#2._Use for loop para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todas las probabilidades.
r = 0
p = 0
for s in range(101):
    if(s % 2 == 0):
        r = r + s
    else:
        p = p + s
print("La suma de pares es %d\nLa suma de impares es %d" %(r,p ))
