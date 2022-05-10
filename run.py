import numpy as np

# Display board and score board

score_board = {'you': ['|', 'score: 0', '|'],
               'bot': ['|', 'score: 0', '|']}

board = np.array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  ['A', '', '', '', '', 'o', '', '', '', ''],
                  ['B', '', '', '', 'o', '', 'o', '', '', ''],
                  ['C', '', '', 'o', '', 'o', '', 'o', '', ''],
                  ['D', '', 'o', '', 'o', '', 'o', '', 'o', ''],
                  ['E', 'o', '', 'o', '', 'o', '', 'o', '', 'o']])

game_is_on = True

letters_to_numbers = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

def print_board():
    You = score_board['you']
    print('Your score: ')
    print(You)
    Bot = score_board['bot']
    print('Bot\'s score: ')
    print(Bot)
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    

print_board()