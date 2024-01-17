def checkk(i):#на вход получает одно из значений координат из списка "не опасных" точек на шахматной доске
        global summ
        summ = 0
        checks = 0
        danger_new = dangers_places_def(n, i, 0)
        if i not in dangers_places: #проверка входит ли данная координата в "опасный список"
            for p in places:#проверка будет ли входить одна из уже размещенных фигур в новый "опасный" список
                for d in danger_new:
                    if p == d:
                        checks = 1#если да, то checks = 1
                        break
            if checks == 0:#если нет, то новая фигура, то новая фигура добавляется в список фигур и обновляется "опасный" список
                places.append((i[0], i[1]))
                for i in danger_new:
                    dangers_places.append(i)
                dangers_places_def(n, i, 1)
                return True
def dangers_places_def(n, i, c):#поиск опасных "координат", переменная отвечает за добавление найденных опасных ходов в общий список. Если с = 1, то будут добавлены, если с = 0 - нет
    #везде есть проверка на то, чтобы значения были в пределах доски
    i = list(i)
    global danger
    danger = []
    #опасные места по горизонтальной линии
    for x in range(0, n+1):
        danger.append([x, i[1]])
    #опасные места по вертикали
    for y in range(0, n+1):
        danger.append([i[0], y])
    #опасные места по главной диагонали
    for j in range(1, n+1):
        danger.append([i[0]+j, i[1]+j])
    if i[0] != 0 and i[1] != 0:
        if i[0] < i[1]:
            minn = i[0]
        else:
            minn = i[1]
        for j in range(minn, 0, -1):
            danger.append([i[0]-j, i[1]-j])
    #опасные места по побочной диагонали
    if i[1] != 0:
        if i[0] < i[1]:
            minn = i[0]
        else:
            minn = i[1]
        for j in range(1, minn+1):
            if i[1]-j >= 0:
                danger.append([i[0]+j, i[1]-j])
    if i[0] != 0:
        if i[0] > i[1]:
            minn = i[0]
        else:
            minn = i[1]
        for j in range(0, minn+1):
            if i[0]-j >= 0:
                danger.append([i[0]-j, i[1]+j])
    #опасные места, конь
    if i[0] + 2 <= n and i[1] + 1 <= n:
        danger.append([i[0]+2, i[1]+1])
    if i[0] + 1 <= n and i[1] + 2 <= n:
        danger.append([i[0]+1, i[1]+2])
    if i[0] - 2 >= 0 and i[1] - 1 >= 0:
        danger.append([i[0]-2, i[1]-1])
    if i[0] - 1 >= 0 and i[1] - 2 >= 0:
        danger.append([i[0]-1, i[1]-2])
    if i[0] + 1 >= 0 and i[1] - 2 >= 0:
        danger.append([i[0] + 1, i[1] - 2])
    if i[0] + 2 >= 0 and i[1] - 1 >= 0:
        danger.append([i[0] + 2, i[1] - 1])
    if i[0] - 1 >= 0 and i[1] + 2 >= 0:
        danger.append([i[0] - 1, i[1] + 2])
    if i[0] - 2 >= 0 and i[1] + 1 >= 0:
        danger.append([i[0] - 2, i[1] + 1])
    if c == 1:
            for i in danger:
                if i not in dangers_places and ((i[0], i[1]) not in places) :
                    dangers_places.append(i)
    return danger
def free_place_def(n):
    free_place = []
    for i in range(n):#перебор всех координат на N-ой доске. Если координата не входит в "опасный" список и в список уже размещенных фигур, то координата добавляется в список свободных мест
        for j in range(n):
            if ([i, j] not in dangers_places) and ((i, j) not in places):
                free_place.append([i, j])
    return free_place

def get_data():
    with open(f'l2.txt', 'r', encoding='utf-8') as file:
        n, l, k = map(int, file.readline().split())
        places = []
        for _ in range(k):
            a = tuple(map(int, file.readline().split()))
            places.append(a)
        return n, l, k, places
def main():
    global dangers_places, places, n, count, k
    n, l, k, places = get_data()
    summ = 0
    dangers_places = []
    for i in places:#заполнение "опасного" списка
        dangers_places_def(n, i, 1)
    free_place = free_place_def(n)
    for i in free_place:#перебор координат из "безопасного" списка и поиск подходящих точек
        if summ < l+1:
            if checkk(i):
                summ += 1
        if summ == l:
            break
    print(places)
    if len(places)-k == l:
        for y in range(n+1):
            for x in range(n+1):
                el = [x, y]
                if (x, y) in places:#если такая же координата есть в списке размещенных фигур, то выводится "#"
                    print('#', end=' ')
                    continue
                elif [x, y] in dangers_places:#если такая же координата есть в списке опасных значений, то выводится "*"
                    print('*', end=' ')
                    continue
                else:#если такой координаты нет, то выводится "0"
                    print('0', end=' ')
            print('\n')

    else:
        return print('no solution')
if __name__ == '__main__':
    main()