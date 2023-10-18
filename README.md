# Reto #8 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

En la resolución de este problema, decidi usar un ciclo "for" que opera en el rango de números del 1 al 101 ya que de esta forma incluira al 100 dentro de este bucle, despues se procede a imprimir los numero que estan en ese rango, en donde por un lado seran los numeros del rango y por otro lado estaran esos mismos numeros pero elevados al cuadrado.

```python
for num in range(1, 101):
  
    print(num, num**2, sep = ", ")
```

### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

Para solucionar este problema, usé dos bucles "for" en donde uno de ellos opera en el rango de números del 1 al 1001 incrementando cada 2 unidades, e inmediatamente despues de eso imprimo los numeros que obtuve en ese rango. 

El otro bucle opera en el rango de numeros de 1 a 1001 pero que cada uno de esos numeros debera tener como residuo 0 al ser dividos entre 2, y que unicamente los que cumplan con esa condicion seran los que se van a imprimir usando "print()". Como resultado podremos ver una lista de numeros en donde comienza con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
for z in range(1,1000,2):
  print(z)
for z in range(1,1001):
  if z%2 == 0:
    
    print(z)
```

### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

Para realizar este codigo lo que hice fue que en primer lugar le pido al usuario que ingrese un numero, y a parte de ese numero se va a crear una lista en un rango desde ese numero ingresado hasta uno en donde se iran restando a 1 unidad.

A partir de este rango solo se van a imprimir los numeros los cuales su residuo al dividir entre 2 sea 0, si a la hora de dividir un numero entre 2 no da 0 como residuo entonces no se va a imprimir. De esta manera consigues hacer una lista con numeros pares en forma descendente usando "range()".

```python
x = int(input("Ingrese un numero: "))
for x in range(x,1,-1):
  if x%2 == 0:
  
    print(x)
```

### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

Para la realización de este ejercicio solicite un numero al usuario, a partir de este numero se crea una funcion que me va a permitir imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

En primer lugar a la hora de crear la función defino que valores ha de retornarme la función dependiendo del numero escogido por el usuario, si el usuario escoge un numero menor que 0 dara "ERROR", si el usuario escoge un numero igual a 0 o 1 me va a retornar como resultado "1", si el valor ingresado es diferente a lo citado previamente se creara un rango da valores "i" desde el numero 1 hasta el numero ingresado, en donde a partir de esto se realiza una operacion de multiplicacion entre el numero ingresado y los valores del rango, dando asi como resultado una lista con los factoriales desde el numero uno hasta el numero ingresado.

Luego solo uso la funcion de "print()" para imprimir por un lado la lista de numeros desde el 1 hasta el numero solicitado y a su vez los factoriales de cada numero al usar la función previamente creada.

```python
x = int(input("Ingrese un numero: "))

def fact(n):
  if n<0:
    return "ERROR"
  if n==0 or n==1:
    return 1
  for i in range(1,n):
    n=n*i
  return n

for x in range(1,x+1):
  print(f"{x}!= {fact(x)}")
```

### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

Para la realización de este codigo le pido al usuario que me ingrese un valor usando "input()", luego a partir de este valor defino una variable llamada "potencia" la cual tendra un valor de 1 entero.

Luego uso la función "range()" para crear un rango de valores "i" desde el numero 1 hasta el numero solicitado +1, y a partir de esto le pido al programa que calcule la potencia por medio de la multiplicación que se ve en el programa. 

Y finalmente al ya haber realizado esa operacion solo imprimo el resultado.

```python
n = int(input("Ingrese un numero: "))
potencia : int = 1
for i in range(1, n+1):
  potencia *= 2
  
print(potencia)
```

### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

En primer lugar creo una función en donde el valor real ingresado estará eleavado al numero natural ingresado. En primer lugar defino la variable "ResultadoPotencia" como 1 y a partir de un rango realizo una operación que calcule x^n.

Luego al ya tener creada la función solicito al usuario los valores x y n, y por ultimo activo la funcion con los valores previamente ingresados.

```python
def Potencia(n:float, x:int):
  ResultadoPotencia : int = 1
  for i in range(1,n+1):
    ResultadoPotencia *= x
  print(f"{x}^{n}={ResultadoPotencia}")

n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))

Potencia(n,x)
```

### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

Realice una función en donde a su vez use la función "for" creando un rango de valores desde el 1 al 10 (dejemos a un lado el hecho de que debia ser hasta 9), y a partir de esto lo que hago es multiplicar los valores que se ingresaran posteriormente con ese rango de valores del 1 al 10. Luego se imprime el resultado y esa seria la función.

Luego de creada la función la llamamos dandole valores desde el 1 hasta el 10 para que realice todo el proceso mencionado anteriormente.

```python
def TabladeMultiplicar(n:int):
  print("Tabla de Multiplicar de " +str(n))
  for i in range(1,11):
    ResultadoTabladeMultiplicar = n*i
    print(f"{n}x{i}={ResultadoTabladeMultiplicar}")
  print()

for n in range(1, 11):
  TabladeMultiplicar(n)
```

### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.



```python

```

### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.



```python

```

### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.



```python

```

###### Recuerda que sin importar tu 
# **SEXO**
###### puedes dejar una estrellita
# **GRATIS**
###### para apoyar el trabajo :D
##### Hablando enserio si consideras que este repo fue de ayuda para ti, estaria muy agradecido si dejaras una estrellita, muchas gracias amix 🙏🙏🙏
