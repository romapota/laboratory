strs: str
target: int
count: int
flag: bool
flag = False
def req(strs:str)-> str: # функция переставляет знаки по одному по очереди и считает подходит данная расстановка знаков для достижения цели или нет, если да, то печатает строку и выхожит из рекурсия, если нет, вызывает сама себя дальше
    count = strs.count(' ')
    sum = 0
    numbers = []
    s_now = ''
    if count > 0:
        req(strs.replace(' ', '+', 1))
        req(strs.replace(' ', '-', 1))
        return
    strs += '.'#добавляем точку, чтобы обозначить конец для цикла и не выйти за рамки
    for i in range(len(strs) - 1):
        if (strs[i] not in ['+', '-'] and strs[i + 1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):#если элемент не знак и следующий жлемент цифра, то добавляем во временную строку символ
            s_now += strs[i]
        if strs[i + 1] in ['+', '-']:#если следующий символ знак, то добавляем во временную строку текущий символ, добавляем эту строку в список и обнуляем строку
            s_now += strs[i]
            numbers.append(s_now)
            s_now = ''
        if strs[i] in ['+', '-']:#если символ знак, то добавляем его в список
            numbers.append(strs[i])
        if strs[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and strs[i + 1] == '.':#если символ цифра и следующий символ точка, добавляем текущий символ и добавляем получившуюся строку в список
            s_now += strs[i]
            numbers.append(s_now)
            break

    sum = int(numbers[0])#придаем переменной значение первого числа
    for i in range(1, len(numbers) - 1):
        if numbers[i] == '+':#если знак плюса, то прибавляем следующее
            sum += int(numbers[i + 1])
        if numbers[i] == '-':
            sum -= int(numbers[i + 1])#если знак минус, то вычитаем следующее

    if sum == target: #функция переобразующая строку с вычислениями и подсчитыващая результат
        file = open('output.txt', 'w+')
        file.write(strs[0:len(strs)-1] + '=' + str(target))#записываем в файл пример без точки
        file.close()
        print(strs[0:len(strs)-1], '=', target)
        flag = True
        exit()

def get_data()->int:
    global strs, target
    with open('input.txt', 'r', encoding='utf-8') as file:  # открытие файла и считывание с него данных
        strs = file.readline()
        numbers = list(map(int, strs.split()))
        target = numbers.pop()
        strs = strs[strs.find(' ') + 1:strs.rfind(' ')]
def main():
    get_data()
    req(strs)
    if flag == False:
        file = open('output.txt', 'w+')
        file.write('no solution')#записываем в файл пример без точки
        file.close()
        print('no soilution')

if __name__ == '__main__':
    main()