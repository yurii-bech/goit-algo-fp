import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченності
    distances = {vertex: float('infinity') for vertex in graph}
    # Відстань до початкової вершини завжди 0
    distances[start] = 0
    # Ініціалізуємо бінарну купу для зберігання вершин та їх відстаней
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Якщо поточна відстань більша, ніж вже знайдена відстань, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Приклад графа з вагами на ребрах
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Початкова вершина
start_vertex = 'A'

# Знаходимо найкоротші шляхи від початкової вершини до всіх інших
shortest_distances = dijkstra(graph, start_vertex)

# Виводимо результати
for vertex, distance in shortest_distances.items():
    print(f'Шлях від вершини {start_vertex} до вершини {vertex}: {distance}')

# Візуалізація графа
G = nx.Graph(graph)
pos = nx.spring_layout(G)  # Позиція вершин для візуалізації

# Відображення графа з вагами на ребрах
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Візуалізація графа з вагами на ребрах')
plt.show()