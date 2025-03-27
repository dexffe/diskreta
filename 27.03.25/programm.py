from test_programm import *
import pprint


#? Волновой алгоритм в окрестности Фон Нейма
def program(labirint, coords, finish, wave=2):
    next_coords = []
    while coords:
        x, y = coords.pop(0)
        if [x, y] == finish:
            pprint.pprint(labirint)
            return "Путь найден " + str(wave-1)
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= x + dx < len(labirint) and 0 <= y + dy < len(labirint[y]) and labirint[x + dx][y + dy] == 0:
                labirint[x + dx][y + dy] = wave
                next_coords.append([x + dx, y + dy])
    if next_coords == []:
        return "Такого пути не существует"
    wave += 1
    return program(labirint, next_coords, finish, wave)


print(program(labirint1, start1, finish1))
print('--------')
print(program(labirint2, start2, finish2))
print('--------')
print(program(labirint3, start3, finish3))