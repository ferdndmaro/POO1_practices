#Polimorfismo
#Oscar Fernando Madera Rojo 2B

class Empleado:
    def __init__(self,nombre,id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
    def calcular_salario(self):
        pass #Método a implementar por las subclases

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado,salario_base,bono):
        self.salario_base = salario_base
        self.bono = bono
        super().__init__(nombre, id_empleado)
    def calcular_salario(self):
        return self.salario_base + self.bono
    
class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado,salario_base,horas_extra,tarifa_extra):
        super().__init__(nombre, id_empleado)
        self.salario_base = salario_base
        self.horas_extra = horas_extra
        self.tarifa_extra = tarifa_extra
    def calcular_salario(self):
        return self.salario_base + (self.horas_extra * self.tarifa_extra)
    
class Vendedor(Empleado):
    def __init__(self, nombre, id_empleado,salario_base,ventas,comision):
        super().__init__(nombre, id_empleado)
        self.salario_base = salario_base
        self.ventas = ventas
        self.comision = comision
    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.comision)
    