# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

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

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(title):
    border = len(title) * '\u2550'
    print(f'{escape_codes.BRIGHT_CYAN}{escape_codes.BOLD}{border}\n{title}\n{border}{escape_codes.RESET}')


def print_error(message):
    print(f'{escape_codes.RED}\u2757 {message}{escape_codes.RESET}')


def write_highlighted(text, end='\n'):
    print(f'{escape_codes.YELLOW}{text}{escape_codes.RESET}', end=end)


def check_if_weekend(day_of_week):
    return day_of_week in [6, 7]


def check_if_valid(value):
    return value >= 1 and value <= 7


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
    print_title('Проверка соответсвия номера дня недели выходному дню')

    day_of_week_num = get_user_input_int(
        'Введите номер дня недели (1 - Пн,\u2026, 7 - Вc): ',
        'Некорректный ввод: введено нечисловое значение. Пожалуйста попробуйте снова.',
        'Номер должен быть в диапазоне от 1 до 7. Пожалуйста попробуйте снова.')

    result = 'Да' if check_if_weekend(day_of_week_num) else 'Нет'

    print(f'\nВывод: {day_of_week_num} -> ', end='')
    write_highlighted(result)
    print()

    user_answer = ask_for_repeat()
