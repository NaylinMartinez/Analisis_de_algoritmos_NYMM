#libreria del tiempo
import time
#libreria para generar numeros/arreglos aleatorios
import random
#libreria para graficar
import matplotlib.pyplot as plt

#definir una funcion para el ordenamiento  QUICKSORT
def QUICKSORT(arr):
    #CASO BASE 
    #cuando los arreglos sea igual a 1
    if len(arr) <= 1:
        #si los arreglos ya son de logitud 1, entonces ya estan ordenados asi que ya los puede retornar
        return arr
    
     #CASO GENERAL   
    # Calcular la suma de los valores dentro, con esto poder obtener la media del arreglo
    #suma = sum(arr)
    # Calcular la cantidad de elementos en el arreglo
    #cantidad_elementos = len(arr)
     #para definir el pivote
    #pivote = suma/cantidad_elementos
    #segunda manera de alegir el pivote
    pivote = random.choice(arr)

    #si los elementos que quedan son menores, se van a la izquierda
    izquierda = [x for x in arr if x < pivote]
    #iguales = [x for x in arr if x == pivote]
    #si los elemntos que quedan son mayores, se van a la derecha
    derecha = [x for x in arr if x > pivote]

    return QUICKSORT(izquierda) + QUICKSORT(derecha)

# hacemos una función para generar un arreglo aleatorio de tamaño n
def arreglo_aleatorio(n):
    return [random.randrange(10, 10000) for _ in range(n)]

# definimos el número de arreglos aleatorios que queremos hacer
num_arreglos = 100
longitudes_arreglos = []
tiempos = []

for _ in range(num_arreglos):
     # Tamaño aleatorio para el arreglo
    longitud_arreglo = random.randrange(10, 10000)
    arr = arreglo_aleatorio(longitud_arreglo)
    
     # con la función del tiempo, medimos cuanto es que tarda en ordenar el arreglo
    inicio = time.time()
    tiempo = QUICKSORT(arr)
    final = time.time()
    
    longitudes_arreglos.append(longitud_arreglo)
    tiempos.append(final - inicio)

# Ordenar las longitudes de los arreglos para la representación lineal
longitudes_arreglos.sort()

# Generar el gráfico con una línea
plt.plot(longitudes_arreglos, tiempos, marker='o')
plt.xlabel("Longitud del arreglo")
plt.ylabel("Tiempo que tarda en ordenar (segundos)")
plt.title('GRFICO DE TIEMPO \n (Practica 2) (Gráfico Lineal)')
plt.show()