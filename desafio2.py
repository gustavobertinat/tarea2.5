numero1 = float(input("Ingrese el primer número, por favor: "))
numero2 = float(input("Ingrese el segundo número, por favor: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Manejar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

print("La suma de estos dos números es:", suma)
print("La resta de estos dos números es:", resta)
print("La multiplicación de estos dos números es:", multiplicacion)
print("La división de estos dos números es:", division)

