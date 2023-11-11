from grafo import Grafo
from random import randint

# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

grafo = Grafo(dirigido=False)


# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio

ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
             'habitacion 1', 'habitacion 2', 'sala de estar', 'terraza', 'patio']

for ambiente in ambientes:
    grafo.insert_vertice(ambiente)


# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco,
# el peso de la arista es la distancia entre los ambientes, se debe cargar en metros

print('b:')

j = 0

for ambiente in ambientes:
    posicion = grafo.search_vertice(ambiente)
    value = grafo.get_element_by_index(posicion)
    # print(value[0])

    if value[1].size() < 3:
        k = 0
        while j == 0:
            if k >= len(ambientes):
                j = 1
            else:
                lugar = ambientes[k]
                posicionB = grafo.search_vertice(lugar)
                valueB = grafo.get_element_by_index(posicionB)
                adyacencia = grafo.is_adyacent(value[0], valueB[0])
                grafo.mark_as_not_visited()

                if valueB[1].size() < 3 and value[0] != valueB[0] and adyacencia == False:
                    peso = randint(1, 10)
                    # print(value[0], valueB[0], peso)
                    grafo.insert_arist(value[0], valueB[0], peso)

                    if value[1].size() == 3:
                        j = 1
                k += 1
        j = 0


grafo.insert_arist('patio', 'comedor', randint(1, 10))
grafo.insert_arist('terraza', 'comedor', randint(1, 10))
grafo.insert_arist('sala de estar', 'habitacion 1', randint(1, 10))
grafo.insert_arist('patio', 'habitacion 1', randint(1, 10))

grafo.mark_as_not_visited()

grafo.barrido()


# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes

print('c:')
metros_cable = 0

for arbol in grafo.kruskal():
    # print(arbol)
    for nodo in arbol.split(';'):
        # print(nodo)
        metros_cable += int(nodo.split('-')[-1])

print(f"Se necesitan {metros_cable} metros de cable")

grafo.mark_as_not_visited()


# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

print('d:')
camino = grafo.dijkstra('habitacion 1', 'sala de estar')

for i in range(camino.size()):
    
    value = camino.pop()
    
    if value[0] == 'sala de estar':
        break

print()
print(f"Se necesitan {value[1]} metros para conectar la habitacion 1  la sala de estar")