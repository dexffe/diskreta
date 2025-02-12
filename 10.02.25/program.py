def alg1(graf: list) -> int:
    start_list = [i for i in range(1, len(graf)+1)]
    l = []
    end_list = []
    isNext = True
    for i in [i for i in range(1, len(graf)+1)]:
        isNext = True
        for j in range(len(graf[i-1])):
            if (j+1 not in end_list) and (graf[i-1][j] == 1) and (j+1 in start_list):
                end_list.append(j+1)
                start_list.remove(j+1)
                isNext = False
        if isNext and end_list != []:
            l.append(end_list)
            end_list = []
    return len(l)


def alg2(graf: list) -> int:
    dict_graf = {}
    for i in range(1, len(graf)+1):
        dict_graf.setdefault(i, -1)
    count_graf = 1
    dict_graf[1] = count_graf
    isNext = True
    for i in dict_graf.keys():
        isNext = True
        for j in range(len(graf[i-1])):
            if graf[i-1][j] == 1 and dict_graf[j+1] != -1:
                dict_graf[i] = count_graf
                isNext = False
            if dict_graf[i] != -1:
                break
        if isNext:
            count_graf += 1
            dict_graf[i] = count_graf 
    return max(dict_graf.values())