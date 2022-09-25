# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

import os

# consts:

WARN_NAN = 'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.'
WARN_OUT_OF_RANGE = 'Нулевое значение координаты недопустимо. Пожалуйста попробуйте снова.'


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

def get_plane_quarter(x, y):
    if x > 0:
        if y > 0:
            return '1-ая'
        elif y < 0:
            return '4-ая'
    elif x < 0:
        if y > 0:
            return '2-ая'
        elif y < 0:
            return '3-я'
    return ''


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


def get_user_input_float(prompt, warn_nan, warn_out_of_range):
    not_a_number = False
    out_of_range = False
    while True:
        if not_a_number:
            not_a_number = False
            print_error(warn_nan)
        if out_of_range:
            out_of_range = False
            print_error(warn_out_of_range)

        try:
            inp = input(prompt)
            inp = make_decimal_separator_invariant(inp)
            num = float(inp)
            out_of_range = not check_if_valid(num)
            if not out_of_range:
                return num
        except:
            not_a_number = True


def ask_for_repeat():
    answer = input('Желаете повторить (Y/n)? ')
    return len(answer) == 0 or answer[0].lower() == 'y'


# main flow:

user_answer = True

while(user_answer):
    # console_clear()
    print_title(
        'Определение номера четверти плоскости XY\n(где X и Y \u2014 горизонтальная и вертикальная оси соответственно)')

    x = get_user_input_float(
        'Введите координату X (X\u22600): ',
        WARN_NAN, WARN_OUT_OF_RANGE)

    y = get_user_input_float(
        'Введите координату Y (Y\u22600): ',
        WARN_NAN, WARN_OUT_OF_RANGE)

    quarter = get_plane_quarter(x, y)

    print(f'\n(X={x:g}; Y={y:g})', end=' -> ')
    write_highlighted(quarter + ' четверть')
    print()

    user_answer = ask_for_repeat()
