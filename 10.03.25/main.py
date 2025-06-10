def ford_bellman(graph, start_vertex):
    n = len(graph)
    distances = {v: float('inf') for v in range(n)}
    distances[start_vertex] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                weight = graph[u][v]
                if weight != 0 and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    return distances
