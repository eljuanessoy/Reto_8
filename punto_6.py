def Potencia(n:float, x:int):
  ResultadoPotencia : int = 1
  for i in range(1,n+1):
    ResultadoPotencia *= x
  print(f"{x}^{n}={ResultadoPotencia}")

n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))

Potencia(n,x)