'''Numpy will help me to navigate through the rows and columns'''
import numpy as np

score_board = {'you': ['|', 'score: 0', '|'],
               'bot': ['|', 'score: 0', '|']}

board = np.array([['', 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['A', '', '', '', '', 'o', '', '', '', ''],
                  ['B', '', '', '', 'o', '', 'o', '', '', ''],
                  ['C', '', '', 'o', '', 'o', '', 'o', '', ''],
                  ['D', '', 'o', '', 'o', '', 'o', '', 'o', ''],
                  ['E', 'o', '', 'o', '', 'o', '', 'o', '', 'o']])

GAME_IS_ON = True

print(board.diagonal())

def init_game():
    """Print score board game init"""

    your_score = score_board['you']
    #global active_player
    active_player = your_score
    print('Your score: ')
    print(your_score)
    bot_score = score_board['bot']
    print('Bot\'s score: ')
    print(bot_score)
    for i in range(6):
        print(board[i])
    position_inputs()

def position_inputs():
    '''Initial game inputs to choose first move'''

    while GAME_IS_ON:
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

    while GAME_IS_ON:
        try:
            column_input = int(input('Choose number for your position from 1-9 in a column: '))
            break
        except ValueError:
            print('Not a required number, please try again')
            position_inputs()

    position_is_valid(row_input, column_input)

def position_is_valid(row, column):
    """Valid posiotion choises"""

    if row not in range(1, 6):
        print('Not a required letter, please start again')
        position_inputs()
    elif column not in range(1, 10):
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
        for i in range(6):
            print(board[i])
        check_for_lines()#was before position_inputs()

def check_for_lines():
    '''Check if got lines for score'''

    all_rows = board[1:6, :]
    for row in all_rows:
        if 'o' not in row:
            score = np.count_nonzero(row)
            score -= 1 #it would not include letter at index 0
            print(score)
            print(row)

    for column in board.T:
        if 'o' not in column:
            # if column != board[:, 0:1]:
            #     print('here for all columns')
            print(column)
            
            score = np.count_nonzero(column)
            score -= 1 #it would not include number at index 0
            print(score)
    position_inputs()
    
    # all_diagonals = {'diagonal_line_1' : [[board[1][5]], [board[2][4]], [board[3][3]], [board[4][2]], [board[5][1]]]}
    #                 # 'diagonal_line_2' :
    #                 # 'diagonal_line_3' :
    #                 # 'diagonal_line_4' :
    #                 # 'diagonal_line_5' :
    #                 # 'diagonal_line_6' :
    #                 # 'diagonal_line_7' :
    #                 # 'diagonal_line_8' :

    # lines_score = diagonal_lines.diagonal_line_1[0] = 5
    # diagonal_lines.diagonal_line_1[1] = 4,
    # diagonal_lines.diagonal_line_1[2] = 3,
    # diagonal_lines.diagonal_line_1[3] = 2,
    # diagonal_lines.diagonal_line_1[4] = 5,
    # diagonal_lines.diagonal_line_1[5] = 4,
    # diagonal_lines.diagonal_line_1[6] = 3,
    # diagonal_lines.diagonal_line_1[7] = 2

    #check_score(row, all_rows)

init_game()