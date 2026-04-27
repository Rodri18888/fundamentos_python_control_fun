# Return

def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado  # Devuelve el valor y termina la función

area = calcular_cuadrado(4)
print(area)  # Imprime: 16



#Funciones sin return

def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return explícito

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None



#Retornando múltiples valores

def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")        # Imprime: Suma: 108
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42



resultado = estadisticas(datos)
print(type(resultado))  # Imprime: <class 'tuple'>
print(resultado)        # Imprime: (108, 18.0, 4, 42)
print(resultado[1])     # Imprime: 18.0 (accediendo al promedio)



#Return anticipado

def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada

    # Este código solo se ejecuta si b no es cero
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None



#Patrones comunes con return

# función booleana (predicado)

def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

# Uso en condicionales
usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")  # Imprime: Acceso denegado
    


# transformación de datos

def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"
    print(formato_nombre("ana", "garcía"))  # Imprime: GARCÍA, Ana



# cálculos y procesamiento    

def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")  # Imprime: Precio con IVA: 121.0 €



# return con estructuras de datos

def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares)  # Imprime: [2, 4, 6, 8, 10]

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados)  # Imprime: {1: 1, 2: 4, 3: 9, 4: 16}



#Buenas practicas con return

# coherencia en los tipos de retorno**: Es recomendable que una función devuelva siempre el mismo tipo de datos, o tipos compatibles.

# Enfoque mejorado: siempre devuelve una lista (vacía en caso de error)
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error

    return [num for num in numeros if num > 0]



# documentar el valor de retorno**: Es importante que quede claro qué devuelve la función.

def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """
    return precio - (precio * porcentaje / 100)


# evitar efectos secundarios**: Las funciones que devuelven valores no deberían, idealmente, modificar el estado global o realizar acciones como imprimir.

# Mejor: separar la obtención del resultado de su presentación
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función



# usar return temprano para casos especiales**: Esto mejora la legibilidad del código.

def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    return "Insuficiente"



#Ejemplo práctico: Función de conversión de temperatura

def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """
    # Validación de parámetros
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si origen y destino son iguales, no hay conversión necesaria
    if origen == destino:
        return valor

    # Primero convertimos a Celsius como unidad intermedia
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # origen es 'C'
        celsius = valor

    # Luego convertimos de Celsius a la unidad de destino
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # destino es 'C'
        return celsius

# Ejemplos de uso
print(convertir_temperatura(25, 'C', 'F'))    # Imprime: 77.0
print(convertir_temperatura(98.6, 'F', 'C'))  # Imprime: 37.0
print(convertir_temperatura(0, 'C', 'K'))     # Imprime: 273.15
print(convertir_temperatura(20, 'X', 'Y'))    # Imprime: None