import math as m

x = float(input("Ingrese un valor en radianes: "))
n = int(input("Ingrese la cantidad de iteraciones: "))

suma = 0
for b in range(n + 1):
    d = (x ** (2 * b + 1)) / (2 * b + 1)
    d *= (-1) ** b
    suma += d

z = (abs(suma - m.atan(x))/m.atan(x))*100

print()
print(f"{suma}")
print(f"{m.atan(x)}")
print(f"El porcentaje de error es de {z}")