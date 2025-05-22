#Figuras con parámetros 
#Oscar Fernando Madera Rojo 2B

from math import pi, tan, sqrt

class Figura:
    def __init__(self, lado, numero_lados = None):
        self.lado = lado
        self.numlados = numero_lados

    def calcular_cuadrado(self):
        perimetro = 4 * self.lado
        area = self.lado ** 2
        return perimetro, area

    def calcular_triangulo(self):
        perimetro = 3 * self.lado
        area = (self.lado ** 2) * (sqrt(3)/4)
        return perimetro, area

    def calcular_pentagono(self):
        perimetro = 5 * self.lado
        area = (5 / 4) * (self.lado ** 2) * (1 / tan(pi / 5))
        return perimetro, area


print("Qué figura deseas calcular?")
print("1.- Cuadrado")
print("2.- Triángulo")
print("3.- Pentágono")

opcion = int(input("Elige una opción (1-3): "))

lado = float(input("Ingresa el lado de la figura: "))
figura = Figura(lado)

if opcion == 1:
    perimetro, area = figura.calcular_cuadrado()
    print(f"El perímetro del cuadrado es: {perimetro}")
    print(f"El área del cuadrado es: {area}")
elif opcion == 2:
    perimetro, area = figura.calcular_triangulo()
    print(f"El perímetro del triángulo es: {perimetro}")
    print(f"El área del triángulo es: {area}")
elif opcion == 3:
    perimetro, area = figura.calcular_pentagono()
    print(f"El perímetro del pentágono es: {perimetro}")
    print(f"El área del pentágono es: {area}")
else:
    print("Entrada no válida")