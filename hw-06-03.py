import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з вагами на ребрах
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray', width=2, arrows=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Graph with Weights")
plt.show()

# Алгоритм Дейкстри для знаходження найкоротшого шляху між усіма вершинами графа
shortest_paths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))
print("Найкоротші шляхи між усіма вершинами графа:")
for source in shortest_paths:
    for target in shortest_paths[source]:
        if source != target:
            print(f"Від {source} до {target}: {shortest_paths[source][target]}")
