# Parametros y argumentos

def saludar_persona(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}!")

saludar_persona("Ana")  # "Ana" es un argumento



#Tipos de parámetros

# parámetros posicionales

def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)  # 100 va a precio_base, 0.21 va a impuesto
print(f"Precio final: {total}")  # Imprime: Precio final: 121.0



# parámetros con valores predeterminados

def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?



# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"# Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"


# parámetros por nombre
 
def dividir(dividendo, divisor):
    return dividendo / divisor

# Usando argumentos posicionales
resultado1 = dividir(10, 2)  # resultado1 = 5.0

# Usando argumentos por nombre
resultado2 = dividir(divisor=2, dividendo=10)  # resultado2 = 5.0



def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)
