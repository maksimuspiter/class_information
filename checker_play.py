from abc import abstractmethod

figure = {
    "white_checker": "⛀",
    "black_checker": "⛂",
    "white_queen": "⛁",
    "black_queen": "⛃",
    "empty_cell": "□",
    "empty_cell2": "☒"

}



class Board:

    board = None

    def start(self):

        board = self.board = [[EmptyCell() for x in range(8)] for y in range(8)]
        black = "BLACK"
        white = "WHITE"
        for i in range(8):
            for j in range(8):
                if i <= 2 and (i + j) % 2 != 0:
                    self.board[i][j] = Checker(white)
                elif i >= 5 and (i + j) % 2 != 0:
                    self.board[i][j] = Checker(black)

    def show_board(self):
        print(' ' * 16, "#" * 22, sep='')
        print(' ' * 16, "#", ' ' * 6, "ABCDEFGH", ' ' * 6, "#", sep='')
        if self.board:
            for i in range(8):
                print(' ' * 16, "#", ' ' * 4, 8 - i, sep='', end=' ')
                for j in range(8):
                    print(self.board[i][j], sep='', end="")
                print(' ', 8 - i, ' ' * 4, "#",  sep="" )
        print(' ' * 16, "#", ' ' * 6, "ABCDEFGH", ' ' * 6, "#", sep='')
        print(' ' * 16, "#" * 22, sep='')

    def show_board_test(self):
        print(' ' * 16, "#" * 22, sep='')
        print(' ' * 16, "#", ' ' * 6, "01234567", ' ' * 6, "#", sep='')
        if self.board:
            for i in range(8):
                print(' ' * 16, "#", ' ' * 4, i, sep='', end=' ')
                for j in range(8):
                    print(self.board[i][j], sep='', end="")
                print(' ', i, ' ' * 4, "#", sep="")
        print(' ' * 16, "#", ' ' * 6, "01234567", ' ' * 6, "#", sep='')
        print(' ' * 16, "#" * 22, sep='')

    def clone(self):
        new_board = Board()
        new_board.board = [self.board[i][:] for i in range(8)]
        return new_board

    def get_checker_figure(self, x, y):
        return self.board[x][y]

    def get_color(self, x, y):
        return self.get_checker_figure(x, y).color

    def move_checker_figure(self, xy_from: (int, int), xy_to: (int, int)):
        """
            Перемещение шашки в новую позицию.
            Создается новая пустая клетка.
            Без удаления шашки противника.
        """
        x_old, y_old = xy_from
        x_new, y_new = xy_to
        if (0 <= x_old <= 7 and 0 <= y_old <= 7 and 0 <= x_new <= 7 and 0 <= y_new <= 7
            and self.board[x_old][y_old].CODE == 'checker'
            and self.board[x_new][y_new].CODE == 'empty'
            and (xy_to in self.board[x_old][y_old].possible_moves(x_old, y_old))):

            self.board[x_old][y_old], self.board[x_new][y_new] = EmptyCell(), self.board[x_old][y_old]
            return True
        else:
            return False

    def kill_checker_figure(self, xy_killer: (int, int), xy_dead: (int, int), xy_new_position: (int, int)):
        """
            Перемещение шашки в новую позицию.
            Создается новая пустая клетка вместо съеденной шашки противника.
            Удалеяется шашка противника, вместо нее --> EmptyCell.
            xy_killer - позиция шашки, которая ходит.
            xy_dead - позиция шашки, которую хотят срубить.

        x_old, y_old = xy_killer
        x_new, y_new = xy_dead
        if (0 <= x_old < 7 and 0 <= y_old < 7 and 0 <= x_new < 7 and 0 <= y_new < 7
            and (
                0 <= x_old + (x_new - x_old) * 2 <= 7 and
                0 <= y_old + (y_new - y_old) * 2 <= 7
                )
            and self.board[x_old][y_old].CODE == self.board[x_new][y_new].CODE == 'checker'
            and self.board[x_old][y_old].color != self.board[x_new][y_new].color
            and ((x_new, y_new) in self.board[x_old][y_old].possible_moves(x_old, y_old))
        ):

            self.board[x_old][y_old], self.board[x_new][y_new],
            self.board[x_old + (x_new - x_old) * 2][y_old + (y_new - y_old)] = \
                EmptyCell(), EmptyCell(), self.board[x_old][y_old]
            return True
        else:
            return False

        """
        x_old, y_old = xy_killer
        x_midle, y_midle = xy_dead
        x_new, y_new = xy_new_position
        if (
                0 <= x_old <= 7
            and 0 <= y_old <= 7
            and 0 <= x_midle <= 7
            and 0 <= y_midle <= 7
            and 0 <= x_new <= 7
            and 0 <= y_new <= 7

            and self.board[x_old][y_old].CODE == self.board[x_midle][y_midle].CODE == 'checker'
            and self.board[x_old][y_old].color != self.board[x_midle][y_midle].color
            and ((x_midle, y_midle) in self.board[x_old][y_old].possible_moves(x_old, y_old))
            and ((x_new, y_new) in self.board[x_old][y_old].possible_position_after_kill(x_old, y_old))
        ):

            self.board[x_old][y_old], self.board[x_midle][y_midle], self.board[x_new][y_new] = \
                EmptyCell(), EmptyCell(), self.board[x_old][y_old]
            return True
        else:
            return False


    def is_empty(self, x, y):
        """Проверка на пустоту (EmptyCell)"""
        return self.get_checker_figure(y, x).CODE == 'empty'


class EmptyCell:
    CODE = "empty"
    number_empty_cell = 0

    def __str__(self):
        # return ("□", "☒")
        return "□"

    def get_moves(self, board, x, y):
        raise Exception('Error!')


class Figure:
    CODE = None
    WHITE_IMG = None
    BLACK_IMG = None

    color = None

    def __init__(self, color):
        self.color = color
        print(f"{self.color} создан")

    def __str__(self):
        return self.WHITE_IMG if self.color == "WHITE" else self.BLACK_IMG

    def __del__(self):
        print(f"{self.color} удален")


class Checker(Figure):
    # WHITE_IMG = '⛀'
    # BLACK_IMG = '⛂'
    CODE = "checker"

    WHITE_IMG = '*'
    BLACK_IMG = '⛂'

    def possible_moves(self, x, y):
        if self.color == "WHITE":
            possible_moves_1 = ((x + 1), (y - 1)) if x < 7 and y > 0 else None
            possible_moves_2 = ((x + 1), (y + 1)) if x < 7 and y < 7 else None
            return (possible_moves_1, possible_moves_2)
        elif self.color == "BLACK":
            possible_moves_1 = ((x - 1), (y - 1)) if x > 0 and y > 0 else None
            possible_moves_2 = ((x - 1), (y + 1)) if x > 0 and y < 7 else None
            return (possible_moves_1, possible_moves_2)
        else:
            return None

    def possible_position_after_kill(self, x, y):
        """
            Можно рубить назад
        """
        if self.CODE == "checker":
            possible_moves_1 = ((x + 2), (y + 2)) if x < 6 and y < 6 else None
            possible_moves_2 = ((x + 2), (y - 2)) if x < 6 and y > 1 else None
            possible_moves_3 = ((x - 2), (y + 2)) if x > 1 and y < 6 else None
            possible_moves_4 = ((x - 2), (y - 2)) if x > 1 and y > 1 else None
            return (possible_moves_1, possible_moves_2)


        else:
            return None





b1 = Board()

b1.start()
b1.show_board_test()

if b1.move_checker_figure((5, 2), (4, 1)):
    b1.show_board_test()

if b1.move_checker_figure((4, 1), (3, 2)):
    b1.show_board_test()

if b1.move_checker_figure((2, 7), (3, 6)):
    b1.show_board_test()

print(b1.kill_checker_figure((2, 1), (3, 2), (4, 3)))
b1.show_board_test()