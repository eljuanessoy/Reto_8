import math as m

x = float(input("Ingrese un valor: "))
n = int(input("Ingrese la cantidad de iteraciones: "))

def factorial(i:int):
    if i == 0:
        return 1
    else:
        p = 1
        for n in range(1,i+1):
            p *= n
        return p
ResultadoSuma : float = 0

for b in range(0,n+1):
    d = x**b
    d = d/factorial(b)
    ResultadoSuma += d
z = (abs(ResultadoSuma - m.e ** x)/m.e ** x) * 100

print()    
print(ResultadoSuma)
print(m.e ** x)
print(f"El porcentaje de error es de {z}%")