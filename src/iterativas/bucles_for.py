# Bucles for y sentencia range



frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)



for i in range(5):
    print(i)



# números del 3 al 7
for i in range(3, 8):
    print(i, end=" ")  # 3 4 5 6 7

print()  # Salto de línea

# números pares del 2 al 10
for i in range(2, 11, 2):
    print(i, end=" ")  # 2 4 6 8 10

print()  # Salto de línea

# cuenta regresiva
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1



#Iterando sobre indices

nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")



nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")



#iterando sobre cadenas

mensaje = "Python"
for letra in mensaje:
    print(letra)


#Iterando sobre diccionarios

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# iterando sobre pares clave-valor
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# iterando solo sobre valores
for valor in usuario.values():
    print(valor)    



#Comprensiones de listas con for

# crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]



#Bucles for anidados

# crear una matriz de multiplicación 3x3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salto de línea después de cada fila
    
    
    
#Casos prácticos

# ejemplo 1: Calcular la suma de los primeros n números  
n = 10
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")  # 55

# ejemplo 2: Encontrar números primos en un rango
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(f"Números primos entre 2 y 19: {primos}")  # [2, 3, 5, 7, 11, 13, 17, 19]

# ejemplo 3: Procesamiento de datos
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# encontrar el día más caluroso
max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

# calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

# días con temperatura superior al promedio
for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")



    