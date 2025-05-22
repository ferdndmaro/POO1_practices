#Hilos y Red
#Oscar Fernando Madera Rojo 2B

###sasyncio###
import asyncio
# Definir una función asincrónica que simula una tarea
async def tarea(nombre):
    print(f"{nombre} inicia")
    await asyncio.sleep(2)
    print(f"{nombre} termina")
# Ejecutar las tareas de forma concurrente
async def main():
    await asyncio.gather(# Ejecutar las tareas de forma concurrente
        tarea("Tarea 1"),
        tarea("Tarea 2")
    )
asyncio.run(main()) # Ejecutar la función principal

###------------------------Hilos-----------------------------------------###

import threading
import time

def tarea(nombre, segundos):
    print(f'Iniciando {nombre}')
    time.sleep(segundos)  # Simula trabajo
    print(f'{nombre} completado')

# Creación de hilos
hilo1 = threading.Thread(
    target=tarea, 
    args=('Tarea-1', 2)
)
hilo2 = threading.Thread(
    target=tarea, 
    args=('Tarea-2', 1)
)

# Inicio de ejecución
hilo1.start()
hilo2.start()

# Esperamos a que terminen
hilo1.join()
hilo2.join()

print('Tareas completadas')

#--------------------------------------------------------------------------------#
# Definimos la clase hilo que hereda de threading.Thread
class hilo(threading.Thread):
    def __init__(self, nombre, intervalo):
        threading.Thread.__init__(self)
        self.nombre = nombre
        self.intervalo = intervalo 
# Definimos el método run que es el que se ejecuta al iniciar el hilo
    def run (self):
        print(f'El hilo {self.nombre} ha comenzado') 
        for i in range(5):
           print(f'el hilo {self.nombre} se encuentra en la iteracion {i}')
           time.sleep(self.intervalo)
           print(f'el hilo{self.nombre} ha finalizado')
# Creamos dos hilos
hilo1 = hilo('Hilo1', 2) # Hilo que duerme 1 segundo
hilo2 = hilo('Hilo2', 4) # Hilo que duerme 2 segundos
hilo1.start() # Iniciamos el hilo
hilo2.start() # Iniciamos el hilo
hilo1.join() # Esperamos a que el hilo termine
hilo2.join() # Esperamos a que el hilo termine
print('Los hilos han terminado') # Mensaje final