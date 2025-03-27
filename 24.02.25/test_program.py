from program import main

# ? Star 
graf1 = [[0, 0, 10, 1, 0], 
         [0, 0, 0, 4, 7], 
         [10, 0, 0, 0, 8], 
         [1, 4, 0, 0, 0], 
         [0, 7, 8, 0, 0]]

# ? Square
graf2 = [[0, 4, 0, 8], 
         [4, 0, 3, 0], 
         [0, 3, 0, 5], 
         [8, 0, 5, 0]]

# ? Example
graf3 = [[0, 2, 0, 2, 0, 0, 0], 
         [2, 0, 7, 3, 0, 0, 0],
         [0, 7, 0, 0, 0, 9, 0],
         [2, 3, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 3, 10],
         [0, 0, 9, 0, 3, 0, 0],
         [0, 0, 0, 5, 10, 0, 0]]


graf4 = [[1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1],
         [0, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 0, 1, 1]]

main(graf4)

# ! так как assert меняет значение передаваеммого списка в функции,
# !  то использовать assert стоит для проверки только одного алгоритма.

# ! Код первого алгоритма удаляет дороги в графе, поэтому граф полностью обнуляеся
# !  и во второй алгоритм призодит не изначальный граф, а нулевой.

# assert alg2(graf1) == 20, 'Ошибка в обработке графа, не верный ответ'
# assert alg2(graf2) == 12, 'Ошибка в обработке графа, не верный ответ'
# assert alg2(graf3) == 28, 'Ошибка в обработке графа, не верный ответ'

# assert alg1(graf1) == 20, 'Ошибка в обработке графа, не верный ответ'
# assert alg1(graf2) == 12, 'Ошибка в обработке графа, не верный ответ'
# assert alg1(graf3) == 28, 'Ошибка в обработке графа, не верный ответ'

# print('Все тесты прошли успешно')