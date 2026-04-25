# bucles for y sentencia range



frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)



for i in range(5):
    print(i)



# Números del 3 al 7
for i in range(3, 8):
    print(i, end=" ")  # 3 4 5 6 7

print()  # Salto de línea

# Números pares del 2 al 10
for i in range(2, 11, 2):
    print(i, end=" ")  # 2 4 6 8 10

print()  # Salto de línea

# Cuenta regresiva
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1



#iterando sobre indices

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


#iterando sobre diccionarios

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")  




    