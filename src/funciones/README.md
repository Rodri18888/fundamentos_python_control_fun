# Funciones en Python
 
Ejercicios sobre funciones en Python. Cada archivo cubre un concepto distinto de la leccion 7, desde la definicion basica hasta la documentacion con docstrings.
 
## Requisitos
 
- Python 3.13 o superior (verificar con `python --version`)
- Sin dependencias externas, solo libreria estandar de Python
## Como ejecutar los ejercicios
 
Todos los comandos se ejecutan desde dentro de la carpeta `funciones/`. Una vez ahi, el comando para correr cualquier archivo es:
 
```bash
python nombre_del_archivo.py
```
 
Para ubicarte en la carpeta correcta desde la terminal (ejemplo en mi computador):
 
```bash
cd C:\Users\Luis\Documents\fundamentos_python_control_fun\src\funciones
```
 
---
 
## Ejercicios
 
### definicion.py
 
```bash
python definicion.py
```
 
**Que hace:**
Introduce el concepto de funcion en Python. Muestra como definir una funcion con la palabra clave `def`, como llamarla, y por que son utiles para organizar y reutilizar codigo. Los ejemplos van desde una funcion sin parametros que imprime un saludo, hasta una que calcula el area de un rectangulo recibiendo datos y devolviendo un resultado. Tambien se muestra que las funciones en Python son ciudadanos de primera clase, lo que significa que pueden asignarse a variables y llamarse a traves de ellas. Se incluye un ejemplo de ambito de variables, donde se demuestra que las variables definidas dentro de una funcion no existen fuera de ella.
 
---
 
### parametros_y_argumentos.py
 
```bash
python parametros_y_argumentos.py
```
 
**Que hace:**
Explica la diferencia entre parametro (la variable que define la funcion) y argumento (el valor que se le pasa al llamarla). Cubre los distintos tipos de parametros que Python permite: posicionales, que se asignan por orden; con valores predeterminados, que se usan si no se pasa ese argumento; y por nombre, que permiten pasar los valores en cualquier orden especificando a cual parametro corresponde cada uno. Tambien muestra como combinar estos tipos en una misma funcion y termina con un ejemplo practico de una funcion para formatear texto que acepta prefijo, sufijo, separador y opcion de mayusculas, demostrando la flexibilidad que dan los distintos tipos de parametros.
 
---
 
### validacion_de_argumentos.py
 
```bash
python validacion_de_argumentos.py
```
 
**Que hace:**
Trabaja la validacion de los datos que recibe una funcion antes de procesarlos. Muestra como verificar que los argumentos sean del tipo correcto y esten dentro de un rango valido usando `isinstance` y comparaciones, lanzando un `ValueError` con un mensaje claro cuando no se cumple la condicion. Tambien cubre el uso de `*args` para funciones que aceptan cualquier cantidad de argumentos posicionales, donde todos llegan como una tupla, y `**kwargs` para funciones que aceptan cualquier cantidad de argumentos por nombre, donde todos llegan como un diccionario. Estos dos mecanismos permiten escribir funciones que se adaptan a distintas cantidades de datos sin necesidad de definir cada parametro por separado.
 
---
 
### return.py
 
```bash
python return.py
```
 
**Que hace:**
Explica la sentencia `return` y sus dos funciones: devolver un valor como resultado de la funcion y terminar su ejecucion inmediatamente. Los ejemplos muestran funciones que retornan un valor calculado, funciones sin `return` que devuelven `None` de forma automatica, y como retornar multiples valores a la vez, que Python empaqueta internamente como una tupla. Se trabaja el patron de retorno anticipado, donde la funcion sale antes de llegar al final si detecta un caso especial como una division por cero o un parametro invalido. Tambien se cubren funciones booleanas que devuelven `True` o `False`, funciones que transforman datos de un formato a otro, y funciones que devuelven estructuras como listas o diccionarios. El archivo termina con un ejemplo completo de conversion de temperatura entre Celsius, Fahrenheit y Kelvin que aplica validacion, retorno anticipado y manejo de casos especiales en un mismo flujo.
 
---
 
### docstrings.py
 
```bash
python docstrings.py
```
 
**Que hace:**
Introduce los docstrings, que son cadenas de texto colocadas justo despues de la definicion de una funcion para documentar que hace, que parametros recibe y que devuelve. A diferencia de los comentarios, los docstrings quedan disponibles durante la ejecucion del programa y pueden consultarse con `help()` o el atributo `__doc__`. El archivo muestra los tres estilos de docstring mas usados: estilo Google, estilo reStructuredText y estilo NumPy, y explica cuando usar un docstring de una sola linea versus uno mas detallado. Tambien se muestra como incluir ejemplos de uso dentro del docstring y como ejecutarlos como pruebas automaticas con el modulo `doctest`. El archivo cierra con buenas practicas: usar verbos en presente, documentar los tipos de datos, indicar que excepciones puede lanzar la funcion, e incluir ejemplos concretos que muestren el comportamiento esperado.