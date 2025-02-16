def alg1(graf: list) -> int:
    count = 0
    end_list = [1]
    list_roads = []
    while len(end_list) != len(graf):
        for i in end_list:
            for j in range(len(graf[i-1])):
                if graf[i-1][j] != 0:
                    list_roads.append((i,  graf[i-1].index(graf[i-1][j])+1, graf[i-1][j]))
                    graf[i-1][j], graf[j][i-1] = 0, 0
        len_short_road = 999999999
        road = ()
        for x, y, l in list_roads:
            if l < len_short_road:
                len_short_road = l
                road = (x, y)
        count += len_short_road
        end_list.append(road[1])
        for road in list_roads:
            if road[1] in end_list:
                list_roads.remove(road)
    return count


def alg2(graf: list) -> int:
    count = 0
    end_list = []
    list_roads = []
    for x in range(len(graf)):
        for y in range(len(graf[x])):
            if graf[x][y] != 0 and (y+1, x+1, graf[x][y]) not in list_roads:
                list_roads.append((x+1, y+1, graf[x][y]))
    sorted_list_roads = sorted(list_roads, key=lambda x: x[2])
    last_roads_list = sorted_list_roads[:]
    for i in sorted_list_roads:
        if i[0] not in end_list or i[1] not in end_list:
            count += i[2]
            end_list.append(i[0])
            end_list.append(i[1])
            last_roads_list.remove(i)

    isRedy = False
    while not isRedy:
        l_nums = []
        isRedy = True
        for i in end_list:
            if end_list.count(i) == 1:
                l_nums.append(i)
                isRedy = False
        if len(l_nums) == 2:
            break
        for i in last_roads_list:
            if i[0] in l_nums or i[1] in l_nums:
                count += i[2]
                end_list.append(i[0])
                end_list.append(i[1])
                last_roads_list.remove(i)
                break
    return count