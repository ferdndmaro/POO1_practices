#Herencia
#Oscar Fernando Madera Rojo 2B

class Vehiculo:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False
    def encender(self):
        self.encendido = True
        return f'{self.marca}{self.modelo}encendido'
    def apagar(self):
        self.encendido = False
        return f'{self.marca}{self.modelo}apagado'
    
class Coche(Vehiculo):
    def __init__(self, marca, modelo, año,num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas
    def activar_aire_acondicionado(self):
        if self.encendido:
            return 'Aire acondicionado activado'
        return 'Enciende el coche primero'

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada
    def hacer_caballito(self):
        if self.encendido:
            return 'Haciendo un caballito!'
        return 'Enciende la moto primero'
 

    