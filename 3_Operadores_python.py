# Operadores en Python

#Operadores Booleanos
#Un tipo de datos booleano representa uno de los dos valores: True o False
print(True)
print(False)

'''Operadores de Asignación
x = 5   # A x se le asigna el valor 5
x += 1  # x = x + 1
x -= 1  # x = x - 1
x *= 2  # x = x * 2
x /= 2  # x = x / 2
Otros operadores de asignacion son %=, //=, **=, &=, |=, ^=, >>= y <<=
'''

'''Operadores Aritmeticos
Suma (+): a + b
Resta(-): a - b
Multiplicación(*): a * b
División(/): a / b
Módulo (%): a % b
División eliminando resto (//): a // b
Exponencial(**): a ** b
'''
'''
# Calcular area de un circulo
radius = int(input('Radio del Circulo ='))    # radius of a circle
area_of_circle = 3.14 * (radius ** 2)         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calcular area de un rectangulo
ancho = int(input("Ancho del rectangulo = "))
largo = int(input("largo del rectangulo = "))
area_of_rectangle = ancho * largo
print('Area of rectangle:', area_of_rectangle)

# Calcular peso de un objeto o cuerpo
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calcular densidad de un liquido
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3')
'''


''' Operadores de comparación
Usamos operadores de comparación para comparar dos valores. 
Comprobamos si un valor es mayor o menor o igual a otro valor.
'''
print(3 > 2)     # El resultado sera True ya que 3 es mayor que 2
print(3 >= 2)    # True ya que 3 es mayor o igual a 2
print(3 < 2)     # False, 3 no es menor que 2
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False, 3 no es igual a 2
print(3 != 2)    # True, xq 3 no es igual a 2
print(len('Jorge') == len('Guadalupe'))  # False
print(len('Jorge') != len('Guadalupe'))  # True
print(len('Jorge') < len('Guadalupe'))   # True
print(len('hola') != len('dios'))      # False
print(len('hola') == len('dios'))      # True



'''Además del operador de comparación anterior, Python usa:
is : Devuelve verdadero si ambas variables son el mismo objeto (x es y)
is not : Devuelve verdadero si ambas variables no son el mismo objeto (x no es y)
in : Devuelve True si la lista consultada contiene un determinado elemento (x en y)
not in : Devuelve True si la lista consultada no tiene un determinado elemento (x en y)'''

print('1 is 1', 1 is 1)                     # True - Son el mismo dato
print('1 is not 2', 1 is not 2)             # True - No son el mismo dato
print('J in Jorge', 'J' in 'Jorge')         # True - J se encuentra en la string
print('G in Jorge', 'B' in 'Jorge')         # False - G mayuscula no se encuentra en la string
print('coding in coding for all', 'coding' in 'coding for all') # True - la frase contiene la palabra
print('4 is 2 ** 2:', 4 is 2 ** 2)          # True



'''Operadores logicos
A diferencia de otros lenguajes, Python usa palabras clave and, or y not como operadores lógicos. 
Los operadores lógicos se utilizan para combinar sentencias condicionales:
'''
print(3 < 5 and 1 < 5)  # True
print(3 < 5 or 4 > 1)   # True
print(not 3 < 5)        # False
print(not True)         # False 
print(not False)        # True
print(not not True)     # True
print(not not False)    # False


'''EJERCICIOS DIA_3'''
# 1._Declara tu edad como variable entera
edad = int(10)
print(type(edad))
# 2._Declara tu altura como una variable flotante
altura = float(1.85)
print(type(altura))
num_complex = complex(1 + 4j)
# 3._Declara tu altura como una variable flotante
print(type(num_complex))

# 4._Escriba un script que solicite al usuario que ingrese la base 
# y la altura del triángulo y calcule el área de este triángulo (área = 0,5 xbxh)
base = int(input('Dame la base del triangulo: '))
altura = int(input('Dame la altura del triangulo: '))
area_triangulo = (base * altura / 2)
int(area_triangulo)
print('El area del triangulo es: ', area_triangulo)

# 5._Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo.
# Calcula el perímetro del triángulo (perímetro = a + b + c).
lado_a = int(input('Dame el lado A: '))
lado_b = int(input('Dame lado B: '))
perim = (lado_a + lado_b) * 2
area = lado_a * lado_b
print('Perimetro del cuadrado: ', perim)
print('Area del cuadrado: ', area)

# 6._Encuentre la longitud de 'python' y 'dragon' y haga una declaración de comparación falsa.
print(len('python') == len('dragon'))
print(len('python') != len('dragon'))

# 7._Use un operador para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
print('on se encuentra en dragon? y en Python', 'on' in 'dragon', 'on' in 'Python')

# 8._ Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
tam = len('python')
print(float(tam))
print(type(str(tam)))

# 9._ Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no?
num = int(input('dame un numero'))
print((num % 2) is 0)

# 10._Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. 
# ¿Calcular el salario de la persona?
horas = int(input('Numero de hora: '))
tarifa = int(input('Euros por Hora: '))
print('Su sueldo sera:', horas * tarifa)

# 11._Escriba un script de Python que muestre la siguiente tabla
print('1 1 1 1 1\n2 2 4 2 4\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')
