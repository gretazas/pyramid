import numpy as np

#game_is_on = True
letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
row = int(input('Choose letter for your position move in a row: '))
column = int(input('choose number for your position in a column: '))

score_board = {'you': ['|', 'score: 0', '|'],
               'bot': ['|', 'score: 0', '|']}

board = np.array([['', 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['A', '|', '|', '', '', 'o', '|', '|', '|', '|'],
                  ['B', '|', '', '|', 'o', '', 'o', '|', '||', '|'],
                  ['C', '|', '', 'o', '', 'o', '', 'o', '|||', '|'],
                  ['D', '|', 'o', '', 'o', '', 'o', '', 'o', '|||'],
                  ['E', 'o', '', 'o', '', 'o', '', 'o', '', 'o'],
                  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']])

def print_board():
    """Print game board"""
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])

def position_choise(choise):
    """Valid posiotion choises"""

    if choise == '@':
        print('Already chosen, please try again.')
    elif choise == '' :
        print('Emply field, please try again.')
    else:
        board[row][column] = '@'
        print_board()
    

def print_game():
    """Print score board"""

    YOU = score_board['you']
    global active_player
    active_player = YOU
    print('Your score: ')
    print(YOU)
    BOT = score_board['bot']
    print('Bot\'s score: ')
    print(BOT)
    print_board()
    position = board[row][column]
    position_choise(position)

print_game()