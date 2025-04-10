# TODO алгоритм Литтла 

from math import inf
len_road = 0
roads = {}
dop_roads = []

def little_alg(graph):
    global len_road, roads, dop_roads
    list_min_numbers_string = []
    list_min_numbers_column = []

    # Список колонок графа
    columns_graph = []
    for i in range(len(graph)):
        s = []
        for j in range(len(graph)):
            s.append(graph[j][i])
        columns_graph.append(s)

    # Находим минимальные значения в строках
    for i in range(len(graph)):
        if min(graph[i]) != inf:
            list_min_numbers_string.append(min(graph[i]))
        else:
            list_min_numbers_string.append(0)

    # Вычитаем минимальные значения из матрицы
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != inf:
                graph[i][j] -= list_min_numbers_string[i]
    
    # Находим минимальные значения в столбцах
    temporary_list = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[j][i] != inf:
                temporary_list.append(graph[j][i])
        if temporary_list != []:
            list_min_numbers_column.append(min(temporary_list))
            temporary_list = []
        else:
            list_min_numbers_column.append(0)

    # Получаем исходную длину дороги    
    len_road += sum(list_min_numbers_string) + sum(list_min_numbers_column)

    # Вычитаем минимальные значения из матрицы
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[j][i] != inf:
                graph[j][i] -= list_min_numbers_column[i]

    # Находим максимальный штраф в матрице для нуля и его 
    max_shtraf = 0
    coords = [0, 0]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0:
                ms = min(graph[i][:j] + graph[i][j + 1:])
                mc = min([graph[x][j] for x in range(len(graph)) if x != i])
                if (ms + mc) > max_shtraf:
                    max_shtraf = ms + mc
                    coords = [i, j]
    roads.setdefault(coords[0], coords[1])

    # Заполняем строку и столбец его пересечения бесконечностями
    for key, value in roads.items():
        graph[key][value] = inf
        if value in roads.keys() and [key, roads[value]] not in dop_roads:
            dop_roads.append([key, roads[value]])
            dop_roads.append([roads[value], key])
    for i in dop_roads:
        graph[i[0]][i[1]] = inf
    graph[coords[1]][coords[0]] = inf
    for i in range(len(graph)):
        graph[i][coords[1]] = inf
        graph[coords[0]][i] = inf

    # конец   
    if graph == [[inf for j in range(len(graph))] for i in range(len(graph))]:
        return len_road
    return little_alg(graph)
