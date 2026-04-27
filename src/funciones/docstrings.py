import doctest
import random
import string
# Docstrings

def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b



#Estructura básica de un docstring

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)



#Accediendo a los docstrings

# Acceder al docstring directamente
print(calcular_promedio.__doc__)

# O usar la función help
help(calcular_promedio)



#Estilos de docstrings
 
# estilo Google


def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]



# estilo reStructuredText (reST)

def convertir_a_celsius(fahrenheit):
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    :param fahrenheit: Temperatura en grados Fahrenheit
    :type fahrenheit: float
    :return: Temperatura en grados Celsius
    :rtype: float
    """
    return (fahrenheit - 32) * 5/9



# estilo NumPy/SciPy

def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]
    
    
    
#Docstrings para funciones simples

# docstring de una linea

"""
def es_mayor_de_edad(edad):
    Determina si una persona es mayor de edad (18 años o más).
    return edad >= 18
"""
   
   

# docstring mas completo

def es_mayor_de_edad(edad):
    """
    Determina si una persona es mayor de edad.

    Args:
        edad: Edad de la persona en años

    Returns:
        True si la edad es 18 o mayor, False en caso contrario
    """
    return edad >= 18 
 
 
 
 #Docstrings para funciones con comportamiento especial
 
def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a: El numerador
        b: El denominador

    Returns:
        El resultado de la división a/b, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
    """
    if b == 0:
        return None
    return a / b



#Herramientas para trabajar con docstrings

"""
- help(): Muestra la documentación de un objeto
- pydoc: Módulo que genera documentación a partir de docstrings
- doctest: Permite ejecutar ejemplos incluidos en los docstrings como pruebas
"""    

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
        base: Longitud de la base del triángulo
        altura: Altura del triángulo

    Returns:
        El área del triángulo

    Ejemplos:
        >>> area_triangulo(4, 3)
        6.0
        >>> area_triangulo(5, 8)
        20.0
    """
    return (base * altura) / 2



# doctest

doctest.testmod()  # Ejecuta todos los ejemplos en los docstrings como pruebas



#Buenas prácticas para escribir docstrings

# sé conciso pero completo**: Incluye toda la información necesaria sin ser excesivamente detallado.


def generar_contraseña(longitud=8):
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))


# usa verbos en presente**: Describe lo que la función hace, no lo que hará o hizo.


# Bien
def validar_usuario(nombre):
    """Verifica si el nombre de usuario cumple con los requisitos."""

# Evitar
"""
def validar_usuario(nombre):
    Esta función verificará si el nombre de usuario cumple con los requisitos.
"""

# documenta los tipos de datos**: Especifica qué tipos de datos espera la función y qué tipo devuelve.

def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())



# incluye ejemplos prácticos**: Los ejemplos ayudan a entender rápidamente cómo usar la función.

def formatear_nombre(nombre, apellido):
    """
    Formatea un nombre completo en formato "Apellido, Nombre".

    Args:
        nombre: Nombre de la persona
        apellido: Apellido de la persona

    Returns:
        Cadena formateada como "Apellido, Nombre"

    Ejemplo:
        >>> formatear_nombre("Juan", "Pérez")
        'Pérez, Juan'
    """
    return f"{apellido}, {nombre}"



# documenta excepciones**: Si tu función puede lanzar excepciones, indícalo en el docstring.

def obtener_elemento(lista, indice):
    """
    Obtiene un elemento de una lista por su índice.

    Args:
        lista: La lista de elementos
        indice: Posición del elemento a obtener (comienza en 0)

    Returns:
        El elemento en la posición especificada

    Raises:
        IndexError: Si el índice está fuera del rango de la lista
    """
    return lista[indice]



#Ejemplo práctico: Función con docstring completo

def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):
    """
    Calcula el precio final de un producto aplicando descuento e impuesto.

    Primero aplica el descuento sobre el precio base y luego
    añade el impuesto sobre el precio con descuento.

    Args:
        precio_base (float): Precio original del producto
        descuento (float, opcional): Porcentaje de descuento (0-100). Predeterminado: 0
        impuesto (float, opcional): Tasa de impuesto (0-1). Predeterminado: 0.21

    Returns:
        float: Precio final después de aplicar descuento e impuesto

    Raises:
        ValueError: Si alguno de los parámetros tiene un valor negativo

    Ejemplos:
        >>> calcular_precio_final(100)
        121.0
        >>> calcular_precio_final(100, 10)
        108.9
        >>> calcular_precio_final(100, 10, 0.1)
        99.0
    """
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")

    precio_con_descuento = precio_base * (1 - descuento/100)
    precio_final = precio_con_descuento * (1 + impuesto)

    return precio_final 
    
    
