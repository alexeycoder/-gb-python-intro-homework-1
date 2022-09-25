# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os

# consts:

TRUE_STR = 'ИСТИНА'
FALSE_STR = 'ЛОЖЬ'
STATEMENT = '\u00ac(X \u22c1 Y \u22c1 Z) = \u00acX \u22c0 \u00acY \u22c0 \u00acZ'


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


def bool_to_str(bool_value):
    return TRUE_STR if bool_value else FALSE_STR


# main flow:

max_len = max(len(TRUE_STR), len(FALSE_STR))
cell_margin = 2
predicates_cell_size = max_len + cell_margin*2
statement_cell_size = len(STATEMENT) + cell_margin*2

horiz_block = '\u2500'
upper_block = '\u252c'
lower_block = '\u2534'
mid_block = '\u253c'
vert_block = '\u2502'

upper_frame = (horiz_block * predicates_cell_size + upper_block) * 3 \
    + horiz_block * statement_cell_size

middle_frame = (horiz_block * predicates_cell_size + mid_block) * 3 \
    + horiz_block*statement_cell_size

lower_frame = (horiz_block * predicates_cell_size + lower_block) * 3 \
    + horiz_block*statement_cell_size

console_clear()
print_title(
    f'Проверка истинности утверждения {STATEMENT} для всех возможных предикат X, Y и Z')

print(upper_frame)

print('X'.center(predicates_cell_size, ' '),
      'Y'.center(predicates_cell_size, ' '),
      'Z'.center(predicates_cell_size, ' '),
      STATEMENT.center(statement_cell_size, ' '),
      sep=vert_block)

for x in False, True:
    for y in False, True:
        for z in False, True:
            result = (not(x or y or z)) == (not x and not y and not z)
            print(middle_frame)
            print(
                bool_to_str(x).center(predicates_cell_size, ' '),
                bool_to_str(y).center(predicates_cell_size, ' '),
                bool_to_str(z).center(predicates_cell_size, ' '),
                bool_to_str(result).center(statement_cell_size, ' '),
                sep=vert_block)

print(lower_frame)
