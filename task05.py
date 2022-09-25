# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import os
from collections import namedtuple

# types

Point = namedtuple('Point', 'x y')

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'


class escape_codes:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'      # курсив, может не работать, в ubuntu ok
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    CYAN = '\033[46m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_CYAN = '\033[96m'


# methods:

def calc_distance(point_a, point_b):
    dx = point_a.x - point_b.x
    dy = point_a.y - point_b.y
    return (dx*dx + dy*dy)**0.5


def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(title):
    lines = title.split(sep='\n')
    longest_line = max(lines, key=len)
    border = len(longest_line) * '\u2550'
    print(f'{escape_codes.BRIGHT_CYAN}{escape_codes.BOLD}{border}\n{title}\n{border}{escape_codes.RESET}')


def print_error(message):
    print(f'{escape_codes.RED}\u2757 {message}{escape_codes.RESET}')


def write_highlighted(text, end='\n'):
    print(f'{escape_codes.YELLOW}{text}{escape_codes.RESET}', end=end)


def check_if_valid(float_num):
    return float_num != 0


def make_decimal_separator_invariant(expected_float_str):
    expected_float_str = expected_float_str.replace(',', '.')
    num_of_extra_dots = expected_float_str.count('.') - 1
    if num_of_extra_dots > 0:
        expected_float_str = expected_float_str.replace(
            '.', '', num_of_extra_dots)
    return expected_float_str


def get_user_input_float(prompt, warn_nan):
    not_a_number = False
    while True:
        if not_a_number:
            not_a_number = False
            print_error(warn_nan)

        try:
            inp = input(prompt)
            inp = make_decimal_separator_invariant(inp)
            num = float(inp)
            return num
        except:
            not_a_number = True


def ask_for_repeat():
    answer = input('Желаете повторить (Y/n)? ')
    return len(answer) == 0 or answer[0].lower() == 'y'


# main flow:

user_answer = True

while(user_answer):
    console_clear()
    print_title('Вычисление расстояния между точками А и Б на плоскости')

    print('Введите координаты точки А:')
    pa = Point(get_user_input_float('X?: ', WARN_NAN),
               get_user_input_float('Y?: ', WARN_NAN))

    print('Введите координаты точки Б:')
    pb = Point(get_user_input_float('X?: ', WARN_NAN),
               get_user_input_float('Y?: ', WARN_NAN))

    distance = calc_distance(pa, pb)

    print(f'\nА ({pa.x:g},{pa.y:g}); Б ({pb.x:g},{pb.y:g})', end=' -> ')
    write_highlighted('{:.2f}'.format(distance))
    print()

    user_answer = ask_for_repeat()
