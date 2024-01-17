

def main():
    global dangers_places, places, n, count, k
    n, l, k, places = get_data()
    summ = 0
    dangers_places = []
    for i in places:  # заполнение "опасного" списка
        dangers_places_def(n, i, 1)
    free_place = free_place_def(n)
    if l != 0:
        for i in free_place:  # перебор координат из "безопасного" списка и поиск подходящих точек
            if summ < l + 1:
                if checkk(i):
                    summ += 1
            if summ == l:
                break
        print(places)
        if len(places) - k == l:
            for y in range(n + 1):
                for x in range(n + 1):
                    el = [x, y]
                    if (x, y) in places:  # если такая же координата есть в списке размещенных фигур, то выводится "#"
                        print('#', end=' ')
                        continue
                    elif [x,
                          y] in dangers_places:  # если такая же координата есть в списке опасных значений, то выводится "*"
                        print('*', end=' ')
                        continue
                    else:  # если такой координаты нет, то выводится "0"
                        print('0', end=' ')
                print('\n')

        else:
            return print('no solution')
    else:
        for y in range(n + 1):
                for x in range(n + 1):
                    el = [x, y]
                    if (x, y) in places:  # если такая же координата есть в списке размещенных фигур, то выводится "#"
                        print('#', end=' ')
                        continue
                    elif [x,
                          y] in dangers_places:  # если такая же координата есть в списке опасных значений, то выводится "*"
                        print('*', end=' ')
                        continue
                    else:  # если такой координаты нет, то выводится "0"
                        print('0', end=' ')
                print('\n')

if __name__ == '__main__':
    main()
