'''Numpy official documentation at: https://numpy.org/doc/'''
import threading
import random
import numpy as np

score_board = {'your_score': 0,
               'bots_score': 0}

board = np.array([
 [
  '', '', '', 'o', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ], [
  'o', '', '', '.  ', '1', '2',
  '3', '4 ', '5 ', '6 ', '7 ', '8 ',
  '9', '.', '.', '.', ''
 ], [
  '', '', '', 'A       ', '', '',
  '', '', 'o', '', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', 'B     ', '', '',
  '', 'o', '   ', 'o', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', 'C    ', '', '',
  'o', '  ', 'o', '   ', 'o', '',
  '', '', '', '', ''
 ], [
  '', '', '', 'D   ', '', 'o',
  ' ', 'o', '   ', 'o', '   ', 'o',
  '', '', '', '', ''
 ], [
  '', '', '', 'E ', 'o', '  ',
  'o', '  ', 'o', '   ', 'o', '   ',
  'o', '', '', '', ''
 ], [
  '', 'o', 'o', '', '', '',
  '', '', '', '', '', '',
  '', '', 'o', 'o', 'o'
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', 'o', '', '', ''
 ], [
  '', '', '', '', '', '',
  '', '', '', '', '', '',
  '', '', '', '', ''
 ]])


ACTIVE_PLAYERS_SCORE = 'your_score'


def choose_level():
    '''input to choose players level'''

    print('  ~~~~~~~. Welcome .~~~~~~~ \n')
    print(' ~~~~~~~~~. to  .~~~~~~~~~~~ \n')
    print('~~~~~~~. Pyramid Game .~~~~~~~ \n')
    print('                                  ')

    game_on = True
    while game_on:
        try:
            print('Choose your game level- \n')
            level_input = str(input('E for easy or H for hard: \n')).upper()
            chosen_level_validation(level_input)
            break
        except KeyError:
            print('Not a required letter, please try again \n')
            choose_level()


def chosen_level_validation(check_input):
    '''Check if level choise is valid'''

    if check_input == 'E' or check_input == 'H':
        level_is_chosen(check_input)
    else:
        print('It must be E or H, please try again: \n')
        choose_level()


def level_is_chosen(chosen_level):
    '''Decide level of the game that the player chooses'''

    global ACTIVE_PLAYERS_SCORE
    if chosen_level == 'E':
        ACTIVE_PLAYERS_SCORE = 'your_score'
        init_game()
    else:
        ACTIVE_PLAYERS_SCORE = 'bots_score'
        init_game()


def init_game():
    '''Print score, board as game initialization
    and from chosen level decide who starts the game
    '''
    print_board()

    if ACTIVE_PLAYERS_SCORE == 'your_score':
        position_inputs()
    else:
        bot_position_choose()


def print_board():
    '''Print board and score'''

    print("------------------------------------- \n")
    line1 = '. '.join(board[1][3:13])
    print(line1)
    line2 = '  '.join(board[2][3:13])
    print(line2)
    line3 = '  '.join(board[3][3:13])
    print(line3)
    line4 = '  '.join(board[4][3:13])
    print(line4)
    line5 = '  '.join(board[5][3:13])
    print(line5)
    line6 = '  '.join(board[6][3:13])
    print(line6)
    print("------------------------------------- \n")
    your_score = score_board['your_score']
    bots_score = score_board['bots_score']
    print(f'Your score: {your_score}')
    print(f'Bot\'s score: {bots_score}')


def position_inputs():
    '''Game inputs( to choose a position) provided for the player'''

    game = True

    while game:
        try:
            row_input = input('Choose a letter from A-E in row: ').upper()
            letters_to_numbers = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6}
            row_input = letters_to_numbers[row_input]
            break
        except ValueError:
            print('Not a required letter, please start again \n')
            position_inputs()
        except KeyError:
            print('Not a required letter, please start again \n')
            position_inputs()

    while game:
        try:
            column_input = int(input('Your number 1-9 in column: \n'))
            column_input += 3
            break
        except ValueError:
            print('Not a required number, please try again \n')
            position_inputs()

    position_is_valid(row_input, column_input)


def position_is_valid(row, column):
    '''Valid posiotion choises'''

    if row not in range(1, 7):
        print('Not a required letter, please start again \n')
        position_inputs()
    elif column not in range(4, 13):
        print('Not a required number, please try again \n')
        position_inputs()
    elif board[row][column] == '@':
        print('Already chosen, please try again. \n')
        position_inputs()
    elif board[row][column] == '':
        print('Emply field, please try again. \n')
        position_inputs()
    else:
        board[row][column] = '@'
        check_for_lines()


def while_rows():
    '''Get eatch row and get score for it'''

    all_rows = board[1:7, :]
    for one_row in all_rows:
        old_score = score_board.get(ACTIVE_PLAYERS_SCORE)
        while 'o' not in one_row:
            score_board[ACTIVE_PLAYERS_SCORE] += np.count_nonzero(one_row)
            score_board[ACTIVE_PLAYERS_SCORE] -= 1
            # it would not include letter at index 0
            one_row[16] = 'o'
            new_value = score_board.get(ACTIVE_PLAYERS_SCORE)
            update = new_value - old_score
            print(f'Line in row {ACTIVE_PLAYERS_SCORE} is up by {update}')
            break


def while_columns():
    '''Get eatch column and get score for it'''

    for one_column in board.T:
        old_score = score_board.get(ACTIVE_PLAYERS_SCORE)
        while 'o' not in one_column:
            score_board[ACTIVE_PLAYERS_SCORE] += np.count_nonzero(one_column)
            score_board[ACTIVE_PLAYERS_SCORE] -= 1
            # it would not include number at index 0
            one_column[len(one_column)-1] = 'o'
            new_value = score_board.get(ACTIVE_PLAYERS_SCORE)
            update = new_value - old_score
            print(f'Line in column {ACTIVE_PLAYERS_SCORE} is up by {update}')
            break


def while_diagonals():
    '''Get each diagonal if all '@'s and score for it'''

    while 'o' not in board.diagonal():
        score_board[ACTIVE_PLAYERS_SCORE] += 2
        board[0][0] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 2 ')
        break
    while 'o' not in board.diagonal(2):
        score_board[ACTIVE_PLAYERS_SCORE] += 3
        board[0][2] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 3 ')
        break
    while 'o' not in board.diagonal(4):
        score_board[ACTIVE_PLAYERS_SCORE] += 4
        board[12][16] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 4 ')
        break
    while 'o' not in board.diagonal(6):
        score_board[ACTIVE_PLAYERS_SCORE] += 5
        board[10][16] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 5 ')
        break
    while 'o' not in np.flipud(board).diagonal(-3):
        score_board[ACTIVE_PLAYERS_SCORE] += 5
        board[10][0] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 5 ')
        break
    while 'o' not in np.flipud(board).diagonal(-1):
        score_board[ACTIVE_PLAYERS_SCORE] += 4
        board[12][0] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 4 ')
        break
    while 'o' not in np.flipud(board).diagonal(1):
        score_board[ACTIVE_PLAYERS_SCORE] += 3
        board[0][14] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 3 ')
        break
    while 'o' not in np.flipud(board).diagonal(3):
        score_board[ACTIVE_PLAYERS_SCORE] += 2
        board[0][16] = 'o'
        print(f'Line in diagonal {ACTIVE_PLAYERS_SCORE} is up by 2 ')
        break


def check_for_lines():
    '''Get to functions that count scores:
    for lines in rows,
    for lines in columns,
    for lines in diagonals - to work at the same time
    '''

    statement_for_rows = threading.Thread(target=while_rows)
    statement_for_columns = threading.Thread(target=while_columns)
    statement_for_diagonals = threading.Thread(target=while_diagonals)
    statement_for_diagonals.start()
    statement_for_rows.start()
    statement_for_columns.start()
    print_board()
    check_game_is_on()


def check_game_is_on():
    '''Check if game is on before continue with next player'''

    if 'o' in board[2:7, 4:13]:
        change_active_player()
    else:
        decide_winner()


def change_active_player():
    '''Change active player'''

    global ACTIVE_PLAYERS_SCORE
    if ACTIVE_PLAYERS_SCORE == 'your_score':
        ACTIVE_PLAYERS_SCORE = 'bots_score'
        bot_position_choose()
        return ACTIVE_PLAYERS_SCORE
    else:
        ACTIVE_PLAYERS_SCORE = 'your_score'
        position_inputs()


def bot_position_choose():
    '''For computer to choose a random position in board'''

    bots_position_in_row = random.randint(2, 6)
    bots_position_in_column = random.randint(4, 12)
    # I need to eliminate emplty spaces in order to choose right position
    if board[bots_position_in_row][bots_position_in_column] != 'o':
        bot_position_choose()
    else:
        # Once got 'o' in board mark it '@' as taken
        board[bots_position_in_row][bots_position_in_column] = '@'
        # Check if scored:
        check_for_lines()


def decide_winner():
    '''Decide winner'''

    if score_board['your_score'] > score_board['bots_score']:
        print('///////////////////////////////////////// \n')
        print('Congradulations! You are the winner! \n')
        print('/////////////////////////////////////////')
    elif score_board['your_score'] < score_board['bots_score \n']:
        print('///////////////////////////////////////// \n')
        print('You lost! Sorry. \n')
        print('///////////////////////////////////////// \n')
    else:
        print('///////////////////////////////////////// \n')
        print('It\'s a draw. \n')
        print('///////////////////////////////////////// \n')


choose_level()
