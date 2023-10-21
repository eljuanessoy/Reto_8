import math as m

def Funcion(i: int):
    if i == 0:
        return 1
    else:
        p = 1
        for numero in range(1, i + 1):
            p *= numero
        return p
    
x = float(input("Ingrese un valor en radianes: "))
n = int(input("Ingrese la cantidad de iteraciones: "))

suma : float = 0
for b in range(n + 1):
    d = (x ** (2 * b + 1)) / Funcion(2 * b + 1)
    d *= (-1) ** b
    suma += d
    
z = (abs(suma - m.sin(x))/m.sin(x))*100

print()
print(f"{suma}")
print(f"{m.sin(x)}")
print(f"El porcentaje de error es de {z}")