# Reto #8 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
for num in range(1, 101):
  
    print(num, num**2, sep = ", ")
```

### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
for z in range(1,1000,2):
  print(z)
for z in range(1,1001):
  if z%2 == 0:
    
    print(z)
```

### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

```python
x = int(input("Ingrese un numero: "))
for x in range(x,1,-1):
  if x%2 == 0:
  
    print(x)
```

### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

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

```python
n = int(input("Ingrese un numero: "))
potencia : int = 1
for i in range(1, n+1):
  potencia *= 2
  
print(potencia)
```

### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

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

###### Recuerda que sin importar tu 
# **SEXO**
###### puedes dejar una estrellita
# **GRATIS**
###### para apoyar el trabajo :D
##### Hablando enserio si consideras que este repo fue de ayuda para ti, estaria muy agradecido si dejaras una estrellita, muchas gracias amix 🙏🙏🙏
