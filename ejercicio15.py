from grafo import Grafo
from random import randint

# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales
# del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais if isinstance(pais, list) else [pais]
        self.tipo = tipo


    def __str__(self):
        return f"Nombre: {self.nombre} - Países: {', '.join(self.pais)} - Tipo: {self.tipo}"


# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de 
# uno en las naturales) y tipo (natural o arquitectónica);

maravillas_naturales = [
    Maravilla("Cataratas del Iguazú", "Argentina", "natural"),
    Maravilla("Gran Cañón", "Estados Unidos", "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Aurora Boreal", "Varios lugares del Ártico", "natural"),
    Maravilla("Monte Everest", "Nepal", "natural"),
    Maravilla("Parque Nacional de Yellowstone", "Estados Unidos", "natural"),
]

maravillas_arquitectonicas = [
    Maravilla("Gran Pirámide de Guiza", "Egipto", "arquitectónica"),
    Maravilla("Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Taj Mahal", "India", "arquitectónica"),
    Maravilla("Estatua de la Libertad", "Estados Unidos", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Ciudad de Petra", "Jordania", "arquitectónica"),
]


# f. deberá utilizar un grafo no dirigido.

grafo = Grafo(dirigido=False)

dic = {}

for i in range(len(maravillas_naturales)):
    dic[maravillas_arquitectonicas[i].nombre] = i
    dic[maravillas_naturales[i].nombre] = i

for maravilla in maravillas_arquitectonicas:
    grafo.insert_vertice(maravilla.nombre)

for maravilla in maravillas_naturales:
    grafo.insert_vertice(maravilla.nombre)


# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;

for i in maravillas_arquitectonicas:
    posicionA = grafo.search_vertice(i.nombre)
    valueA = grafo.get_element_by_index(posicionA)
    for j in maravillas_arquitectonicas:
        posicionB = grafo.search_vertice(j.nombre)
        valueB = grafo.get_element_by_index(posicionB)
        adyacencia = grafo.is_adyacent(valueA[0], valueB[0])
        if valueA != valueB and adyacencia == False:
            peso = randint(100, 5000)
            grafo.insert_arist(valueA[0], valueB[0], peso)

for i in maravillas_naturales:
    posicionB = grafo.search_vertice(i.nombre)
    valueA = grafo.get_element_by_index(posicionB)
    for j in maravillas_naturales:
        posicionB = grafo.search_vertice(j.nombre)
        valueB = grafo.get_element_by_index(posicionB)
        adyacencia = grafo.is_adyacent(valueA[0], valueB[0])
        if valueA != valueB and adyacencia == False:

            peso = randint(100, 5000)
            grafo.insert_arist(valueA[0], valueB[0], peso)


# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

print('c:')
bosque = grafo.kruskal()
print("Arbol de expansion minimo de cada tipo de maravilla:")
print()
for arbol in bosque:
    print("Arbol:")
    for nodo in arbol.split(";"):
        print(nodo)
        print()


#  d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

print('d:')
paises = []
for i in maravillas_naturales:
    posicionA = grafo.search_vertice(i.nombre)
    valueA = grafo.get_element_by_index(posicionA)
    for j in maravillas_arquitectonicas:
        posicionB = grafo.search_vertice(j.nombre)
        valueB = grafo.get_element_by_index(posicionB)
        indexA = dic[valueA[0]]
        indexB = dic[valueB[0]]
        if (
            maravillas_arquitectonicas[indexB].pais[0]
            in maravillas_naturales[indexA].pais
        ):
            if (maravillas_arquitectonicas[indexB].pais in paises) == False:
                paises.append(maravillas_arquitectonicas[indexB].pais)

for pais in paises:
    print(f"{pais[0]} tiene los 2 tipos de maravilla")
print()

# e. determinar si algún país tiene más de una maravilla del mismo tipo;

print('e:')
paises_mas_naturales = []
paises_mas_arquitectonicas = []

for i in maravillas_arquitectonicas:
    posicionA = grafo.search_vertice(i.nombre)
    valueA = grafo.get_element_by_index(posicionA)
    for j in maravillas_arquitectonicas:
        posicionB = grafo.search_vertice(j.nombre)
        valueB = grafo.get_element_by_index(posicionB)
        indexA = dic[valueA[0]]
        indexB = dic[valueB[0]]
        for k in maravillas_arquitectonicas[indexB].pais:
            for l in maravillas_arquitectonicas[indexA].pais:
                if k == l and valueB[0] != valueA[0]:
                    if (k in paises_mas_arquitectonicas) == False:
                        paises_mas_arquitectonicas.append(k)
                        
                        
for i in maravillas_naturales:
    posicionA = grafo.search_vertice(i.nombre)
    valueA = grafo.get_element_by_index(posicionA)
    for j in maravillas_naturales:
        posicionB = grafo.search_vertice(j.nombre)
        valueB = grafo.get_element_by_index(posicionB)
        indexA = dic[valueA[0]]
        indexB = dic[valueB[0]]
        for k in maravillas_naturales[indexB].pais:
            for l in maravillas_naturales[indexA].pais:
                if k == l and valueB[0] != valueA[0]:
                    if (k in paises_mas_naturales) == False:
                        paises_mas_naturales.append(k)

for i in paises_mas_naturales:
    print(f"{i} mas de una maravilla natural")
print()

for i in paises_mas_arquitectonicas:
    print(f"{i} mas de una maravilla arquitectura")
print()


        
