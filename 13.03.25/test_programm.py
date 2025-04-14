from programm import floyd_warshall
import pprint

graph1 = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]
"""
Ожидаемый результат после Флойда:
[0, 3, 7, 5]
[2, 0, 6, 4] 
[3, 1, 0, 5]
[5, 3, 2, 0]
"""

graph2 = [
    [0, 1, float('inf'), float('inf')],
    [float('inf'), 0, -1, float('inf')],
    [float('inf'), float('inf'), 0, -1],
    [-1, float('inf'), float('inf'), 0]
]
"""
Ожидаемый результат:
[ 0,  1,  0, -1]
[-2,  0, -1, -2]
[-2, -1,  0, -1]
[-1,  0, -1,  0]
"""

pprint.pprint(floyd_warshall(graph1))

pprint.pprint(floyd_warshall(graph2))