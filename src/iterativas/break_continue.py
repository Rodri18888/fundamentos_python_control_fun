from typing import TypedDict

# Break - continue

#La sentencia break

for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")



#Casos de uso prácticos para break

# búsqueda eficiente: Detener la búsqueda una vez encontrado el elemento deseado.

def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice

    return -1  # Si llegamos aquí, el elemento no está en la lista

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

#validación de entrada con salida: Permitir al usuario salir de un proceso de entrada.

while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

# optimización de algoritmos: Evitar cálculos innecesarios.

def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # No es primo, salimos inmediatamente

    return True  # Si llegamos aquí, es primo



#La sentencia continue

for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")

#Casos de uso prácticos para continue

# filtrado de datos: Procesar solo los elementos que cumplen cierta condición.

temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")


# manejo de casos especiales: Evitar procesar casos que requieren tratamiento diferente.

numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")


# validación de datos: Saltar entradas inválidas en un proceso de análisis.

datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")



#Combinando break y continue

numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break

#Uso en bucles anidados

for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")


encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo


#Consideraciones de rendimiento y legibilidad, Refactorización de bucles

"""
# En lugar de:
for item in lista:
    if condicion1(item):
        continue
    if condicion2(item):
        break
    # Más código...

# Considera:
def procesar_item(item):
    if condicion1(item):
        return False
    if condicion2(item):
        return None
    # Procesar y devolver resultado
    return resultado

for item in lista:
    resultado = procesar_item(item)
    if resultado is None:
        break
    if resultado is False:
        continue
    # Usar resultado... 

"""
"""
# Versión ineficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
# Seguimos recorriendo toda la lista aunque ya encontramos el objetivo

# Versión eficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
        break  # Terminamos inmediatamente
"""

#Ejemplos prácticos avanzados

# ejemplo 1: Validación de contraseña


def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue  # Optimización: ya verificamos este requisito

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Probamos algunas contraseñas
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]
for pwd in contraseñas:
    if validar_contraseña(pwd):
        print(f"'{pwd}' es válida")
    else:
        print(f"'{pwd}' NO es válida")


# ejemplo 2: Procesamiento de transacciones

class Transaccion(TypedDict):
    id: int
    monto: int
    estado: str 


transacciones: list[Transaccion] = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0

for t in transacciones:
    # Ignoramos transacciones no completadas
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue

    # Verificamos montos válidos
    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue

    # Procesamos la transacción
    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

print(f"Total procesado: {total_procesado}€")
