#Diseño avanzado de clases
#Oscar Fernando Madera Rojo 2B

from abc import ABC,abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def mover(self):
        pass
    @abstractmethod
    def detener(self):
        pass
    @abstractmethod
    def obtener_velocidad_maxima(self):
        pass

class Conducible(ABC):
    @abstractmethod
    def conducir(self):
        pass
    @abstractmethod
    def estacionar(self):
        pass

class Mantenible(ABC):
    @abstractmethod
    def revisar(self):
        pass
    @abstractmethod
    def reparar(self):
        pass
#Uso polimorfico
def probar_vehiculo(vehiculo):
    print(vehiculo.mover())
    if isinstance(vehiculo, Conducible):
        print(vehiculo.conducir())
    if isinstance(vehiculo,Mantenible):
        print(vehiculo.revisar())
    print(vehiculo.detener())

class Coche(Vehiculo, Conducible, Mantenible):
    def mover(self):
        return "Coche moviéndose"
    def detener(self):
        return "Coche detenido"
    def obtener_velocidad_maxima(self):
        return "200 km/h"
    def conducir(self):
        return "Conduciendo coche"
    def estacionar(self):
        return "Coche estacionado"
    def revisar(self):
        return "Revisando coche"
    def reparar(self):
        return "Reparando coche"

class Motocicleta(Vehiculo, Conducible):
    def mover(self):
        return "Motocicleta moviéndose"
    def detener(self):
        return "Motocicleta detenida"
    def obtener_velocidad_maxima(self):
        return "180 km/h"
    def conducir(self):
        return "Conduciendo motocicleta"
    def estacionar(self):
        return "Motocicleta estacionada"

class Bicicleta(Vehiculo):
    def mover(self):
        return "Bicicleta moviéndose"
    def detener(self):
        return "Bicicleta detenida" 
    def obtener_velocidad_maxima(self):
        return "30 km/h"

vehiculos = [Coche(),Motocicleta(),Bicicleta()]
for v in vehiculos:
    probar_vehiculo(v)
    print() #Separar formato de salida


