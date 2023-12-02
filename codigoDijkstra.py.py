 
import heapq 
from collections import defaultdict 
import time 

class GrafoPonderado: 
	def __init__(self):
        self.vertices = set() 
        self.aristas = defaultdict(list)

 	def agregar_vertice(self, vertice): 
    # Agrega un vértice al conjunto de vértices. 
	    self.vertices.add(vertice) 

    def agregar_arista(self, desde_vertice, hacia_vertice, peso): 
    # Agrega una arista bidireccional con su respectivo peso. 
        self.vertices.add(desde_vertice) 
        self.vertices.add(hacia_vertice) 
        self.aristas[desde_vertice].append((hacia_vertice, peso)) 
        self.aristas[hacia_vertice].append((desde_vertice, peso)) 

    def dijkstra(self, vertice_inicial): 
        # Implementación del algoritmo de Dijkstra para encontrar caminos más cortos. 
        distancias = {vertice: float('infinity') for vertice in self.vertices} 
        distancias[vertice_inicial] = 0 
        padres = {vertice: None for vertice in self.vertices} 
        cola_prioridad = [(0, vertice_inicial)] 
        tiempo_inicio = time.time() 

        while cola_prioridad: 
	        distancia_actual, vertice_actual = heapq.heappop(cola_prioridad) 

            if distancia_actual > distancias[vertice_actual]: 
                continue 
            for vecino, peso_arista in self.aristas[vertice_actual]: 
                distancia = distancia_actual + peso_arista 
                if distancia < distancias[vecino]: 
                    distancias[vecino] = distancia 
                    padres[vecino] = vertice_actual 
                    heapq.heappush(cola_prioridad, (distancia, vecino)) 

        tiempo_fin = time.time() 
        tiempo_transcurrido = tiempo_fin - tiempo_inicio 
        caminos_minimos = {vertice: self.construir_camino(vertice_inicial, vertice, padres) for vertice in self.vertices} 
        return distancias, caminos_minimos, tiempo_transcurrido 

    def construir_camino(self, vertice_inicial, vertice_final, padres): 
        # Construye el camino más corto desde el vértice inicial hasta el vértice final. 
        camino = [] 
        vertice_actual = vertice_final 
        while vertice_actual is not None: 
	        camino.insert(0, vertice_actual) 
	        vertice_actual = padres[vertice_actual] 
        return camino

 # Crear instancias de GrafoPonderado para cada caso 
grafo1 = GrafoPonderado() 
grafo2 = GrafoPonderado() 
grafo3 = GrafoPonderado() 
grafo4 = GrafoPonderado() 
grafo5 = GrafoPonderado() 

# Caso 1 
grafo1.agregar_vertice("A") 
grafo1.agregar_vertice("B") 
grafo1.agregar_vertice("C") 
grafo1.agregar_arista("A", "B", 5) 
grafo1.agregar_arista("A", "C", 3) 
grafo1.agregar_arista("B", "C", 2) 

# Caso 2 
grafo2.agregar_vertice("A") 
grafo2.agregar_vertice("B") 
grafo2.agregar_vertice("C") 
grafo2.agregar_vertice("D") 
grafo2.agregar_arista("A", "B", 2) 
grafo2.agregar_arista("A", "C", 4) 
grafo2.agregar_arista("B", "C", 1) 
grafo2.agregar_arista("B", "D", 7) 
grafo2.agregar_arista("C", "D", 3) 

# Caso 3
grafo3.agregar_vertice("A")
grafo3.agregar_vertice("B")
grafo3.agregar_vertice("C")
grafo3.agregar_vertice("D")
grafo3.agregar_vertice("E")
grafo3.agregar_arista("A", "B", 4)
grafo3.agregar_arista("A", "C", 2)
grafo3.agregar_arista("B", "C", 5)
grafo3.agregar_arista("B", "D", 10)
grafo3.agregar_arista("C", "D", 1)
grafo3.agregar_arista("D", "E", 3)

# Caso 4
grafo4.agregar_vertice("A")
grafo4.agregar_vertice("B")
grafo4.agregar_vertice("C")
grafo4.agregar_arista("A", "B", 2)
grafo4.agregar_arista("B", "C", 3)

# Caso 5
grafo5.agregar_vertice("A")
grafo5.agregar_vertice("B")
grafo5.agregar_vertice("C")
grafo5.agregar_arista("A", "B", 7)
grafo5.agregar_arista("A", "C", 1)
grafo5.agregar_arista("B", "C", 5)

# Ejecutar el algoritmo de Dijkstra para cada caso 
for i, grafo in enumerate([grafo1, grafo2, grafo3, grafo4, grafo5], start=1): 
    vertice_inicial = "A" 

    # Medir el tiempo de ejecución 
    tiempo_inicio_caso = time.time() 
    distancias, caminos_minimos, tiempo_ejecucion = grafo.dijkstra(vertice_inicial) 
    tiempo_fin_caso = time.time() 

    print(f"Caso {i}:")
    print("*************************************************************\n") 
    print(f"El camino más corto localizado es desde {vertice_inicial}: {distancias}") 
    for vertice, camino in caminos_minimos.items(): 
        print("*************************************************************\n") 
        print(f"El recorrido desde {vertice_inicial} hasta {vertice}: {camino}") 
    print("*************************************************************\n") 
    print(f"El tiempo que tarda en ejecutarse es de: {tiempo_ejecucion} segundos") 
    print(f"El tiempo total del caso es de: {tiempo_fin_caso - tiempo_inicio_caso} segundos") 
    print("*************************************************************\n")