#Ejercicio_1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# Límite definido en 101 para que incluya el número 100
for n in range(101):
   print(n)

#Ejercicio_2
# Desarrolla un programa que solicite al usuario un número 
# entero y determine la cantidad de dígitos que contiene.

while True:
    # Bloque try para que en caso de ingresar algo que no sea un número entero, ejecute la
    # la excepción.
    try:
        # Ingreso del número del usuario
        num = int(input("Ingrese un número entero: "))
        # Defino una variable auxiliar
        num_entero = num
        # Se puede utilizar la función abs()
        # num_entero = abs(int(num))
        # En este caso, se utiliza condicionales y luego se multiplica el número ingresado por -1 
        # cuando el número es negativo, para obtener el positivo.
        # En caso de que el número ingresado sea positivo, el algoritmo no hace nada.
        if num_entero >= 0:
            pass
        else:
            num_entero = num_entero * -1
        # División que da como resultado la parte entera, se reasigna a la misma variable.
        num_entero = num_entero // 10
        # Definir contador
        contador = 1
        # Se define estructura repetitiva hasta que el número sea > 0, que indicaría
        # que se han procesado todos los dígitos.
        while num_entero > 0:
            # Se actualiza contador de dígitos
            contador += 1
            num_entero = num_entero // 10
        # Al finalizar ciclo while, se presentan en pantalla los datos resultantes
        print(f"El número {num}, tiene {contador} dígito/s")
        # Se fuerza la salida del bucle while True que repetía el ingreso de un número, hasta
        # que este fuera un entero
        break
    except:
        # En caso de no ser un entero, se ejecuta este aviso y se continúa la ejecución del
        # ciclo while true.
        print("Se debe ingresar un número entero")
        continue


#Ejercicio_3
# Escribe un programa que sume todos los números enteros comprendidos entre dos 
# valores dados por el usuario, excluyendo esos dos valores.

# Bloque try para ingresar números enteros
try:
    num1 = int(input("Ingrese primer número: "))
    num2 = int(input("Ingrese segundo número: "))
    # Se define variable suma
    suma = 0
    # Comparación de valores para definir los límites del bucle for
    # Luego se asigna a variable suma, el valor anterior y el valor de n.
    if num1 <= num2:
        for n in range(num1 + 1, num2):
            suma = suma + n
    elif num1 >= num2:
        for n in range(num2 + 1, num1):
            suma = suma + n
    # Al finalizar, se presentan los resultados
    print(f"El resultado de la suma de todos los números comprendidos es: {suma}")
except:
    # Se ejecuta en caso de no cumplirse try, en este caso, números no enteros o
    # caracteres alfanuméricos.
    print("Debe ingresar números enteros")

# Ejercicio_4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario 
# ingrese un 0.

# Se define variable suma
suma = 0
while True:
    # Bloque try dentro del bucle while para no terminar la secuencia en caso que no se ingrese un 
    # número entero
    try:
        # Se ingresa número del usuario
        num = int(input("Ingrese número - Ingrese 0 para salir: "))
        # Se comprueba si es la condición de parada (num = 0)
        if num == 0:
            # Se presentan los resultados y se rompe el bucle while true
            # que solicitaba números.
            print(f"\nLa suma de los números ingresados es: {suma}\n")
            break
        # Se realiza la suma de los números ingresados
        suma = suma + num
    except:
        print("Ingrese solo números enteros")

# Ejercicio_5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar 
# el número.

# Se importa librería random
import random
# Se genera número aleatorio entre 0 y 9
num_aleatorio = random.randint(0,9)
# Se define contador de intentos
contador = 1
# Se inicia bucle while para ingreso de números
while True:
        # Se solicita el número al usuario, sin convertir a entero, esto es para
        # establecer una condición de parada, en este caso con el caracter q. Se puede
        # establecer también algún número fuera del rango 0 a 9.
        num = input("Adivina el número aleatorio entre 0 y 9 (q para salir): ")
        # Se verifica que no se cumpla la condición de parada (q)
        if num != "q":
            # Bloque try para verificar que lo ingresado sea un número entero
            try:
                # Se convierte a entero y se reasigna.
                num = int(num)
                # Se verifica que el número ingresado se encuentre entre 0 y 9
                # en caso contrario se continúa con el bucle
                if 0 <= num <= 9:
                    # Se verifica coincidencia con el número aleatorio generado, de ser verdadero, 
                    # se presenta el contador de intentos y se detiene el bucle, en caso de no coincidir, se 
                    # incrementa el contador de intentos y se continúa con el bucle
                    if num == num_aleatorio:
                        print("Has acertado el número. Felicitaciones!!!")
                        print(f"Cantidad de intentos: {contador}")
                        break
                    else:
                        print("No has acertado. Intenta nuevamente")
                        contador += 1
                else:
                    print("Debes ingresar números enteros entre 0 y 9")
                    continue
            except:
                 # Se presenta un mensaje en caso de no ser un entero
                 print("Debes ingresar números entre 0 y 9")
                 continue
        else:
             # Si se ingresa caracter q, se rompe el ciclo.
             break

# Ejercicio_6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# Se establece rango del bucle for, se finaliza en -1 para que incluya el valor 0, y se 
# decrementa en 2 para imprimir números pares a partir de 100
for n in range(100,-1, -2):
    print(n)

# Ejercicio_7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# En este caso se define bloque try por fuera del bucle while true, para no establecer condición de parada,
# se puede finalizar ingresando cualquier número no entero o caracter alfanumérico.
try:
    # Bucle while para realizar más de una operación hasta que se ingrese caracteres o flotantes
    while True:
        # Se ingresa número de usuario
        num = int(input("Ingrese número final (entrada distinta de números enteros = salir): "))
        # Se define variable suma
        suma = 0
        # Se verifica que el número ingresado sea > 0
        if num >= 0:
            # Se define bucle for, no se especifíca si deben o no incluír los extremos del rango, por lo
            # que el extremo superior no se incluye. El inferior (0) se incluye dado que en la suma no modifica el resultado.
            # Para incluír el número ingresado por el usuario, sumar uno a la variable num en el bucle (num + 1).
            for n in range(0, num):
                # Se actualiza la variable suma.
                suma += n
            # Al concluir bucle for, se presenta el resultado
            print(f"La suma total es: {suma}")
        else:
            # Si el número ingresado no sea >= 0, se continúa con el bucle while.
            print("Debes ingresar un número entero positivo")
            continue
except:
    # Si el número no es un entero, se presenta el mensaje y se finaliza
    print("Debes ingresar números enteros positivos")

# Ejercicio_8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Se define cantidad total de números a ingresar
NUM_TOTALES = 100
# Se definen variables contador
positivos = 0
negativos = 0
pares = 0
impares = 0
contador = 1
# Bucle mientras el contador de números enteros cumpla la condición
while contador <= NUM_TOTALES:
    # Se ingresa número del usuario sin convertir a entero para brindar condición de parada,
    # si se requiere finalizar antes de cumplir la totalidad de números.
    num = input("Ingrese número (q para salir): ")
    # Se evalúa condición de parada (q), en caso de ser verdadero, se rompe el bloque while
    if num == "q":
        break
    else:
        # En caso de no ser verdadero la condición de parada, se define bloque try para convertir
        # el número ingresado en entero
        try:
            # Se convierte a entero, de no ser posible, se ejecuta excepción.
            num = int(num)
            # Se evalúa el módulo en dos del número y de ser 0 es par, de lo contrario impar
            # Dentro se verifica si es positivo o negativo
            if (num % 2) == 0:
                pares += 1
                if num >= 0:
                    positivos += 1
                else:
                    negativos += 1
            else:
                impares += 1
                if num < 0:
                    negativos += 1
                else:
                    positivos += 1
            # Se actualiza contador, solo cuando los valores ingresados sean enteros.
            contador +=1
        except:
            # Se ejecuta cuando hay una excepción en try, en este caso un número no entero o
            # alfanumérico, luego se continúa con el bucle
            print("Debes ingresar números enteros")
            continue
# Se presentan los resultados, una vez se haya cumplido o roto el bucle while
print(f"Total de números pares: {pares}")
print(f"Total de números impares: {impares}")
print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")

# Ejercicio_9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Se define cantidad total de números a ingresar
NUM_TOTALES = 100
# Se define variable suma y contador de números
suma = 0
contador = 1
# Bucle que se ejecutará hasta que se cumplan la cantidad de números definidas.
while contador <= NUM_TOTALES:
    # Se ingresan números del usuario
    num = input("Ingrese número (q para salir): ")
    # Se evalúa condición de parada, en caso verdadero se rompe el bucle.
    if num == "q":
        break
    else:
        # Bloque try para verificar conversión a enteros y operación
        try:
            # Conversión de los números del usuario, actualización de variable suma y contador
            num = int(num)
            suma = suma + num
            contador +=1
        except:
            # De no ingresar enteros se presenta mensaje y se continúa con el bucle
            print("Debes ingresar números enteros")
            continue
# Al finalizar bucle while, se calcula promedio y se presenta en pantalla con el mensaje
promedio = suma / (contador - 1)
print(f"El promedio es: {promedio}")

# Ejercicio_10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Bloque try para manejar enteros y relizar excepción en caso contrario
try:
    # Se ingresa número del usuario
    numero = int(input("Ingrese un número entero: "))
    # Se obtiene valor absoluto
    num = abs(numero)
    # Se convierte número de usuario a string
    strNum = str(num)
    # Se cuentan la cantidad de caracteres
    cantidad_digitos = len(strNum)
    # Se define variable que contendrá el nuevo número en tipo string
    nuevo_num = ""
    # Se define bucle for decreciente, valor inicial la cantidad de caracteres, y límite inferior
    # -1 para que incluya al 0, en paso -1
    # Se concatena a la variable suma, cada caracter en sentido inverso
    for n in range(cantidad_digitos - 1, -1, -1):
        nuevo_num = nuevo_num + strNum[n]
    # Se verifica si el número era negativo, de ser verdadero se multiplica por -1 para mantener
    # el signo
    if numero < 0:
        nuevo_num = int(nuevo_num) * -1
    # Se presenta mensaje con el nuevo número inverso
    print(f"El número {numero} invertido es: {nuevo_num}")
except:
    # Se ejecuta en caso de no ingresar un número entero
    print("Debe ingresar un número entero")