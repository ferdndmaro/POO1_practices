#Arreglos,listas,conjuntos y diccionarios
#Oscar Fernando Madera Rojo 2B

###Arreglos/Listas###
class Arreglos:
    def __init__(self):
        self.lista = []

    def insertar(self, elemento):
        self.lista.append(elemento)
        print(f"'{elemento}' agregado a la lista.")

    def modificar(self, indice, nuevo_valor):
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevo_valor
            print(f"Elemento en la posición {indice} modificado a '{nuevo_valor}'.")

    def eliminar(self, indice):
        if 0 <= indice < len(self.lista):
            eliminado = self.lista.pop(indice)
            print(f"'{eliminado}' eliminado de la lista.")
        else:
            print("Índice fuera de rango.")

    def mostrar(self):
        print("Lista actual:", self.lista)

arreglo = Arreglos()
while True:
    print("\nValores dentro de la lista")
    print("1 - Insertar valor a la lista")
    print("2 - Modificar valor en la lista")
    print("3 - Eliminar valor de la lista")
    print("4 - Mostrar lista")
    print("5 - Salir")
    
    opcion = int(input("Selecciona una opción: "))
    
    if opcion == 1:
        elemento = input("Ingresa el valor a agregar: ")
        arreglo.insertar(elemento)
    elif opcion == 2:
        indice = int(input("Ingresa el índice a modificar: "))
        nuevo_valor = input("Ingresa el nuevo valor: ")
        arreglo.modificar(indice, nuevo_valor)
    elif opcion == 3:
        indice = int(input("Ingresa el índice a eliminar: "))
        arreglo.eliminar(indice)
    elif opcion == 4:
        arreglo.mostrar()
    elif opcion == 5:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")

###Conjuntos###

# Si tenemos un conjunto c = {1,2,3}
# c.add(4) -> Añade elementos
# c.remove(1) -> Elimina el elemento del conjunto, si no se encuentra manda error
# c.discard(5) -> Elimina el elemento del conjunto, si no se encuentra no detiene el programa
#   n in c -> si existe el valor n dentro del conjunto, saldrá True

b = {0,1,2,3,4}
print("Conjunto de 5 elementos: ", b)
# agregar un valor  b.add
b.add(5)
print("Agregar un valor: ", b)
# eliminar un valor que existe  b.remove
b.remove(0)
print("Eliminar un valor que existe: ", b)
# eliminar un valor que no existe   b.remove
b.discard(6)
print("Eliminar un valor que no existe: ", b)
# verificar si existe un valor  n in b
print("verificar un valor que existe: ", 1 in b)
# agregar un valor repetido     b.add
b.add(2)
print("Agregar un valor repetido: ", b)

#------------------UNION
print("----------------UNION-----------------------")
a = {5,6,7,8}
u = b.union(a)
print(u)
u = a|b
print(u)

#------------------INTERSECTION
print("-----------------INTERSECTION----------------------")
i = a.intersection(b)
print(i)
i = a & b
print(i)

#------------------DIFFERENCE
print("-----------------DIFFERENCE----------------------")
d = a.difference(b)
print(d)
d = a - b
print(d)
print("-----------------SYMETRIC DIFFERENT----------------------")
sd = a.symmetric_difference(b)
print(sd)
sd = a^b
print(sd)

#------------------PERTENECE
print("-----------------PERTENECE----------------------")
a = {1,2,3}
b = {1,2,3,4,5}

print(a.issubset(b))
print(b.issuperset(a))

#------------------NUMERO DE ELEMENTOS
print("-----------------NUMERO DE ELEMENTOS----------------------")
n = len(a)
print(n)

#------------------CONJUNTO VACIO
print("-----------------CONJUNTO VACIO----------------------")
a.clear()
print(a)

#------------------COPIAR CONJUNTO
print("-----------------COPIAR CONJUNTO----------------------")
e = b.copy()
print(e)

###Diccionarios###

dic = {'x' : "equis", 'y' : "ye", 'd' : "de"}
dic2 = dict(x = "equis", y = "ye", d = "de")

#Encontrar un valor
print(dic['x']) #equis
print(dic.get('x')) #equis
print(dic.get('z')) #none
#print(dic['z'])
#Aunque hagan lo mismo, con "[]" manda un error y con get te manda un valor nulo.

#Modificar un valor existente
dic['x'] = "equis :O"
print(dic['x']) #equis :O

#Agregar elementos, si no existe, lo agrega
dic['z'] = "zeta"
print(dic['z']) #zeta

#Eliminar un elemento
del dic['y']
print(dic)

dic = {'x' : "equis", 'y' : "ye", 'd' : "de"}
x = dic.pop('y') #El elemento que se elimina, se almacenará en esta variable
print(dic)
print(x)

#Encontrar un elemento dentro del diccionario
print('x' in dic) # true

#Acceder a las llaves
llaves = dic.keys()
print(llaves)

#Acceder a los valores
valores = dic.values()
print(valores)

#El diccionario se convertira en una tupla
p = dic.items()
print(p)

#Vaciar el diccionario
dic2.clear()
print(dic2)

#Modificar multiples elementos existentes o agragar elementos inexistentes
dic.update({'x' : "wasaa", 'y' : "wesee", 'd': "wisii"})
print(dic)