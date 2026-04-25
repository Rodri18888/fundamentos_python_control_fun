# expresiones condicionales:



edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)



a = 1

b = 2

print("El máximo es:", a if a > b else b)



edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)



numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']



dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)



