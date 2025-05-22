#Figuras y cálculo de un polígono
#Oscar Fernando Madera Rojo 2B
from abc import ABC,abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    
class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        return 3.14159 * self.radio * self.radio
class Triangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura)/2
class Calculadora:
    def calcular_area_total(self,figuras):
        return sum(figura.calcular_area() for figura in figuras)
    
