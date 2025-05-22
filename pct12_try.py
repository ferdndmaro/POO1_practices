#TRY
#Oscar Fernando Madera Rojo 2B
#División segura
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
except ValueError:
    print("¡Error! Debes ingresar números válidos.")
#Acceso a índices en listas
lista = [10, 20, 30]
try:
    indice = int(input("Ingresa un índice (0-2): "))
    print(f"El elemento es: {lista[indice]}")
except IndexError:
    print("¡Error! El índice está fuera de rango.")
except ValueError:
    print("¡Error! Debes ingresar un número entero.")
#Conversión de tipos
try:
    numero = int(input("Ingresa un número entero: "))
    print(f"Número ingresado: {numero}")
except ValueError:
    print("¡Error! Debes ingresar un número entero válido.")

#try-else
nombre_archivo = input("Ingresa el nombre del archivo: ")
try:
    archivo = open(nombre_archivo, 'r')
except FileNotFoundError:
    print("¡Error! El archivo no existe.")
else:
    print("Archivo leído con éxito:")
    print(archivo.read())
    archivo.close()

#Uso de finally
nombre_archivo = input("Ingresa el nombre del archivo: ")
try:
    archivo = open(nombre_archivo, 'r')
except FileNotFoundError:
    print("¡Error! El archivo no existe.")
else:
    print("Archivo leído con éxito:")
    print(archivo.read())
    archivo.close()
finally:
    print("Proceso terminado.")