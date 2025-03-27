def alg(graf: list) -> int:
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


def main(graf: list) -> int:
    test_graf = graf.copy()
    count_components = alg(test_graf)
    print('count_components:', count_components)
    list_graf = []
    for i in range(len(test_graf)+1):
        for j in range(len(test_graf)):
            if test_graf[i][j] != 0 and (i+1, j+1) not in list_graf :
                list_graf.append((i+1, j+1))
                test_graf[j][i] = 0
                test_graf[i][j] = 0
                print(list_graf)
                if alg(test_graf) > count_components:
                    print('alg(test_graf):', alg(test_graf))
                print('test_graf:', test_graf)
                test_graf = graf.deepcopy()
                print('test_graf_save:', test_graf)
                

                
        
    