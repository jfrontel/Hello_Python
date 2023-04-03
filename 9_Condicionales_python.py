# Condicionales en Python
'''
De forma predeterminada, las declaraciones en el script de Python se ejecutan secuencialmente de arriba a abajo. 
Si la lógica de procesamiento lo requiere, el flujo secuencial de ejecución se puede alterar de dos formas:
    Ejecución condicional: se ejecutará un bloque de una o más sentencias si cierta expresión es verdadera
    Ejecución repetitiva: un bloque de una o más sentencias se ejecutará de forma repetitiva siempre que cierta expresión sea verdadera. 
    En esta sección, cubriremos las declaraciones if , else y elif . 
Los operadores lógicos y de comparación que aprendimos en las secciones anteriores serán útiles aquí.'''

# if condition:
'''En python y otros lenguajes de programación, la palabra clave if se usa para verificar si una condición es verdadera y ejecutar el código de bloque. 
Recuerde la sangría después de los dos puntos.'''
a = 0
if a > 0: 
    print("a es un numero positivo")
else:
    print("a es un numero negativo")
    
# If Elif Else
'''En nuestra vida diaria, tomamos decisiones a diario. Tomamos decisiones no comprobando una o dos condiciones, sino múltiples condiciones. 
Al igual que la vida, la programación también está llena de condiciones. Usamos elif cuando tenemos múltiples condiciones.'''
if a > 0: 
    print("a es un numero positivo")
elif a < 0:
    print("a es un numero negativo")
else:
    print("a es igual a cer0")

#De forma corta
print("A es positivo") if a > 0 else print("A es negativo o Zer0")

# Condiciones anidadas
b = 3
if b > 0:
    if b % 2 == 0:
        print("B es positivo y par")
    else:
        print('B es positivo e impar')
elif b < 0:
    print("B es negativo")
else:
    print('B es Zero')    

# Condición If y operadores lógicos AND
if b > 0 and b % 2 == 0:
    print("B es positivo y par")
elif b > 0 and b % 2 != 0:
    print("B es positivo e impar")
elif b < 0:
    print("B es negativo")
else:
    print('B es Zero')
    
# Condición If y operadores lógicos OR
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


#       EJERCICIOS DIA_9 --- NIVEL 1
# 1._ Obtenga la entrada del usuario usando input ("Ingrese su edad:"). # Si el usuario tiene 18 años o más, dé su opinión: tiene edad suficiente para conducir. 
# Si es menor de 18, dé su opinión para esperar la cantidad de años que faltan. Producción:
print("\nEJERCICIOS DIA_9 --- NIVEL 1")
edad = int(input("Ingrese su edad: "))
if edad > 17:
    print("Tienes edad para conducir")
else:
    print("Te faltan %d para empezar a conducir" %(18 - edad))

# 2._ Compara los valores de my_age y your_age usando if... else. ¿Quién es mayor (tú o yo)? Use input ("Ingrese su edad:") para obtener la edad como entrada. 
# Puede usar una condición anidada para imprimir 'año' para una diferencia de edad de 1 año, 'años' para diferencias mayores y un texto personalizado si mi_edad = su_edad.
mi_edad = 39
tu_edad = int(input("Dime tu edad: "))
total = mi_edad - tu_edad
if total == 0:
    print("Tenemos la misma edad")
elif total > 0:
    if total == 1:
        print("Soy mayor por 1 año")
    else:
        print("Soy mayor por %d años" %total)
else:
    total *= -1
    if total == 1:
        print("Eres mayor por 1 año")
    else:
        print("Eres mayor por %d años" %total)

# 3._ Obtenga dos números del usuario mediante el indicador de entrada. 
# Si a es mayor que b, devuelve a es mayor que b, si a es menor, b devuelve a es menor que b, de lo contrario, a es igual a b.
num_a = int(input("deme el numero a: "))
num_b = int(input("deme el numero b: "))
if num_a > num_b:
    print("%d es mayor que %d" %(num_a, num_b))
elif num_b > num_a:
    print("%d en mayor que %d" %(num_b, num_a))
else:
    print("a y b son iguales")
    
    
#       EJERCICIOS DIA_9 --- NIVEL 2
# 1._Escriba un código que califique a los estudiantes de acuerdo con sus puntajes:
'''80-100, A
70-89, B
60-69, C
50-59, D
0-49, F'''
nota = int(input("Cual es su puntuación en el examen? "))
if nota >= 0 and nota <= 100:
    if nota >= 80 and nota <= 100:
        print("Su nota es A")
    elif nota >= 70 and nota <= 79:
        print("Su nota es B")
    elif nota >= 60 and nota <= 69:
        print("Su nota es C")
    elif nota >= 50 and nota <= 59:
        print("Su nota es D")
    else:
        print("Su nota es F")
else:
    print("Eso es imposible, escribe bien tu puntuación")

#2._ Consulta si la temporada es Otoño, Invierno, Primavera o Verano. 
# Si la entrada del usuario es: septiembre, octubre o noviembre, la estación es otoño. 
# Diciembre, enero o febrero, la temporada es invierno. 
# Marzo, Abril o Mayo, la temporada es Primavera. Junio, Julio o Agosto, la temporada es Verano
Otono = ['septiembre', 'octubre', 'noviembre']
Invierno = ['diciembre', 'enero', 'febrero']
Primavera = ['marzo', 'abril', 'mayo']
Verano = ['junio', 'julio', 'agosto']
mes = input('En que mes del año estamos? ')
if mes in Otono:
    print("Estamos es Otoño")
elif mes in Invierno:
        print("Estamos es Invierno")
elif mes in Verano:
        print("Estamos es Verano")
elif mes in Primavera:
        print("Estamos es Primavera ")
else:
    print("Ha escrito mal el mes, asegurese de que lo introduce en minusculas")

# 3._ La siguiente lista contiene algunas frutas:
fruits = ['banana', 'orange', 'mango', 'lemon']
#Si una fruta no existe en la lista, agregue la fruta a la lista e imprima la lista modificada. 
#Si la fruta existe print('Esa fruta ya existe en la lista')
var = input("Deme el nombre de una fruta: ")
if var in fruits:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(var)
print(fruits)
