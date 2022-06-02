'''Numpy will help me to navigate through the rows and columns'''
import numpy as np


import threading


import random


score_board = {'your_score': 0,
               'bots_score': 0}

board = np.array([
 ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
 ['o', '', '', 'o', 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '.', '.', '.'],
 ['', '', '', 'A', '', '', '', '', 'o', '', '', '', '', '', '', '', ''],
 ['', '', '', 'B', '', '', '', 'o', '', 'o', '', '', '', '', '', '', ''],
 ['', '', '', 'C', '', '', 'o', '', 'o', '', 'o', '', '', '', '', '', ''],
 ['', '', '', 'D', '', 'o', '', 'o', '', 'o', '', 'o', '', '', '', '', ''],
 ['', '', '', 'E', 'o', '', 'o', '', 'o', '', 'o', '', 'o', '', '', '', ''],
 ['', 'o', 'o', '', '', '', '', '', '', '', '', '', '', 'o', 'o', 'o', 'o']])

GAME_IS_ON = True
ACTIVE_PLAYERS_SCORE = 'your_score'


def init_game():
    """Print score board game initialization"""

    your_total_score = score_board['your_score']
    print('Your int score: ', your_total_score)
    bot_total_score = score_board['bots_score']
    print('Bot\'s int score: ', bot_total_score)
    print(board[1:7, 3:13])
    position_inputs()


def position_inputs():
    '''Initial game inputs to choose first move'''

    while GAME_IS_ON:
        try:
            row_input = input('Choose a letter from A-E for row: ').upper()
            letters_to_numbers = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6}
            row_input = letters_to_numbers[row_input]
            break
        except ValueError:
            print('Not a required letter, please start again')
            position_inputs()
        except KeyError:
            print('Not a required letter, please start again')
            position_inputs()

    while GAME_IS_ON:
        try:
            column_input = int(input('Your number 1-9 for column: '))
            column_input += 3
            break
        except ValueError:
            print('Not a required number, please try again')
            position_inputs()

    position_is_valid(row_input, column_input)


def position_is_valid(row, column):
    """Valid posiotion choises"""

    if row not in range(1, 7):
        print('Not a required letter, please start again')
        position_inputs()
    elif column not in range(4, 13):
        print('Not a required number, please try again')
        position_inputs()
    elif board[row][column] == '@':
        print('Already chosen, please try again.')
        position_inputs()
    elif board[row][column] == '':
        print('Emply field, please try again.')
        position_inputs()
    else:
        board[row][column] = '@'
        if 'o' in board[2:7, 4:13]:
            print(board[1:7, 3:13])
            check_for_lines()
        else:
            decide_winner()


def while_rows():
    '''Get eatch row and get score for it'''

    all_rows = board[1:6, :]
    for one_row in all_rows:
        while 'o' not in one_row:
            score_board[ACTIVE_PLAYERS_SCORE] += np.count_nonzero(one_row)
            score_board[ACTIVE_PLAYERS_SCORE] -= 1
            # it would not include letter at index 0
            one_row[13] = 'o'
            print('row score:', score_board[ACTIVE_PLAYERS_SCORE])
            break


def while_columns():
    '''Get eatch column and get score for it'''

    for one_column in board.T:
        while 'o' not in one_column:
            score_board[ACTIVE_PLAYERS_SCORE] += np.count_nonzero(one_column)
            score_board[ACTIVE_PLAYERS_SCORE] -= 1
            # it would not include number at index 0
            one_column[len(one_column)-1] = 'o'
            print('column score:', score_board[ACTIVE_PLAYERS_SCORE])
            break


def while_diagonals():
    '''Get each diagonal and score for it'''

    while 'o' not in board.diagonal():
        score_board[ACTIVE_PLAYERS_SCORE] += 2
        board[0][0] = 'o'
    while 'o' not in board.diagonal(2):
        score_board[ACTIVE_PLAYERS_SCORE] += 3
        board[0][2] = 'o'
    while 'o' not in board.diagonal(4):
        score_board[ACTIVE_PLAYERS_SCORE] += 4
        board[0][4] = 'o'
    while 'o' not in board.diagonal(6):
        score_board[ACTIVE_PLAYERS_SCORE] += 5
        board[0][6] = 'o'
    while 'o' not in np.flipud(board).diagonal(3):
        score_board[ACTIVE_PLAYERS_SCORE] += 5
        board[0][10] = 'o'
    while 'o' not in np.flipud(board).diagonal(5):
        score_board[ACTIVE_PLAYERS_SCORE] += 4
        board[0][12] = 'o'
    while 'o' not in np.flipud(board).diagonal(7):
        score_board[ACTIVE_PLAYERS_SCORE] += 3
        board[0][14] = 'o'
    while 'o' not in np.flipud(board).diagonal(9):
        score_board[ACTIVE_PLAYERS_SCORE] += 2
        board[0][16] = 'o'


def check_for_lines():
    '''Get functions to work at the same time'''

    statement_for_rows = threading.Thread(target=while_rows)
    statement_for_columns = threading.Thread(target=while_columns)
    statement_for_diagonals = threading.Thread(target=while_diagonals)
    # position_inputs_again = threading.Thread(target = position_inputs)
    # change_active_players = threading.Thread(target=change_active_player)
    statement_for_diagonals.start()
    statement_for_rows.start()
    statement_for_columns.start()
    print('Your score:', score_board['your_score'])
    print('Bot\'s score:', score_board['bots_score'])
    # change active player
    change_active_player()
    # position_inputs_again.start()


def change_active_player():
    '''Change active player'''

    global ACTIVE_PLAYERS_SCORE
    if ACTIVE_PLAYERS_SCORE == 'your_score':
        ACTIVE_PLAYERS_SCORE = 'bots_score'
        print('bots score=', ACTIVE_PLAYERS_SCORE)
        bot_position_choose()
        return ACTIVE_PLAYERS_SCORE
    else:
        ACTIVE_PLAYERS_SCORE = 'your_score'
        print('your score=', ACTIVE_PLAYERS_SCORE)
        position_inputs()


def bot_position_choose():
    '''Make computer to choose a random position in board'''
    print('got to change_active_player1')
    bots_position_in_row = random.randint(2, 7)
    bots_position_in_column = random.randint(4, 13)
    # I need to eliminate emplty spaces in order to choose right position
    if board[bots_position_in_row][bots_position_in_column] != 'o':
        bot_position_choose()
    else:
        # Once got 'o' in board mark it '@' as taken
        board[bots_position_in_row][bots_position_in_column] = '@'

    print(board[1:7, 3:13])
    # Check if scored:
    check_for_lines()


def decide_winner():
    '''Decide winner'''

    if score_board['your_score'] > score_board['bots_score']:
        print('Congradulations! You are the winner!')
    elif score_board['your_score'] < score_board['bots_score']:
        print('You lost! Sorry.')
    else:
        print('It\'s a draw.')


init_game()
