
# Ejercicio N°1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Solicitud de edad
edad = input("Ingrese su edad: ")

try:
    #Convertir edad en entero y reasignar a la misma variable
    edad = int(edad)

    #Corroborar si es negativo
    if edad < 1:
        print("La edad es un número negativo, ingrese números enteros mayores a 0")
    
    #En caso de no ser negativo comprobar si es mayor de edad
    elif edad >= 18:
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")
except:
    print("Error en el ingreso de su edad, ingrese números enteros mayores a 0")


# Ejercicio N°2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# Definir límtes
NOTA_MIN_APROBADO = 6
NOTA_MAX_APROBADO = 10
NOTA_MIN_DESAPROBADO = 0

# Solicitud de nota al usuario
nota = input("Ingrese su nota: ")

try: 
    # Convertir nota a float
    nota = float(nota)

    # Comprobar aprobado, desaprobado o fuera de rango
    if NOTA_MIN_APROBADO<= nota <= NOTA_MAX_APROBADO:
        print("Aprobado")
    elif NOTA_MIN_DESAPROBADO <= nota < NOTA_MIN_APROBADO:
        print("Desaprobado")
    else:
        print("La nota se encuentra fuera de rango 0 a 10")

except:
    print("Error al ingresar la nota. Por favor, reingrese")


# Ejercicio N°3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# Solicitar número al usuario
numero = input("Ingrese número: ")

try:
    
    # Comparar el módulo del número: 0 par, distinto de 0 impar
    if int(numero) % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

except:
    print("Error al ingresar número, por favor, ingrese solo números enteros")



# Ejercicio N°4:  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# Niño/a: menor de 12 años.
# Adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.

# Definir límites etarios
NINO_MAX_AGE = 12
NINO_MIN_AGE = 0
ADOLESCENTE_MAX_AGE = 18
ADULTO_MIN_AGE = 30

# Solicitar edad al usuario
edad = input("Ingrese su edad: ")

try:
    # Convertir a entero
    edad = int(edad)

    # Comprobar si la edad es un número negativo
    if edad < 0:
        print("La edad es un número negativo")

    # Comprobar si edad corresponde a un niño
    elif NINO_MIN_AGE <= edad < NINO_MAX_AGE:
        print("Niño/a")

    # Comprobar si edad corresponde a un adolescente
    elif NINO_MAX_AGE <= edad < ADOLESCENTE_MAX_AGE:
        print("Adolescente")
    
    # Comprobar si edad corresponde a un adulto/a joven
    elif ADOLESCENTE_MAX_AGE <= edad < ADULTO_MIN_AGE:
        print("Adulto/a joven")

    # De no corresponder otra opción, la edad corresponde a un adulto/a
    else:
        print("Adulto/a")
except:
    print("Error al ingresar edad. La edad debe ser un número entero no negativo")

# Ejercicio N°5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# Definir límites superior e inferior
PASS_MAX = 14
PASS_MIN = 8

# Solicitud de contraseña al usuario
password = input("Por favor, ingrese contraseña: ")

# Contar caracteres
cantidad_caracteres = len(password)

# Comprobar si la contraseña tiene entre 8 y 14 caracteres
if PASS_MIN <= cantidad_caracteres <= PASS_MAX:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio N°6: El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. 

from statistics import mode, median, mean
import random

# Generar lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Ordenar de menor a mayor la lista, solo para fines de visualización, no importa el orden al momento
# del cálculo.
numeros_aleatorios.sort()

# Calcular la media
media = mean(numeros_aleatorios)

# Calcular la mediana
mediana = median(numeros_aleatorios)

# Calcular la moda
moda = mode(numeros_aleatorios)

# Imprimir la lista generada y los valores de la media, mediana y moda
print(f"Lista de números: \n{numeros_aleatorios}\nLa media es: {media}\nLa mediana es: {mediana}\nLa moda es: {moda}")

# Comprobar el sesgo
if moda < mediana < media:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")

# Ejercicio N°7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Definir caracter final y variables VOCALES como string de vocales
CARACTER_FINAL = "!"
VOCALES = "aeiou"

# Solicitud de palabra o frase al usuario
palabra = input("Ingrese palabra o frase: ")

# Contar cantidad de letras de la palabra o frase
cantidad_letras = len(palabra)

# Determinar última letra de la frase, como en Python un string puede manejarse como una lista de
# letras consecutivas, la última letra será: cantidad de letras de la frase menos uno.
ultima_letra = palabra[cantidad_letras - 1]

# Convertir la última letra en minúscula para realizar la comparación y no exista errores si el usuario
# ingresa el texto en mayúsculas, a su vez, reasignar el resultado a la misma variable.
ultima_letra = ultima_letra.lower()

# Comprobar si la última letra está en el string de vocales, si es verdadero agregar ! al final
# Si es falso, imprimir la frase tal cual la ingresó el usuario.
# También pueden utilizarse elif por cada letra.
if ultima_letra in VOCALES:
    print(palabra + CARACTER_FINAL)
else:
    print(palabra)

# Ejercicio N°8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Definir opciones
OP_UNO = "1. Nombre en mayúsculas"
OP_DOS = "2. Nombre en minúsculas"
OP_TRES = "3. Primera letra mayúscula"

# Solicitar nombre al usuario
nombre = input("Ingrese nombre: ")

# Solicitar opción al usuario
opcion = input(f"\nIngrese Opción: \n{OP_UNO}\n{OP_DOS}\n{OP_TRES}\n")

# Comparar opción con string de números y determinar cada acción según selección. De no corresponder
# se muestra opción incorrecta.

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción incorrecta")

# Ejercicio N°9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Solicitar ingreso de magnitud al usuario 
magnitud = input("Ingrese magnitud del terremoto en escala de Ritcher: ")

try:
    # Convertir a float
    magnitud = float(magnitud)

    # Según la escala, se presenta detalle.
    if 0 <= magnitud < 3:
        print("Muy leve - Imperceptible")
    elif 3 <= magnitud < 4:
        print("Leve - Ligeramente perceptible")
    elif 4 <= magnitud < 5:
        print("Moderado - Sentido por personas, pero generalmente no causa daños")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte - Puede causar daños en estructuras débiles")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte - Puede causar daños significativos")
    elif magnitud >= 7:
        print("Extremo - Puede causar graves daños a gran escala")

except:
    print("Error, debe ingresar números mayores a cero")

# Ejercicio N°10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitar hemisferio al usuario
hemisferio = input("Ingrese Hemisferio N: Norte - S: Sur ")
# Convertir a mayúsculas para adaptar s o n
hemisferio = hemisferio.upper()

# Comprobar hemisferio
if hemisferio == "N" or hemisferio == "S":
    try:
        # Solicitar mes y dia, convertir a entero
        mes = input("Ingrese mes del año: ")
        mes = int(mes)
        dia = input("Ingrese día del mes: ")
        dia = int(dia)
       
        # Comprobar si el mes está entre 1 y 12 y el día entre 1 y 31
        if 1 <= mes <= 12:
            if 1 <= dia <= 31:
                # Comprobar los meses de cambio de estación 12, 3, 6, 9 y el día de cambio
                if mes == 12:
                    if dia >= 21:
                        # Mensaje según hemisferio
                        print("Invierno") if hemisferio == "N" else print("Verano")
                    else:
                        print("Otoño") if hemisferio == "N" else print("Primavera")
                elif mes == 3:
                    if dia >= 21:
                        print("Primavera") if hemisferio == "N" else print("Otoño")
                    else:
                        print("Invierno") if hemisferio == "N" else print("Verano")
                elif mes == 6:
                    if dia >= 21:
                        print("Verano") if hemisferio == "N" else print("Invierno")
                    else:
                        print("Primavera") if hemisferio == "N" else print("Otoño")
                elif mes == 9:
                    if dia >= 21:
                        print("Otoño") if hemisferio == "N" else print("Primavera")
                    else:
                        print("Verano") if hemisferio == "N" else print("Invierno")
                # Comprobar los meses intermedios de cada estación
                elif mes == 1 or mes == 2:
                    print("Invierno") if hemisferio == "N" else print("Verano")
                elif mes == 4 or mes == 5:
                    print("Primavera") if hemisferio == "N" else print("Otoño")
                elif mes == 7 or mes == 8:
                    print("Verano") if hemisferio == "N" else print("Invierno")
                elif mes == 10 or mes == 11:
                    print("Otoño") if hemisferio == "N" else print("Primavera")                       
    except:
        print("Error al ingresar mes o dia, ingrese números enteros del 1 al 12 para el mes y del 1 al 31 para el día")
else:
    print("Error al elegir Hemisferio: N = Norte - S = Sur")