# Reto_8
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```pseudocode
for num in range(1, 101):
    print(num, num**2, sep = ", ")
```

### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```pseudocode
for z in range(1,1000,2): 
  print(z)
for z in range(1,1001):
  if z%2 == 0:
    print(z)
```

### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

```pseudocode
x = int(input("Ingrese un numero: "))
for x in range(x,1,-1):
  if x%2 == 0:
    print(x)
```

### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

```pseudocode
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
  print(x, fact(x), sep = ", ")
```

### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```pseudocode
n = int(input("Ingrese un numero: "))
numeros = [n]
for n in numeros:
  print(2**n)
```

### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

```pseudocode
n = int(input("Ingrese un numero entero: "))
x = float(input("Ingrese un numero real: "))
real = [x]
for x in real:
  if n>0:
    print(x**n)
```

### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```pseudocode
for x in range(1,10):
  print(1, x, 1*x,sep = ", ")
print("---------")
for x in range(1,10):
  print(2, x, 2*x,sep = ", ")
print("---------") 
for x in range(1,10):
  print(3, x, 3*x,sep = ", ")
print("---------") 
for x in range(1,10):
  print(4, x, 4*x,sep = ", ")
print("---------")
for x in range(1,10):
  print(5, x, 5*x,sep = ", ")
print("---------") 
for x in range(1,10):
  print(6, x, 6*x,sep = ", ")
print("---------")
for x in range(1,10):
  print(7, x, 7*x,sep = ", ")
print("---------")
for x in range(1,10):
  print(8, x, 8*x,sep = ", ")
print("---------")
for x in range(1,10):
  print(9, x, 9*x,sep = ", ")
```
