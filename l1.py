def req(strs): # функция переставляет знаки по одному по очереди и считает подходит данная расстановка знаков для достижения цели или нет, если да, то печатает строку и выхожит из рекурсия, если нет, вызывает сама себя дальше
    count = strs.count(' ')
    if count > 0:
        req(strs.replace(' ', '+', 1))
        req(strs.replace(' ', '-', 1))
        return
    if eval(strs) == target: #функция переобразующая строку с вычислениями и подсчитыващая результат
        print(strs, '=', target)
        exit()

def get_data():
    global strs, target
    with open('l1.txt', 'r', encoding='utf-8') as file:  # открытие файла и считывание с него данных
        strs = file.readline()
        numbers = list(map(int, strs.split()))
        target = numbers.pop()
        strs = strs[strs.find(' ') + 1:strs.rfind(' ')]
def main():
    get_data()
    req(strs)


if __name__ == '__main__':
    main()