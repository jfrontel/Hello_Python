# String en Python

'''El texto es un tipo de datos de cadena. 
Todos los datos entre comillas simples, dobles o triples son cadenas.'''

# Crear una cadena
letra = 'P'
print(letra)
print(len(letra))
print(type(letra))
frase = 'Esto es una cadena de caracteres'
print(frase)
print(len(frase))
print(type(frase))
#Cadena multilinea con comillas triples
oracion = '''En un lugar de la mancha
de cuyo nombre no quiero acordarme, 
vivia un hidalgo caballero'''
print(oracion)
#Concatenar Cadenas
nombre = 'Jorge'
apellido = 'Frontela'
space = ' '
print(nombre + space + apellido)
nom_comp = nombre + space + apellido # Lo podemos guardar en variable
print('Tu nombre es: ', nom_comp)


'''Secuencias de espape en Python
En Python y otros lenguajes \ seguido de un caracter es una secuencia de escape.
\n: nueva linea
\t: Tabulador significa (8 espacios)
\\: barra invertida
\': Una frase (')
\": comillas dobles (")'''

calderon = "Que es la vida. Un frenesi.\n\tQue es la vida. Una ilusion, una sombra, una ficcion;\n\t\t y el mayor bien es pequehno; que toda la vida es suehno, y los suehnos, suehnos son.\n"
print(calderon)


'''Formato de la cadena:    Formato antiguo %
%s - Cadena (o cualquier objeto con una representacion de cadena, como numeros)
%d - Enteros
%f - Numeros de punto flotante
"%.number of digitsf" - Num de punto flotante con precision fija'''

nomb = 'Jorge'
apell = 'Frontela'
leng = 'Python'
print('Yo soy %s %s. Y estoy estudiando %s' %(nomb, apell, leng))
form_antig = 'Yo soy %s %s. Y estoy estudiando %s' %(nomb, apell, leng)
print(form_antig)

rad = 10
pi = 3.141592
area = pi * rad **2
print(area)
print('%s: El area de un circulo de radio %d es %.4f' %(nomb, rad, area))

'''Formato de la cadena:    Formato nuevo str.format %'''
a = 1
b = 7
print('Yo soy {} {}. Yo estudio {}' .format(nomb, apell, leng))
print('{} + {} = {}' .format(a, b, a + b))
print('{}: El area de un circulo de radio {} es {:.4f}' .format(leng, rad, area))


'''Cadenas como secuencias de caracteres
La forma mas sencilla de extraer caracteres individuales de cadenas 
es descomprimirlos en las variables correspondientes.'''

#Desempaquetar
lang = 'Python'
a, b, c, d, e, f = lang
print(a)
print(f)

#Acceso a caracteres por indice
print(lang[0])
print(lang[5]) 
print(lang[-1]) #Empezar por el final
print(lang[-6])

#Cortar cadenas
print(lang[0:3])
print(lang[3:6])
print(lang[-1:-4])  #No sirve para caracteres por el final al menos en version 2.7
print(lang[-4:])    #thon
print(lang[-6:])    #Python
print(lang[2:])     #thon

#Invertir una cadena
str_inv = "Por cien canhones por banda"
print(str_inv[::-1])
print(str_inv[::7])  # Esto me coge una letra de cada 7 (empieza en 0) NO invierte
print(str_inv[::-2]) # Esto me coge una letra de cada 2 y me lo invierte

#Saltar caracteres al cortar
pto = lang[0:6:2] # De la cadena Python desde index 0 a 6 cogeme de 2 en 2
print(pto)



'''Funciones de Cadenas
Hay muchos metodos  y funciones de cadena que nos permiten formatear cadenas.'''

# capitalize (): convierte el primer caracter de la cadena en letra mayuscula
str_soled = 'mUchos anhos despues, frente al peloton de fusilamiento, el Coronel Aureliano Buendia...'
print(str_soled.capitalize()) # **Por lo visto pone las demas en minusculas
print(str_soled[0:9].capitalize())

# count(): devuelve la cantidad de veces que encuentra una subcadena en la cadena, cuenta(subcadena, inicio=.., final=..). 
#El inicio es una indexacion inicial para contar y el final es el ultimo indice para contar.
print(str_soled.count('B'))     #1
print(str_soled.count('s'))     #5
print(str_soled[0:15].count('s'))

# endswith(): comprueba si una cadena termina con un final especifico, Devuelve True o False
print(str_soled.endswith('...'))   #True
print(str_soled.endswith('Buendia'))   #False

# expandtabs(): reemplaza el caracter de tabulacion con espacios, el tamanho de tabulacion predeterminado es 8. 
# Toma el argumento de tamanho de tabulacion
str_tab = "Barrie postula que\t,antes de nacer,\ttodos los bebes son aves;\tde aqui nace la figura de\tPeter Pan"
print(str_tab.expandtabs())
print(str_tab.expandtabs(2))
print(str_tab.expandtabs(20))   # No entiendo muy bien esto

# find(): Devuelve el indice de la primera aparicion de una subcadena, si no se encuentra devuelve -1
print(str_soled.find('B'))
print(str_soled.find('m'))
print(str_soled.find('fr'))
print(str_soled.find('Buen'))
print(str_soled.find('x'))

# rfind(): Devuelve el indice de la ultima aparicion de una subcadena, si no se encuentra devuelve -1
print(str_soled.rfind('U'))
print(str_soled.rfind('C'))

# format(): formatea la cadena en una salida mas agradable
print('Yo soy {} {}. Yo estudio {}' .format(nomb, apell, leng))

# index (): devuelve el indice mas bajo de una subcadena, los arg adicionales indican el indice inicial y final
# Si no se encuentra la subcadena, genera un valueError.
str_soledad = 'muchos anhos despues, frente al peloton de nhfusilamiento, el Coronel Aureliano Buendia...'
sub_cad = 'nh'
print(str_soledad.index('nh'))
print(str_soledad.index(sub_cad))
print(str_soledad.index(sub_cad, 10, 80))

# rindex(): Devuelve el indice mas alto de una subcadena, los argumentos adicionales indican el indice inicial y final
print(str_soledad.rindex('nh'))
print(str_soledad.rindex(sub_cad))
print(str_soledad.rindex(sub_cad, 10, 80))

# isalnum(): comprueba el caracter alfanumerico
x = 'Escuela42'
y = '42'
z = 'Escuela'
print(x.isalnum()) #True
print(y.isalnum()) #True
print(z.isalnum()) #True

# isalpha(): comprueba si todos los elementos de cadena son caracteres alfabeticos (az y AZ)
print(x.isalpha()) #False
print(y.isalpha()) #False
print(z.isalpha()) #True

# isdecimal(): comprueba si todos los caracteres de una cadena son decimales (0-9)
'''
#Algo va mal  podria ser la version 2.7 de Python
#print(x.isdecimal()) 
#print(y.isdecimal()) 
#print(z.isdecimal()) 
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed'''

# isdigit(): comprueba si todos los caracteres de una cadena son numeros (0-9 y algunos otros caracteres Unicode)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# slower(): Comprueba si todos los caracteres del alfabeto en la cadena estan en minuisculas
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Comprueba si todos los caracteres del alfabeto en la cadena estan en mayusculas
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# swapcase (): convierte todos los caracteres en mayusculas a minusculas y todos los caracteres en minusculas 
# a caracteres en mayusculas
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# title (): devuelve una cadena de titulo en mayusculas
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# strip (): elimina todos los caracteres dados desde el principio y el final de la cadena
challenge = 'thirty days of pythoonnn'
print(challenge.strip('onthy')) 

# join(): Devuelve una cadena concatenada
str_1 = ' '
str_11 = '...'
str_2 = 'Mundo'
print(str_1.join(str_2))
print(str_11.join(str_2))
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print('\n'.join(web_tech))

# replace (): reemplaza la subcadena con una cadena dada
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split (): divide la cadena, utilizando la cadena dada o el espacio como separador
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# comienza con (): comprueba si la cadena comienza con la cadena especificada
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False



#      EJERCICIOS DIA_4

# 1._ Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str_ej1 = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(str_ej1))
print('Thirty ' + 'Days ' + 'Of ' + 'Python')
# 2._ Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str_ej2 = ['Codificacion', 'Para', 'Todos']
print((' '.join(str_ej2)))
# 3._ Declare una variable llamada empresa y asignele un valor inicial "Codificacion para todos".
# 4._ Print the variable company using print().
# 5._ Print the length of the company string using len() method and print().
empresa = 'Codificacion para todos'
print(empresa)
print(len(empresa))
# 6._ Cambie todos los caracteres a letras mayusculas usando el metodo upper().
# 7._ Cambie todos los caracteres a letras minusculas usando el metodo lower().
print(empresa.upper())
print(empresa.lower())
# 8._ Use los metodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
# 9._ Cut (corte) la primera palabra de la cadena Coding For All.
sub_caden = empresa[0:12]
print(sub_caden)
# 10._ Verifique si la cadena Coding For All contiene una palabra Coding usando el metodo index, find u otros metodos.
str_ej10 = 'Coding For All'
sub_ej10 = 'Coding'
print(str_ej10.find(sub_ej10))
print(str_ej10.index(sub_ej10))
# 11._ Reemplace la palabra codificacion en la cadena 'Coding For All' por Python.
# 12._ Reemplace la palabra All en la cadena 'Coding For All' por Everyone.
print(str_ej10.replace('Coding', 'Python'))
print(str_ej10.replace('All', 'Everyone'))
# 13._ Split the string 'Coding For All' using space as the separator (split()).
var = (str_ej10.split(' '))
print(var)
# 14._ Cual es el caracter en el indice 0 en la cadena Coding For All
# 15._ Cual es el ultimo indice de la cadena Coding For All
print(str_ej10[0])
print(str_ej10[-1])
# 16._ Use index para determinar la posicion de la primera aparicion de C en Coding For All.
print(str_ej10.index('C'))
# 17._ Use rfind para determinar la posicion de la ultima aparicion de l en Coding For All People.
print(str_ej10.rfind('l'))
# 18._ Corta la frase 'porque porque porque' en la siguiente oracion: 
# 'No puedes terminar una oracion con porque porque porque es una conjuncion'
str_ej18 = 'No puedes terminar una oracion con porque porque porque es una conjuncion'
q = str_ej18.index('porque')
r = str_ej18.rindex('porque') + len('porque')
print(str_ej18[q:r])
s = str_ej18.find('porque')
t = str_ej18.rfind('porque') + len('porque')
print(str_ej18[s:t])
# 19._ La siguiente lista contiene los nombres de algunas de las bibliotecas de Python: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Unase a la lista con un hash con cadena de espacio.
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(lista))
# 20._ Use la secuencia de escape de nueva linea para separar las siguientes oraciones
str_ej20 = 'I am enjoying this challenge.'
str_ej201 ='I just wonder what is next.'
print(str_ej20 + '\n' + str_ej201)
