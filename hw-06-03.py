import networkx as nx
import sys

# Створення графа з вагами на ребрах
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

def dijkstra(graph, source):
    # Ініціалізуємо відстані до всіх вершин як нескінченні
    distances = {vertex: sys.maxsize for vertex in graph.nodes()}
    # Відстань до стартової вершини дорівнює 0
    distances[source] = 0

    # Множина відвіданих вершин
    visited = set()

    while len(visited) < len(graph.nodes()):
        # Вибираємо вершину з найменшою відстанню
        min_distance = sys.maxsize
        for vertex in graph.nodes():
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current = vertex

        # Позначаємо поточну вершину як відвідану
        visited.add(current)
        
        # Оновлюємо відстані до всіх сусідів поточної вершини
        for neighbor in graph.neighbors(current):
            path_length = distances[current] + graph[current][neighbor]['weight']
            if path_length < distances[neighbor]:
                distances[neighbor] = path_length

    return distances

# Застосування алгоритму Дейкстри для знаходження найкоротших шляхів від вершини 'A'
shortest_paths_from_A = dijkstra(G, source='A')

print("Найкоротші шляхи від вершини 'A' до всіх інших вершин:")
print(shortest_paths_from_A)