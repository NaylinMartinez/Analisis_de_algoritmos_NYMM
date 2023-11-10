import random
import time
import matplotlib.pyplot as plt

def mochila_fraccionaria(capacidad, objetos):
    # Ordenar por el valor del peso
    objetos.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_objetos = 0.0
    mochila = []
    for valor, peso in objetos:
        # Si el objeto se puede mover completo
        if capacidad >= peso:
            mochila.append((valor, peso))
            total_objetos += valor
            capacidad -= peso
        # El objeto pesa más de la capacidad de la mochila
        else:
            fracc = capacidad / peso 
            mochila.append((valor * fracc, peso * fracc))
            total_objetos += valor * fracc
            break
    return total_objetos, mochila

def generar_objetos_aleatorios(n):
    return [(random.randrange(10, 100), random.randrange(10, 100)) for _ in range(n)]

if __name__ == "__main__":
    tiempos = []

    for _ in range(10):
        capacidadAleatoria = random.randrange(10, 100)
        objetosAleatorios = generar_objetos_aleatorios(capacidadAleatoria)
        
        print(f"\nCapacidad de la mochila: {capacidadAleatoria}")
        print(f"Objetos generados aleatoriamente: {objetosAleatorios}")
        
        inicio_tiempo = time.time()
        total, mochila = mochila_fraccionaria(capacidadAleatoria, objetosAleatorios)
        final_tiempo = time.time()
        
        print(f"El total de objetos es {total}")
        print(f"La mochila queda: {mochila}")
        print(f"Tiempo de ejecución: {final_tiempo - inicio_tiempo} segundos\n")

        tiempos.append(final_tiempo - inicio_tiempo)

    # Gráfico
    plt.plot(range(1, 11), tiempos, marker='o')
    plt.title('Tiempo de ejecución de la mochila fraccionaria')
    plt.xlabel('Número de ejecución')
    plt.ylabel('Tiempo (segundos)')
    plt.show()
