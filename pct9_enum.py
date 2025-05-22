#ENUM
#Oscar Fernando Madera Rojo 2B

from enum import Enum

class Dias(Enum):
    LUNES = 'lunes'
    MARTES = 'martes'
    MIERCOLES = 'miercoles'
    JUEVES = 'jueves'
    VIERNES = 'viernes'
    SABADO = 'sabado'
    DOMINGO = 'domingo'

def verificar_dia(dia):
    try:
        if not isinstance(dia, str):
            raise TypeError('Se esperaba un valor de tipo str.')

        dia = dia.capitalize()  # Normalizar formato

        if dia in [d.value for d in Dias]:  # Verificar si está en el Enum
            print(f'Día válido: {dia}')
        else:
            raise ValueError('Día ingresado no válido, debe ser un día de la semana.')

    except TypeError as e:
        print(f'Error de tipo: {e}')
    except ValueError as e:
        print(f'Error: {e}')
    finally:
        print('Ejecución finalizada.')

# Pruebas
verificar_dia('Lunes')     # Día válido
verificar_dia('domingo')   # Día válido
verificar_dia('Feriado')   # Error: Día no válido
verificar_dia(123)        # Error de tipo 