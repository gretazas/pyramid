'''Numpy will help me to navigate through the rows and columns'''
import numpy as np

score_board = {'your_score': 0,
               'bots_score': 0}

board = np.array([['','','','','','','','','','','','','','','','',''],
                  ['o','','','', 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '.', '.','.'],
                  ['','','','A', '', '', '', '', 'o', '', '', '', '', '', '', '',''],
                  ['','','','B', '', '', '', 'o', '', 'o', '', '', '', '', '', '',''],
                  ['','','','C', '', '', 'o', '', 'o', '', 'o', '', '', '', '', '',''],
                  ['','','','D', '', 'o', '', 'o', '', 'o', '', 'o', '', '', '', '',''],
                  ['','','','E', 'o', '', 'o', '', 'o', '', 'o', '', 'o', '', '', '',''],
                  ['','','','','','','','','','','','','','','','','']])

GAME_IS_ON = True

def init_game():
    """Print score board game initialization"""

    your_total_score = score_board['your_score']
    # global active_player
    # active_player = your_score
    print('Your score: ')
    print(your_total_score)
    bot_total_score = score_board['bots_score']
    print('Bot\'s score: ')
    print(bot_total_score)
    print(board[1:7,3:13])
    position_inputs()

def position_inputs():
    '''Initial game inputs to choose first move'''

    while GAME_IS_ON:
        try:
            row_input = input('Choose a letter from A-E for your position move in a row: ').upper()
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
            column_input = int(input('Choose a number from 1-9 for your position in a column: '))
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
        if 'o' in board[1:7,3:13]:
            for i in range(0, 8):
                print(board[i])
        else:
            for i in range(0, 8):
                print(board[i])
            decide_winner()

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

    if 'o' not in board.diagonal():
        score_board['your_score'] += 2
        board[0][0] = 'o'
        # replace_for_column = np.char.replace (diagonal,  '@', '*')
        # print(replace_for_column)
        # print('Total score:', score_board['your_score'])
    if 'o' not in board.diagonal(2):
        score_board['your_score'] += 3
        board[0][2] = 'o'
    if 'o' not in board.diagonal(4):
        score_board['your_score'] += 4
        board[0][4] = 'o'
    if 'o' not in board.diagonal(6):
        score_board['your_score'] += 5
        board[0][6] = 'o'
    if 'o' not in np.flipud(board).diagonal(3):
        score_board['your_score'] += 5
        board[0][10] = 'o'
    if 'o' not in np.flipud(board).diagonal(5):
        score_board['your_score'] += 4
        board[0][12] = 'o'
    if 'o' not in np.flipud(board).diagonal(7):
        score_board['your_score'] += 3
        board[0][14] = 'o'
    if 'o' not in np.flipud(board).diagonal(9):
        score_board['your_score'] += 2
        board[0][16] = 'o'

    print('Your score:', score_board['your_score'])
    position_inputs()
    
def decide_winner():
    '''Decide who won'''
    if score_board['your_score'] > score_board['bots_score']:
        print('Congradulations! You are the winner!')
    elif score_board['your_score'] < score_board['bots_score']:
        print('You lost! Sorry.')
    else:
        print('It\'s a draw.')


init_game()
