#Ejercicio_1
print("Hola mundo")

#Ejercicio_2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio_3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio_4
radio = float(input("Ingresa radio del círculo: "))
print("El área del círculo es: ", 3.14 * radio ** 2, "y su perímetro es: ", 2 * 3.14 * radio)

#Ejercicio_5
segundos = float(input("Ingrese segundos a convertir en horas: "))
print("Equivale a: ", segundos / 3600, " horas")

#Ejercicio_6 con secuenciales
numero = int(input("Ingresa un número entero: "))
print(f"{numero} . 0 = {numero * 0}")
print(f"{numero} . 1 = {numero * 1}")
print(f"{numero} . 2 = {numero * 2}")
print(f"{numero} . 3 = {numero * 3}")
print(f"{numero} . 4 = {numero * 4}")
print(f"{numero} . 5 = {numero * 5}")
print(f"{numero} . 6 = {numero * 6}")
print(f"{numero} . 7 = {numero * 7}")
print(f"{numero} . 8 = {numero * 8}")
print(f"{numero} . 9 = {numero * 9}")
print(f"{numero} . 10 = {numero * 10}")

#Ejercicio_7
num1 = int(input("Ingresa primer número entero distinto de 0: "))
num2 = int(input("Ingresa segundo número entero distinto de 0: "))
print(f"El resultado de la suma es: {num1 + num2}")
print(f"El resultado de la resta del primero menos el segundo es: {num1 - num2}")
print(f"El resultado de la resta del segundo menos el primero es: {num2 - num1}")
print(f"El resultado de la división del primero con el segundo: {num1 / num2}")
print(f"El resultado de la división del segundo con el primero: {num2 / num1}")
print(f"El resultado del producto es: {num1 * num2}")

#Ejercicio_8
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso: "))
print(f"Tu IMC es: {peso / altura ** 2}")

#Ejercicio_9
temperatura = float(input("Ingresa temperatura en grados Celsius: "))
print(f"La temperatura en Farenheit es : {9 / 5 * temperatura + 32}")

#Ejercicio_10
num1 = float(input("Ingresa primer número: "))
num2 = float(input("Ingresa segundo número: "))
num3 = float(input("Ingresa tercer número: "))
print(f"El promedio de los números es: {(num1 + num2 + num3) / 3}")