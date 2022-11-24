import random
import time


class Board:
    board = None
    empty_cell = "□"
    full_cell_x = "☒"
    full_cell_o ="○"

    def create_new_board(self):

        board = self.board = [[Emptycell() for x in range(3)] for y in range(3)]

    def show_board(self):
        print("#"*10)
        for i in range(3):
            print("#", " " * 2, sep="", end="")
            for j in range(3):
                print(self.board[i][j], sep='', end="")
            print(" " * 3, "#", sep="")
        print("#" * 10)

    def get_cell_code(self, x, y):
        return self.board[x][y].CODE

    def change_cell(self, x, y, code):
        self.board[x][y] = Xcell() if code == 'X' else Ocell()

    def get_board(self):
        return self.board


class CellFigure:

        CODE = None
        CELL_IMG = None

        def __init__(self):
            print(f"New Cell Figure {self.CODE}")

        def __str__(self):
            return self.CELL_IMG

        def get_code(self):
            return self.CODE


class Emptycell(CellFigure):
    CODE = 'empty'
    CELL_IMG = "□"


class Xcell(CellFigure):
    CODE = 'X'
    CELL_IMG = "X"


class Ocell(CellFigure):
    CODE = 'O'
    CELL_IMG = "0"


def victory(counter, step_list, cell_code, board):
    if counter < 3:
        return False
    elif counter == 3:
        x_sum = set(map(lambda x: x[0], step_list))
        y_sum = set(map(lambda x: x[1], step_list))
        if (len(x_sum) == len(y_sum) and len(x_sum) == 3) or (
                len(x_sum) + len(y_sum) == 4 and (len(x_sum) == 1 or len(y_sum) == 1)
        ):
            return True
    else:
        str_spis=[]
        # Проверка строк
        for i in range(3):
            for j in range(3):
                str_spis.append(board.get_cell_code(i, j))
            if all(str_spis) == cell_code:
                return True
            else:
                str_spis = []
        # Проверка столбцов
        for i in range(3):
            for j in range(3):
                str_spis.append(board.get_cell_code(j, i))
            if all(str_spis) == cell_code:
                return True
            else:
                str_spis = []

        # Проверка главной диагонали
        for i in range(3):
            str_spis.append(board.get_cell_code(i, i))
            if all(str_spis) == cell_code:
                return True
            else:
                str_spis = []
        # Проверка побочной диагонали
        for i in range(3):
            for j in range(3):
                if i + j == 2:
                    str_spis.append(board.get_cell_code(i, i))
            if all(str_spis) == cell_code:
                return True
            else:
                return False


def chose_cell_user():
    while True:
        print(f"Выберете клетку")
        try:
            x, y = input(f"Введите клетку в формате 'x y' через пробел: ").strip().split()
        except:
            print("Неверный формат входных данных")
            continue

        try:
            x, y = int(x), int(y)
        except:
            print("Неверный формат входных данных")
            print("Нужно ввести 2 числа через пробел")
            continue
        if 0 <= x <= 2 and 0 <= y <= 2:
            return x, y
        else:
            print("Неверный формат входных данных")
            print("числа должны быть натуральными и меньше 3")


def play():

    b = Board()
    b.create_new_board()
    b.show_board()
    counter = 0
    flag = False

    user_cell_code = 'X'
    bot_cell_code = "O"
    user_step_list = []
    rob_step_list = []

    while True:
        if flag:
            break
        x, y = chose_cell_user()

        # ход юзера
        while True:
            if b.get_cell_code(x, y) == 'empty':
                b.change_cell(x, y, user_cell_code)
                b.show_board()

                user_step_list.append((x, y))
                counter += 1

                if victory(counter, user_step_list, user_cell_code, b.get_board()):
                    print("Вы победили")
                    flag = True
                    break
                elif counter == 5:
                    print("Вы проиграли, больше ходов нет")
                    flag = True
                    break
                time.sleep(1)
                break
            else:
                print("Эта клетка занята")
                x, y = chose_cell_user()

        # random-ход противника
        if flag:
            break
        while True:
            x, y = random.choice(range(3)), random.choice(range(3))
            if b.get_cell_code(x, y) == 'empty':
                b.change_cell(x, y, bot_cell_code)
                b.show_board()
                time.sleep(1)
                rob_step_list.append((x, y))
                if victory(counter, rob_step_list, bot_cell_code, b.get_board()):
                    print("Вы проиграли")
                    flag = True
                break


play()
print("Пока")