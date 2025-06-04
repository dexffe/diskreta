# Алгоритм Дейкстры


graph = [[0, 7, 9, 0, 0, 14], 
        [7, 0, 10, 15, 0, 0], 
        [9, 10, 0, 11, 0, 2], 
        [0, 15, 11, 0, 6, 0], 
        [0, 0, 0, 6, 0, 9], 
        [14, 0, 2, 0, 9, 0]]


def dijkstra(graph, start):
    n = len(graph)
    distances = {i+1: float('inf') for i in range(n)}
    distances[start] = 0
    visited = set()

    while len(visited) < n:
        current = None
        min_dist = float('inf')
        for vertex in distances:
            if vertex not in visited and distances[vertex] < min_dist:
                min_dist = distances[vertex]
                current = vertex

        if current is None:
            break

        visited.add(current)

        for neighbor in range(n):
            weight = graph[current - 1][neighbor]
            if weight != 0 and distances[neighbor + 1] > distances[current] + weight:
                distances[neighbor + 1] = distances[current] + weight

    print(distances)


dijkstra(graph, 1)