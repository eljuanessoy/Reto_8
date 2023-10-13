def TabladeMultiplicar(n:int):
  print("Tabla de Multiplicar de " +str(n))
  for i in range(1,11):
    ResultadoTabladeMultiplicar = n*i
    print(f"{n}x{i}={ResultadoTabladeMultiplicar}")
  print()

for n in range(1, 11):
  TabladeMultiplicar(n)