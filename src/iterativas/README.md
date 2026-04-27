# Estructuras Iterativas en Python
 
Ejercicios sobre estructuras de control iterativo en Python. Cada archivo cubre un concepto distinto de la leccion 6, desde los bucles basicos hasta el control de flujo con sentencias especiales.
 
## Requisitos
 
- Python 3.13 o superior (verificar con `python --version`)
- Sin dependencias externas, solo libreria estandar de Python
## Como ejecutar los ejercicios
 
Todos los comandos se ejecutan desde dentro de la carpeta `iterativas/`. Una vez ahi, el comando para correr cualquier archivo es:
 
```bash
python nombre_del_archivo.py
```
 
Para ubicarte en la carpeta correcta desde la terminal (ejemplo en mi computador):
 
```bash
cd C:\Users\Luis\Documents\fundamentos_python_control_fun\src\iterativas
```
 
---
 
## Ejercicios
 
### bucles_for.py
 
```bash
python bucles_for.py
```
 
**Que hace:**
Cubre el uso del bucle `for` en sus distintas formas. Empieza recorriendo listas elemento por elemento, luego introduce la funcion `range()` con sus tres variantes: solo con el limite final, con inicio y fin, y con paso personalizado, incluyendo cuenta regresiva con paso negativo. Tambien muestra como acceder a indices usando `range(len())` y la alternativa mas clara con `enumerate()`. Se trabaja la iteracion sobre cadenas caracter por caracter y sobre diccionarios usando los metodos `items()`, `keys()` y `values()`. Hacia el final incluye comprensiones de listas, bucles anidados para generar tablas de multiplicar, y casos practicos como sumar los primeros n numeros, encontrar numeros primos en un rango y procesar una lista de temperaturas para obtener el dia mas caluroso y el promedio.
 
---
 
### bucles_while.py
 
```bash
python bucles_while.py
```
 
**Que hace:**
Trabaja el bucle `while`, que a diferencia del `for` no recorre una secuencia fija sino que se repite mientras una condicion sea verdadera. Los ejemplos muestran el patron basico con un contador, la validacion de entrada del usuario hasta que escriba un numero valido, y un juego de adivinanza con limite de intentos. Tambien se cubren bucles con condicion de salida variable usando `break` y `continue` dentro del mismo cuerpo, bucles infinitos controlados con `while True`, y el calculo de factorial. Se incluyen dos algoritmos numericos: aproximacion de raiz cuadrada por el metodo de Newton y validacion de entradas en rango con manejo de excepciones. Al final hay una comparacion directa entre resolver el mismo problema con `while` y con `for`, para entender cuando conviene cada uno.
 
---
 
### break_continue.py
 
```bash
python break_continue.py
```
 
**Que hace:**
Explica como alterar el comportamiento normal de un bucle usando `break` y `continue`. Con `break` el bucle termina inmediatamente al cumplirse una condicion, sin procesar las iteraciones restantes. El archivo muestra esto con una busqueda en lista, un menu que espera que el usuario escriba "salir", y una funcion para determinar si un numero es primo saliendo en cuanto encuentra un divisor. Con `continue` el bucle no termina sino que salta la iteracion actual y pasa a la siguiente, lo que se usa para filtrar temperaturas negativas, evitar divisiones por cero y ignorar valores no numericos en una lista mixta. Tambien se combinan ambas sentencias en el mismo bucle, se muestra como afectan unicamente al bucle mas interno cuando hay bucles anidados, y se usa una bandera booleana para salir de multiples niveles. Incluye dos ejemplos avanzados: validacion de contrasena caracter por caracter y procesamiento de transacciones segun su estado.
 
---
 
### pass_else.py
 
```bash
python pass_else.py
```
 
**Que hace:**
Introduce dos caracteristicas que Python tiene en bucles y que no existen en la mayoria de otros lenguajes. La sentencia `pass` no hace nada, pero sirve como marcador de posicion cuando la sintaxis exige una instruccion y aun no hay codigo que poner ahi, o cuando se quiere dejar explicito que no hacer nada en cierto caso es intencional. La clausula `else` en bucles se ejecuta una unica vez cuando el bucle termina de forma normal, es decir, sin que se haya ejecutado un `break`. Si el bucle termina por `break`, el bloque `else` se omite por completo. Esto lo hace ideal para busquedas donde se quiere confirmar si se encontro o no el elemento, y para validaciones donde se quiere asegurar que todos los elementos cumplieron una condicion. El archivo muestra `else` tanto en bucles `for` como en `while`, y termina con un ejemplo integrado de validacion de formulario que combina `pass`, `else`, `break` y manejo de excepciones en un mismo flujo.