'''Numpy will help me to navigate through the rows and columns'''
import numpy as np

score_board = {'your_score': 0,
               'bots_score': 0}

board = np.array([['o', 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '.', '.'],
                  ['A', '', '', '', '', 'o', '', '', '', '', '', '', ''],
                  ['B', '', '', '', 'o', '', 'o', '', '', '', '', '', ''],
                  ['C', '', '', 'o', '', 'o', '', 'o', '', '', '', '', ''],
                  ['D', '', 'o', '', 'o', '', 'o', '', 'o', '', '', '', ''],
                  ['E', 'o', '', 'o', '', 'o', '', 'o', '', 'o', '', '', ''], 
                  ['','','','','','','','','','','','','']])

GAME_IS_ON = True

def init_game():
    """Print score board game init"""

    your_total_score = score_board['your_score']
    # global active_player
    # active_player = your_score
    print('Your score: ')
    print(your_total_score)
    bot_total_score = score_board['bots_score']
    print('Bot\'s score: ')
    print(bot_total_score)
    for i in range(6):
        print(board[i])
    position_inputs()

def position_inputs():
    '''Initial game inputs to choose first move'''

    while GAME_IS_ON:
        try:
            row_input = input('Choose a letter from A-E for your position move in a row: ').upper()
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
            column_input = int(input('Choose a number from 1-9 for your position in a column: '))
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
    '''Check if got lines for score and count it'''

    # all_rows = board[1:6, :]
    # for one_row in all_rows:
    #     if 'o' not in one_row:
    #         score_board['your_score'] += np.count_nonzero(one_row)
    #         score_board['your_score'] -= 1 #it would not include letter at index 0
    #         # np.char.replace (one_row,  '@', '*')
    #         one_row[12] = 'o'
    #         print('row score:', score_board['your_score'])
    #         position_inputs()
    #         break
    

    #                                         # all_columns = board[1:6, 1:10]
    #                                         # for column in all_columns:
    # for one_column in board.T:
    #     if 'o' not in one_column:
    #         score_board['your_score'] += np.count_nonzero(one_column)
    #         score_board['your_score'] -= 1 #it would not include number at index 0
    #         # replace_for_column = np.char.replace (column,  '@', '*')
    #         # print(replace_for_column)
    #         one_column[len(one_column)-1] = 'o'
    #         print(one_column)
    #         print('column score:', score_board['your_score'])
    #         position_inputs()
    #         break
    # position_inputs()

    all_diagonals = [board.diagonal(-2),
                    board.diagonal(),
                    board.diagonal(2),
                    board.diagonal(4),
                    np.flipud(board).diagonal(0),
                    np.flipud(board).diagonal(2),
                    np.flipud(board).diagonal(4),
                    np.flipud(board).diagonal(6)]# -1

    for diagonal in all_diagonals:
        if 'o' not in diagonal:
            score_board['your_score'] += np.count_nonzero(diagonal)
            score_board['your_score'] -= 1 #it would not include number at index 0
            # replace_for_column = np.char.replace (diagonal,  '@', '*')
            # print(replace_for_column)
            print('diagonal score:', score_board['your_score'])
            break
    # print('Total score:', score_board['your_score'])
    position_inputs()

init_game()
