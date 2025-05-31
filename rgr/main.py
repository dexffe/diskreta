# Вариант 14
# Имеется сеть трубопроводов, соединяющих пункт А (пункт добычи нефти) с пунктом В (нефтеперерабатывающий завод). 
# Трубопроводы могут соединяться и разветвляться в промежуточных пунктах. 
# Количество нефти, которое может быть перекачено по каждому отрезку трубопровода в единицу времени определяется диаметром трубы. 
# Сколько нефти можно прокачать через такую сеть в единицу времени?
# Формат входных данных
# Во входном файле записано сначала число N (1<=N<=100), определявшее количество узлов сети. 
# Затем идет описание сети, где каждое соединение задается тремя числами - номерами узлов, которые она соединяет и диаметром сети. 
# Все соединения строго ориентированы.
# Формат выходных данных
# На экран выведите числа – суммарная величина объема прокаченной нефти.

#* Алгоритм Форда-Фалкерсона
import pprint
import copy

count_road = int(input('Введите количество дорог: '))

s1 = []
for i in range(count_road):
    s1.append(list(map(int, input().split())))

size_graph = 0
for i in s1:
    if i[0] > size_graph:
        size_graph = i[0]
    if i[1] > size_graph:
        size_graph = i[1]

graph = [[0 for i in range(size_graph)] for i in range(size_graph)]

for i in s1:
    graph[i[0]-1][i[1]-1] = i[2]


resault = 0

isOver = True
while(isOver):
    dictionary_roads = {}
    from_point = 0  
    graph_copy = copy.deepcopy(graph)
    while from_point < len(graph_copy)-1 and isOver:
        to_point = graph_copy[from_point].index(max(graph_copy[from_point]))
        len_road = max(graph_copy[from_point])
        if len_road == 0:
            if len(dictionary_roads) == 0:
                isOver = False
                break
            coords = dictionary_roads.popitem()[0]
            graph_copy[coords[0]][coords[1]] = 0
            from_point = coords[0]
            continue
        dictionary_roads.setdefault((from_point, to_point), len_road)
        from_point = to_point

        minimal_road = min(dictionary_roads.values())
        for key, value in dictionary_roads.items():
            graph_copy[key[0]][key[1]] -= minimal_road

    if isOver:
        minimal_road = min(dictionary_roads.values())
        for key, value in dictionary_roads.items():
            graph[key[0]][key[1]] -= minimal_road
        resault += minimal_road

print('Ответ:', resault)