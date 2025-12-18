import networkx as nx
import heapq



def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start] = 0
    
    priority_queue = [(0, start)]
    predecessors = {node: None for node in graph.nodes()}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, attributes in graph[current_node].items():
            weight = attributes.get('weight', 1)
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths, predecessors


G = nx.Graph()
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

start_node = 'C'
distances, paths = dijkstra(G, start_node)

print(f'Найкоротші відстані від вершини "{start_node}":')
for node, dist in distances.items():
    print(f'До вершини {node}: {dist}')
