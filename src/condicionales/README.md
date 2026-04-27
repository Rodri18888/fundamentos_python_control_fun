# Condicionales en Python
 
Ejercicios sobre estructuras de control condicional en Python. Cada archivo cubre un concepto distinto de la leccion 5, desde la declaracion `if` basica hasta la evaluacion de cortocircuito.
 
## Requisitos
 
- Python 3.13 o superior (verificar con `python --version`)
- Sin dependencias externas, solo libreria estandar de Python
> El archivo `match-case.py` requiere minimo Python 3.10, ya que esa estructura fue introducida en esa version. Si obtienes un error de sintaxis al ejecutarlo, el problema es la version instalada.
 
## Como ejecutar los ejercicios
 
Todos los comandos se ejecutan desde dentro de la carpeta `condicionales/`. Una vez ahi, el comando para correr cualquier archivo es:
 
```bash
python nombre_del_archivo.py
```
 
Para ubicarte en la carpeta correcta desde la terminal (ejemplo en mi computador):
 
```bash
cd C:\Users\Luis\Documents\fundamentos_python_control_fun\src\condicionales
```
 
---
 
## Ejercicios
 
### if.py
 
```bash
python if.py
```
 
**Que hace:**
Muestra el uso basico de la declaracion `if`. El programa define variables como `edad` o `temperatura` y evalua condiciones simples sobre ellas. Si la condicion se cumple, imprime un mensaje en pantalla; si no, no hace nada. Tambien incluye un ejemplo con operadores logicos `and` y `or` dentro del mismo `if`, como verificar si una hora esta dentro de un rango determinado.
 
---
 
### if-else.py
 
```bash
python if-else.py
```
 
**Que hace:**
Trabaja la toma de decisiones binarias. El programa siempre va a ejecutar uno de dos bloques posibles: el del `if` si la condicion es verdadera, o el del `else` si es falsa. Los ejemplos incluyen verificar si una persona puede votar segun su edad, comparar una contrasena ingresada por el usuario, y determinar si un numero es par o impar usando el operador modulo `%`. Tambien hay un caso con multiples instrucciones dentro de cada bloque, como actualizar un saldo bancario tras un retiro.
 
---
 
### if-elif-else.py
 
```bash
python if-elif-else.py
```
 
**Que hace:**
Extiende la logica condicional para manejar mas de dos escenarios. Python evalua cada condicion en orden y ejecuta el bloque del primer caso verdadero, ignorando el resto. Los ejemplos del archivo clasifican un numero como positivo, negativo o cero, asignan una calificacion segun un rango de nota numerica, y determinan si una persona es menor de edad, adulta o mayor de 65 anos usando comparaciones encadenadas. Tambien hay un caso donde se omite el `else` porque no se necesita una accion por defecto.
 
---
 
### match-case.py
 
```bash
python match-case.py
```
 
**Que hace:**
Implementa coincidencia estructural de patrones, disponible desde Python 3.10. En lugar de encadenar multiples `elif`, `match` compara una expresion contra varios patrones definidos con `case`. Los ejemplos cubren: identificar el nombre de una fruta ingresada por el usuario, determinar la posicion de un punto en un plano cartesiano usando tuplas, aplicar condiciones adicionales a los patrones con guardas (`if` dentro del `case`), procesar una lista de diccionarios segun el rol de cada usuario, y manejar listas con cantidad variable de elementos usando el operador `*`.
 
---
 
### operadores_logicos.py
 
```bash
python operadores_logicos.py
```
 
**Que hace:**
Muestra como combinar condiciones usando los operadores `and`, `or` y `not`. Con `and`, ambas condiciones deben ser verdaderas para que el bloque se ejecute. Con `or`, basta con que una lo sea. Con `not`, se invierte el valor logico de la condicion. El archivo incluye ejemplos de precedencia (el orden en que Python evalua los operadores es primero `not`, luego `and`, luego `or`) y muestra por que usar parentesis es importante para controlar ese orden. Tambien compara escribir condiciones anidadas versus combinarlas con operadores logicos, mostrando que la segunda opcion es mas clara.
 
---
 
### expresiones_condicionales.py
 
```bash
python expresiones_condicionales.py
```
 
**Que hace:**
Introduce el condicional ternario, que permite escribir una decision simple en una sola linea en lugar de un bloque `if-else` completo. La sintaxis es `valor_si_verdadero if condicion else valor_si_falso`. Los ejemplos asignan un mensaje segun la edad, determinan el maximo entre dos numeros, anidan expresiones condicionales para clasificar a una persona en tres categorias, y las aplican dentro de listas por comprension para etiquetar numeros como pares o impares. Tambien se muestra como usar el ternario para evitar una division por cero antes de realizar el calculo.
 
---
 
### condicionales_anidados.py
 
```bash
python condicionales_anidados.py
```
 
**Que hace:**
Trabaja estructuras `if` dentro de otras estructuras `if`, utiles cuando una condicion solo tiene sentido evaluarse si otra ya fue verdadera. Los ejemplos clasifican a una persona segun edad y estado civil, manejan el caso de licencia de conducir donde primero se verifica la edad y luego el permiso de los padres, y validan usuario y contrasena en dos pasos donde la contrasena solo se revisa si el usuario es correcto. El archivo tambien muestra cuando los condicionales anidados se vuelven dificiles de leer y como reescribirlos de forma mas lineal o usando `elif` con operadores logicos.
 
---
 
### cortocircuito_y_optimizacion.py
 
```bash
python cortocircuito_y_optimizacion.py
```
 
**Que hace:**
Explica la evaluacion de cortocircuito, que es el comportamiento de Python de dejar de evaluar condiciones en cuanto el resultado ya esta determinado. Con `and`, si la primera condicion es falsa, Python no revisa la segunda porque el resultado ya es falso de todas formas. Con `or`, si la primera es verdadera, tampoco evalua la segunda. Esto permite evitar errores en tiempo de ejecucion: por ejemplo, verificar que una lista no este vacia antes de acceder a su primer elemento evita un `IndexError`, y verificar que el divisor no sea cero antes de dividir evita un `ZeroDivisionError`. Tambien se cubren las funciones `any()` y `all()`, que aplican el mismo principio sobre listas de condiciones.