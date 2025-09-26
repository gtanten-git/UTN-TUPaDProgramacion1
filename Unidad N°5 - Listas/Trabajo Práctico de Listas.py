# Ejercicio 1
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.
import random

# Se genera lista con 10 notas aleatorias entre 1 y 10
notas = [random.randint(1,10) for n in range(10)]
# Se definen las variables a utilizar
suma = 0
max = notas[0]
min = notas[0]
# Se muestra la lista notas con un ciclo for
for n in notas:
    print(n)
# Suma de notas y búsqueda del máximo
for i in range(len(notas)):
    suma += notas[i]
    if max < notas[i]:
        max = notas[i]
    elif min > notas[i]:
        min = notas[i]
# Imprime el promedio y las notas mínimas y máximas
print(f"El promedio es: {suma / len(notas)}")
print(f"La nota más alta es: {max}, y la nota más baja: {min}")

# Ejercicio 2
# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# Definición de variables
productos = []
# Se crea un mensaje para insertar en un marco visual
mensaje = "Ud. ingresó los siguientes productos"
marco = ""
# Solicitud de productos al usuario dentro del bucle
for n in range(5):
    producto = input("Ingrese producto (letras y números): ")
    if producto.isalnum():
        productos.append(producto)
# Orden alfabético con la función sorted()
productos = sorted(productos)
# Se calcula cantidad de caracteres del mensaje para definir el marco, luego se imprime
for n in range(len(mensaje)):
    marco += "*"
print()
print(marco)
print(mensaje)
print(marco)
print()
# Se muestras los productos
for producto in range(len(productos)):
    print(f"{producto + 1}. {productos[producto]}")
print()
print(marco)
# Bucle que muestra la opción de eliminar
while True:
    op = input("Ingrese producto que desee eliminar (q para salir): ")
    if op == "q":
        break
    try:
        op = int(op)
        print(f"Se eliminó: {productos[op - 1]}")
        productos.remove(productos[op - 1])
        break
    except:
        print("Debe ingresar opción válida numérica")
        continue
print()
# Se muestra lista resultante
for n in productos:
    print(n)
print()

# Ejercicio 3
# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.
import random
# Se genera lista aleatoria
num = [random.randint(1,100) for n in range(15)]
# Se definen variables
num_pares = []
num_impares = []
# Verificación de paridad y adición a lista correspondiente
for n in range(len(num)):
    if num[n] % 2 == 0:
        num_pares.append(num[n])
    else:
        num_impares.append(num[n])
# Se imprimen cantidad de números pares e impares y la lista de cada uno
print(f"Cantidad de números pares: {len(num_pares)}")
for n in num_pares:
    print(n, end=" ")
print()
print(f"Cantidad de números impares: {len(num_impares)}")
for n in num_impares:
    print(n, end=" ")
print()

# Ejercicio 4
# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado

datos = [1, 3, 5, 7, 1, 9, 5, 3]
datos_sin_repeticion = []
# Verificación de que cada elemento de la lista no esté en en la lista sin repeticiones
# Si no se encuentra, se añade nuevo elemento
for n in range(len(datos)):
    if datos[n] not in datos_sin_repeticion:
        datos_sin_repeticion.append(datos[n])
# Imprime lista original y lista sin repeticiones
print("Lista original")
for n in datos:
    print(n, end=" ")
print()
print("Lista sin elementos repetidos")
for n in datos_sin_repeticion:
    print(n, end=" ")

# Ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# Se importa librería os para utilizar la opción cls (limpiar pantalla)
import os
import time
# Se define lista de nombres, mensaje y marco para presentar recuadro visual
estudiantes = ["Lorena", "Diego", "Juana", "Cristian",
               "Lucrecia", "Juan", "Micaela", "Pablo"]
mensaje = "Listado de estudiantes actuales"
marco = ""
for n in mensaje:
    marco += "*"
# Ciclo while del menú
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Impresión del título
    print()
    print(marco)
    print(mensaje)
    print(marco)
    print()
    # Muestra la lista de estudiantes con ciclo for
    for estudiante in range(len(estudiantes)):
        print(f"{estudiante + 1}. {estudiantes[estudiante]}")
    print()
    print(marco)
    # Solicitud de opciones al usuario
    print("Ingrese opción para continuar (a: agregar estudiante, e: eliminar estudiante, s: salir)")
    op = input("Su opción: ")
    # Se convierte a minúsculas
    op.lower()
    # Solicitud de opción al usuario
    match op:
        case "a":
            estudiantes.append(input("Ingrese nuevo estudiante: "))
            continue
        case "e":
                try:
                    # Ingreso de estudiante a eliminar
                    num_estudiante = int(input("Ingrese número de estudiante a eliminar: "))
                    if 1 <= num_estudiante <= len(estudiantes):
                        print(f"Se eliminó: {estudiantes[num_estudiante - 1]}")
                        estudiantes.remove(estudiantes[num_estudiante - 1])
                        time.sleep(2)
                        continue
                except:
                    print("Opción inválida")
                    time.sleep(2)
                    continue        
        case "s":
            break
        case _:
            print("Opción no válida")
            time.sleep(2)
print()

# Ejercicio 6
# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

import random
# Se genera lista de números aleatoria
num = [random.randint(1,100) for n in range(7)]
# Se muestra lista original
for n in num:
    print(n, end=" ")
print()
# Definir último número
ultimo = num[len(num) - 1]
# Con un ciclo descendente de uno en uno, se reordena la lista
for n in range(len(num) - 1, -1, -1):
    num[n] = num[n -1]
# Se establece primer elemento, último de la lista original
num[0] = ultimo
for n in num:
   print(n, end=" ")

# Ejercicio 7
# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

import random
# Se genera matriz de temperaturas 7 x 2
temperaturas = [[random.randint(-2, 30) for i in range(2)] for i in range(7)]
# Se define lista de días de la semana
dia = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Se define variables
temp_max = 0
temp_min = 0
variacion = 0
amplitud = 0
suma_max = 0
suma_min = 0
dia_mayor_amplitud = []
# Ciclo for para establecer temperaturas mínimas y máximas, se reacomoda
for n in range(len(temperaturas)):
    if temperaturas[n][0] <= temperaturas[n][1]:
        temp_max = temperaturas[n][1]
        temp_min = temperaturas[n][0]
    elif temperaturas[n][0] > temperaturas[n][1]:
        temp_max = temperaturas[n][0]
        temp_min = temperaturas[n][1]
    # Se imprime día, temperatura mínima y máxima
    print(f"Día: {dia[n]}")
    print(f"Temperatura mínima: {temp_min}")
    print(f"Temperatura máxima: {temp_max}")
    # Suma de temperaturas
    suma_max += temp_max
    suma_min += temp_min
    # Cálculo de variación y generación de lista para determinar amplitud mayor y día
    variacion = temp_max - temp_min   
    if variacion > amplitud:
            amplitud = variacion
            dia_mayor_amplitud.clear()
            dia_mayor_amplitud.append([dia[n], amplitud])
    elif variacion == amplitud:
            dia_mayor_amplitud.append([dia[n], amplitud])
# Promedio de temperaturas
print(f"El promedio de temperaturas mínimas es: {round(suma_min/len(temperaturas), 2)}°C. El promedio de temperaturas máximas es: {round(suma_max/len(temperaturas), 2)}°C")
# Se imprime día o días de mayor amplitud térmica
if len(dia_mayor_amplitud) > 1:
    print(f"Los días de mayor amplitud térmica fueron: ", end= " ")
    for n in range(len(dia_mayor_amplitud)):
        print(f"{dia_mayor_amplitud[n][0]},", end=" ")
    print(f"con una amplitud de: {dia_mayor_amplitud[n][1]}°C")
else:
    print(f"El día de mayor amplitud térmica fue: {dia_mayor_amplitud[0][0]}, con una amplitud de: {dia_mayor_amplitud[0][1]}°C")


# Ejercicio 8
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

import random
# Se definen variables
promedios_materia = [0 for n in range(3)]
suma_estudiante = 0
suma_materia = 0
contador = 1
# Se genera matriz de estudiantes con notas de materias
notas = [[random.randint(1, 10) for i in range(3)] for i in range(5)]
# Se imprime notas por estudiante y se calcula la suma de notas por estudiante y la suma para calcular los promedios por 
# materia
for n in range(len(notas)):
    print(f"Notas estudiante N°{n+1}: ", end= " ")
    for m in range(len(notas[n])):
        print(notas[n][m], end= " ")
        suma_estudiante += notas[n][m]
        promedios_materia[m] += notas[n][m]
    # Se imprime promedio por estudiante
    print()
    print(f"Promedio estudiante N°{n+1}: {round(suma_estudiante/(m+1), 2)}")
    print()
    # Se reinicia suma para nuevo estudiante
    suma_estudiante = 0
# Se imprime promedios de cada materia
for n in range(len(promedios_materia)):
    print(f"Promedio Materia N°{n + 1}: {promedios_materia[n]/len(notas)}")

# Ejercicio 9
# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

import os
import time
# Se define matriz que contiene todas las combinaciones posibles de tateti
combinaciones = [[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]], [[0, 0], [0, 1], [0, 2]],
                 [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
                 [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]]]
# Se define lista de contadores para cada jugador
contadores = [[0 for i in range(2)] for i in range(9)]
# Se definen variables para crear matriz visual vacía y marco
marco =""
caracter = " - "
# Se genera matriz visual con caracter -
vacio = [[caracter for i in range(3)] for i in range(3)]
# Se definen caracter para cada jugador
jugador_1 = " X "
jugador_2 = " O "
# Se define estado del aviso, turno y título
aviso = False
turno = ""
titulo = "Ta-Te-Ti - Por consola"
# Se definen listas de jugadas realizadas para cada jugador
pos_jug_1 = []
pos_jug_2 = []
# Se define variables de estado de repetido y contador de jugador O
repetido = False
cont_O = 0
# Se define el marco visual
for n in titulo:
    marco += "*"
# Se limpia pantalla y se imprime marco con título
import os
import time
# Se define matriz que contiene todas las combinaciones posibles de tateti
combinaciones = [[[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]], [[0, 0], [0, 1], [0, 2]],
                 [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
                 [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]]]
# Se define lista de contadores para cada jugador
contadores = [[0 for i in range(2)] for i in range(9)]
# Se definen variables para crear matriz visual vacía y marco
marco =""
caracter = " - "
# Se genera matriz visual con caracter -
vacio = [[caracter for i in range(3)] for i in range(3)]
# Se definen caracter para cada jugador
jugador_1 = " X "
jugador_2 = " O "
# Se define estado del aviso, turno y título
aviso = False
turno = ""
titulo = "Ta-Te-Ti - Por consola"
# Se definen listas de jugadas realizadas para cada jugador
pos_jug_1 = []
pos_jug_2 = []
# Se define variables de estado de repetido y contador de jugador O
repetido = False
cont_X = 0
# Se define el marco visual
for n in titulo:
    marco += "*"
# Se limpia pantalla y se imprime marco con título
os.system("cls")
print(marco)
print(titulo)
print(marco)
# Se ingresa nombres de jugadores 
nombre_jugador_1 = input("Ingrese nombre del primer jugador: ")
nombre_jugador_2 = input("Ingrese nombre del segundo jugador: ")

while True:
    # Se limpia pantalla y se reimprime el marco visual con el título
    os.system("cls")
    print(marco)
    print(titulo)
    print(marco)
    # Se imprime matriz de jugadas
    for n in range(len(vacio)):
        for m in vacio[n]:
            print(m, end= " ")
        print()
    print()
    # Aviso para indicar ganador
    if aviso:
            print("TA - TE - TI", win)
            print()
            break
    # Orden de turno
    if turno == nombre_jugador_1:
        turno = nombre_jugador_2
    else:
        turno = nombre_jugador_1
    #En caso de que el segundo contador llegue a 4 jugadas, define empate
    if cont_X == 5:
        print("Empate")
        time.sleep(2)
        break
    # Turno del jugador
    print(f"{turno}")
    # Solicitud de fila y columna, en caso de ingresar q, salida
    fila = input(f"Ingrese fila: ")
    if fila.lower() == "q":
        print("Hasta luego!!!")
        time.sleep(2)
        break
    columna = input(f"Ingrese columna: ")
    if columna.lower() == "q":
        print("Hasta luego!!!")
        time.sleep(2)
        break
    try:
        # Se enumeran los índices
        fila = int(fila) - 1
        columna = int(columna) - 1
        # Si fila o columna no se encuentran dentro de la matriz
        if not (-1 < fila <= 2) or not (-1 < columna <= 2):
            print("Debe ingresar un valor entre 1 y 3 para filas y columnas")
            # Se define turno
            turno = nombre_jugador_2 if turno == nombre_jugador_1 else nombre_jugador_1
            time.sleep(2)
            continue
        # Se define lista de ingreso fila y columna (jugada)
        lista_ingreso = [fila, columna]
        # Se adiciona jugada a la lista del jugador correspondiente
        pos_jug_1.append(lista_ingreso) if turno == nombre_jugador_1 else pos_jug_2.append(lista_ingreso)
        # Verifica si jugada está en alguna lista de jugadas
        repetido = lista_ingreso in pos_jug_2 if turno == nombre_jugador_1 else lista_ingreso in pos_jug_1
        # Si repetido es verdadero, solicita re ingreso
        if repetido:
            print()
            print("Posición Ocupada - Re ingrese")
            print()
            turno = nombre_jugador_2 if turno == nombre_jugador_1 else nombre_jugador_1
            time.sleep(2)
            continue
        # Se escribe posición en la matriz visual según turno y se cuenta cantidad de jugadas
        # jugador 2
        if turno == nombre_jugador_1:
            vacio[fila][columna] = jugador_1
            cont_X += 1
        else: 
            vacio[fila][columna] = jugador_2
            
        # Se cuentan jugadas dentro de las combinaciones, en caso de que cada contador por combinación
        # cumple la condición ( 3 en línea) aviso se pone en True para mostrar mensaje al ganador.
        for i in range(len(combinaciones)):
            if lista_ingreso in combinaciones[i]:
                if turno == nombre_jugador_1:
                    contadores[i][0] += 1
                else:
                    contadores[i][1] += 1
                for n in range(len(contadores[i])):
                    if contadores[i][n] == 3: 
                        aviso = True
                        win = turno
                        break
    except:
        # Si hay una excepción
        print("Opción inválida")
        turno = nombre_jugador_2 if turno == nombre_jugador_1 else nombre_jugador_1
        time.sleep(2)
        continue

# Ejercicio 10
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana

import random
# Se genera lista de ventas por día de la semana para 4 productos
ventas = [[ round(random.randint(5, 30), 2)for i in range(4)] for i in range(7)]
# Lista de contadores a 0
total_vendido = [0 for i in range(4)]
# Lista total de cada día a 0
total_dia = [0 for i in range(7)]
# Lista de días de la semana
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
mayor_venta = 0
dia_mayores_ventas = []
producto_mas_vendido = 0
producto_mas_vendido_string = ""
# Se imprime tabla de productos por día
print()
print("Productos ", end="  ")
for dia in semana:
    print(dia, end="  ")
print()
for n in range(len(ventas[0])):
    print(f"Producto {n + 1} ", end=" ")
    relleno = ""
    for m in range(len(ventas)):
        
        print(f"{relleno}{ventas[m][n]}", end="")
        relleno = " " * (len(semana[m]) - len(str(ventas[m][n])) + 2)
    print()
# Cálculo total vendido por producto en una semana y en el día de todos los productos
for dia in range(len(ventas)):
    for producto in range(len(ventas[dia])):
        total_vendido[producto] += ventas[dia][producto]
        total_dia[dia] += ventas[dia][producto]
print()
# Se imprime total vendido por producto y se calcula producto/s más vendido en la semana
# Se genera string para imprimir
print("Total vendido por producto: ")
for n in range(len(total_vendido)):
    print(f"Producto {n + 1}: {round(total_vendido[n], 2)} unidades")
    if producto_mas_vendido < total_vendido[n]:
        producto_mas_vendido = total_vendido[n]
        producto_mas_vendido_string = ""
        producto_mas_vendido_string = f"Producto {n + 1} con {total_vendido[n]}"
    elif producto_mas_vendido == total_vendido[n]:
        producto_mas_vendido_string = producto_mas_vendido_string + f"y {semana[n]} con {total_vendido[n]}"
print()
# Se calcula día/s de mayor/es venta/s
for n in range(len(ventas)):
    if total_dia[n] > mayor_venta:
        dia_mayores_ventas.clear()
        mayor_venta = total_dia[n]
        dia_mayores_ventas.append([semana[n], mayor_venta])
    elif total_dia[n] == mayor_venta:
        dia_mayores_ventas.append([semana[n], mayor_venta])   
print()
# Se imprime por pantalla
print(f"El/los días con mayores ventas totales fue/fueron: ")

for n in range(len(dia_mayores_ventas)):
    print(f"{dia_mayores_ventas[n][0]} con {dia_mayores_ventas[n][1]} ", end= " ")
print("unidades")
print(f"El producto más vendido fue: {producto_mas_vendido_string} unidades")
print()