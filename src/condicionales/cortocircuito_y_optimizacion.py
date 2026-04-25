# evaluacion de cortocircuito y optimizacion:

#uso para prevenir errores
lista = []

if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")



dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")



#optimizacion del rendimiento

# if usuario_esta_autenticado and tiene_permiso_avanzado and realizar_operacion_cara():
    # Ejecutar operación



#consideraciones sobre efectos secundarios
acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")



if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")



if acceso_permitido or (acceso_registrado and True):
    print("Acceso concedido.")



#evaluacion en expresiones condicionales
 
# resultado = funcion_pesada() if condicion else valor_por_defecto



#uso con any() y all()



numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")



condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")    
    
