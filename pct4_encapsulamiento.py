#Encapsulamiento
#Oscar Fernando Madera Rojo 2B

class CuentaBancaria:
    def __init__(self,numero_cuenta,saldo_inicial=0):
        self._numero_cuenta = numero_cuenta
        self._saldo = saldo_inicial
    def depositar(self,cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
    def retirar(self,cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False
    def consultar_saldo(self):
        return self._saldo
    def obtener_numero_cuenta(self):
        return self._numero_cuenta


        