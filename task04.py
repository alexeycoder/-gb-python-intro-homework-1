# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import os


# consts:

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

def get_range_by_quarter_description(quarter):
    match quarter:
        case 1:
            return 'X\u2208(0,+\u221e), Y\u2208(0,+\u221e)  \u2261  X > 0, Y > 0'
        case 2:
            return 'X\u2208(-\u221e,0), Y\u2208(0,+\u221e)  \u2261  X < 0, Y > 0'
        case 3:
            return 'X\u2208(-\u221e,0), Y\u2208(-\u221e,0)  \u2261  X < 0, Y < 0'
        case 4:
            return 'X\u2208(0,+\u221e), Y\u2208(-\u221e,0)  \u2261  X > 0, Y < 0'

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


def check_if_valid(value):
    return value in [1, 2, 3, 4]


def get_user_input_int(prompt, warn_nan, warn_out_of_range):
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
            num = int(input(prompt))
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
    console_clear()
    print_title('Диапазон возможных значений координат по номеру четверти плоскости XY\n'
                '(где X и Y \u2014 горизонтальная и вертикальная оси координат соответственно)')

    quarter = get_user_input_int(
        'Введите номер четверти плоскости XY: ',
        'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.',
        'Номер должен быть в диапазоне от 1 до 4. Пожалуйста попробуйте снова.')

    range_description = get_range_by_quarter_description(quarter)

    print(f'\nВывод: {quarter} четверть -> ', end='')
    write_highlighted(range_description)
    print()

    user_answer = ask_for_repeat()
