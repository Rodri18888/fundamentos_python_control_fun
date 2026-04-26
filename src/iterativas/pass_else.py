# Pass y else en bucles

#Setencia pass

# Bucle que no hace nada para los números pares
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")


"""
def procesar_datos():
    # Función aún no implementada
    pass

# El programa puede seguir ejecutándose sin errores
procesar_datos()



modo_debug = False

for i in range(100):
    # En modo normal, no mostramos nada durante el procesamiento
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

    # Código de procesamiento real aquí        
"""

#La cláusula else en bucles

"""
La sintaxis es:

for elemento in secuencia:
    # Cuerpo del bucle
else:
    # Código que se ejecuta si el bucle termina normalmente


O para bucles `while`:


while condicion:
    # Cuerpo del bucle
else:
    # Código que se ejecuta si el bucle termina normalmente

"""

# ¿cuándo se ejecuta el else?

# Buscar un número primo en una lista
numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")



numeros = [4, 6, 7, 8, 10]  # Ahora incluimos el 7

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")



#Casos de uso prácticos

# validación con else

def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# Probamos con diferentes listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida


# búsqueda con else

def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario

base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]

buscar_usuario(base_usuarios, "Ana")      # Existente
buscar_usuario(base_usuarios, "Roberto")  # Nuevo


# combinando pass y else

def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # Explícitamente no hacemos nada con valores normales
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"

# Probamos con diferentes conjuntos de datos
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # Uno excede el umbral


# uso en bucles while**

def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

encontrar_raiz(25)  # Debería converger rápidamente
encontrar_raiz(612, 5)  # Probablemente no converja en 5 iteraciones



#Consideraciones de estilo y legibilidad

"""
# Versión más explícita con comentarios
for item in coleccion:
    if condicion(item):
        # Procesamiento normal
        procesar(item)
    else:
        pass  # Intencionalmente no hacemos nada con estos elementos
else:
    # Este bloque se ejecuta si el bucle termina normalmente (sin break)
    print("Procesamiento completado sin interrupciones")
"""



#Ejemplo integrado: Sistema de validación

def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    # Verificar campos requeridos
    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:  # Campo vacío
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        # Solo llegamos aquí si todos los campos requeridos existen y no están vacíos
        # Ahora validamos el formato de cada campo

        # Validar email
        if "@" not in datos["email"]:
            errores.append("Email inválido")

        # Validar edad
        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")

    # Validaciones opcionales
    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Explícitamente indicamos que es opcional

    # Resultado final
    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

# Probamos con diferentes formularios
formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

print(validar_formulario(formulario1))
print(validar_formulario(formulario2))