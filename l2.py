from numpy import array

vars: list
allVar: list
def varios(board: list, x: int, y: int, l: int, n: int, varss: list, allVar: list) -> None:
    while True:#перебор всех ходов
        y += 1
        if y >= n:  #если конец строки, то идем на следующую
            y = 0
            x += 1
        if x >= n:  #если конец таблицы, то выходим
            break
        if board[x][y] == 0:  #Если место доступно для хода, то ставим фигуры
            copy_board=array(board)
            copy_var = [i for i in varss]
            put_figure(copy_board, n, x, y, copy_var)#размещение фигуры
            if l - 1 == 0:#нужен ли еще подбор
                allVar.append(copy_var)
                if len(allVar) == 1:
                    print_board_in_console(copy_board)
                continue
            #продолжение подбора
            varios(copy_board, x, y + 1, l - 1, n, copy_var, allVar)
def search_place(board: list, x: int, y: int, n: int) -> None:#поиск возможных ходов
    #Ходы по осям и диагоналям
    for delta in range(1, n):
        put_danger(board, x + delta, y - delta, n)
        put_danger(board, x - delta, y + delta, n)
        put_danger(board, x + delta, y + delta, n)
        put_danger(board, x-delta, y-delta, n)
        put_danger(board, x, delta, n)
        put_danger(board, delta, y, n)
    #ходы слона
    put_danger(board, x + 2, y + 1, n)
    put_danger(board, x + 2, y - 1, n)
    put_danger(board, x-2, y - 1, n)
    put_danger(board, x-2, y + 1, n)
    put_danger(board, x - 1, y - 2, n)
    put_danger(board, x + 1, y - 2, n)
    put_danger(board, x-1, y + 2, n)
    put_danger(board, x+1, y + 2, n)
def put_danger(board: list, x: int, y: int, n: int) -> bool:#записываем клетки с возможным ударом
    if not (0 <= x < n and 0 <= y < n):#проверка на выход за пределы поля
        return False
    if board[x][y] != 1:#проверка на поставленную фигуру
        board[x][y] = 2
        return True
    else:
        return True
def put_figure(board: list, n: int, x: int, y: int, vars: list) -> None:#размещение фигуры на доске
    board[x][y] = 1
    vars.append((x, y))
    search_place(board, x, y, n)
def save_vars(vars: list) -> None:#запись решений в файл
    with open("output.txt", "w") as f:
        if not len(vars):
            f.write("no solutions")
        else:
            for i_g in vars:
                f.writelines(f"{str(i)} " for i in i_g)
                f.writelines('\n')
    print("Количество решений:", len(vars))
def print_board_in_console(board: list) -> None:#вывод доски

    for m in board:
        s = ""
        for r in m:
            if r == 1:#если стоит фигура, то добавляем '#'
                s += " " + '#'
            elif r == 2:#если клетка с возможным ходом, то добавляем '*'
                s += " " + '*'
            else:#если клетка пустая, то добавляем '0'
                s += " " + '0'
        print(s)
def main() -> None:
    vars = []
    allVar = []
    with open("input.txt", "r") as f_f:
        n, l, k = map(int, f_f.readline().split())
        board = array([[0] * n for _ in range(n)])
        #Добавление расставленных фигур на доску
        for _ in range(k):
            x, y = map(int, f_f.readline().split())
            put_figure(board, n, x, y, vars)
    #Если нужно поставить 0 фигур, то просто печатаем доску
    if l == 0:
        if not (len(vars) == 0):
            allVar.append(vars)
        print_board_in_console(board)
        return save_vars(allVar)
    #подбираем расстановки
    varios(board, 0, -1, l, n, vars, allVar)
    save_vars(allVar)

if __name__ == "__main__":
    main()

