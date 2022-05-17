'''Numpy will help me to navigate through the rows and columns'''
import numpy as np

score_board = {'you': ['|', 'score: 0', '|'],
               'bot': ['|', 'score: 0', '|']}

board = np.array([['', 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['A', '', '', '', '', 'o', '', '', '', ''],
                  ['B', '', '', '', 'o', '', 'o', '', '', ''],
                  ['C', '', '', 'o', '', 'o', '', 'o', '', ''],
                  ['D', '', 'o', '', 'o', '', 'o', '', 'o', ''],
                  ['E', 'o', '', 'o', '', 'o', '', 'o', '', 'o'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

#game_is_on = True

def print_game():
    """Print score board game init"""

    YOU = score_board['you']
    #global active_player
    active_player = YOU
    print('Your score: ')
    print(YOU)
    BOT = score_board['bot']
    print('Bot\'s score: ')
    print(BOT)
    for i in range(7):
        print(board[i])
    position_inputs()

def position_inputs():
    '''Initial game inputs to choose first move'''

    while True:
        try:
            row_input = input('Choose letter for your position from A-E move in a row: ').upper()
            letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
            row_input = letters_to_numbers[row_input]
            break
        except ValueError:
            print('Not a required letter, please start again')
            position_inputs()
        except KeyError:
            print('Not a required letter, please start again')
            position_inputs()

    while True:
        try:
            column_input = int(input('Choose number for your position from 1-9 in a column: '))
            break
        except ValueError:
            print('Not a required number, please try again')
            position_inputs()

    position_is_valid(row_input, column_input)

def position_is_valid(row, column):
    """Valid posiotion choises"""

    if board[row][column] == '@':
        print('Already chosen, please try again.')
        position_inputs()
    elif board[row][column] == '':
        print('Emply field, please try again.')
        position_inputs()
    else:
        board[row][column] = '@'
        for i in range(7): print(board[i])
        position_inputs()

print_game()