# operadores logicos en condicionales

# and
edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")



# or
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")



# not
llueve = False

if not llueve:
    print("Podemos salir al parque.")




# combinacion de operadores logicos
edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")



# precedencia de operadores logicos (not > and > or)

#sin parentesis
a = True
b = False
c = not b

resultado = a or b and c
print(resultado)  # Imprime True



#con parentesis
resultado = (a or b) and c
print(resultado)  # Imprime True



# uso de condiciones complejas en declaraciones if



#sin operadores
usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")
        
        

#utilizando and
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")

        