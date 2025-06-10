from main import ford_bellman 

graph = [
    [0, 1, 2],
    [1, 0, 2],
    [2, 1, 0]
]

start_vertex = 0
distances = ford_bellman(graph, start_vertex)

print(distances) 