import random
# Bucles while

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")



#Bucles controlados por eventos
 
objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")
    


#Bucles con condición de salida variable    

saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break  # Salimos del bucle inmediatamente

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Volvemos al inicio del bucle

    saldo -= gasto

print(f"Saldo final: {saldo}€")



#Bucles infinitos controlados
while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")
        
        
        
#Procesamiento de datos con while 

def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # 120



#Simulaciones y aproximaciones

def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2  # Valor inicial
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero/aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # 5.000000
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # 2.645751



#Validación de entrada con while

def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")



#Patrones con while

def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)



#Consideraciones de rendimiento

"""
¡CUIDADO! Bucle infinito
contador = 1
while contador <= 5:
    print(contador)
     Olvidamos incrementar contador
"""

# corregido
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Importante: actualizar la variable de control
    
    
    
#Comparación con bucles for

# usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# equivalente con for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")    