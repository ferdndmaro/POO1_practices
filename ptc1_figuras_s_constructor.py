#Figuras sin constructor
#Oscar Fernando Madera Rojo 2B
class Cuadrado:
    def perimetro(lado):
        perimetro = lado * 4 
        return perimetro
    def area(lado):
        area = lado * lado 
        return area
Area = Cuadrado.perimetro(5)
Perimetro = Cuadrado.area(5)
print(f'El area es:{Area}')
print(f'El perimetro es:{Perimetro}')

