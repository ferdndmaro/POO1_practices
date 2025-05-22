#Abstracción 
#Oscar Fernando Madera Rojo 2B

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura

