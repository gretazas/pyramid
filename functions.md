First called function is choose_level()

<img width="400" height="250" src="./assets/images/def_images/level.png" alt="function">

After we need to check if the data is valid

<img width="350" height="150" src="./assets/images/def_images/level_validation.png" alt="function">

When the level is chosen, need to decide who will begin the game. 
- For E(easy) the Player starts the game 
- For H(hard) the Bot starts the game

<img width="350" height="150" src="./assets/images/def_images/level_is_chosen.png" alt="function">

- For E(easy) the Player starts the game and brings us to position_inputs()
- For H(hard) the Bot starts the game and brings us to bot_position_choose()

<img width="350" height="150" src="./assets/images/def_images/init_game.png" alt="function">

The next picture shows that the Player must choose a position on the board to make a move

<img width="400" height="350" src="./assets/images/def_images/position_inputs.png" alt="function">

The Bot chooses a random position, by running positions with the condition to get 'o' in it

<img width="350" height="200" src="./assets/images/def_images/bot_position.png" alt="function">

Then we check if we got any lines to score points.<br>
We must run all functions together before continuing the game so I use threading.

<img width="350" height="200" src="./assets/images/def_images/check_lines.png" alt="function">

Those functions in the function check_for_lines() are:
- def while_rows()
    Here I just run for loop to get each row filled fully with '@'s, making a line to count the score.
    Function np.count_nonzero(one_row) is very handy here to count all '@'s in the line.
- def while_columns()
    The same situation with the columns np.count_nonzero(one_column).
- def while_diagonals()
    With diagonals I found it tricky, so decided to treat each diagonal individually

<img width="350" height="200" src="./assets/images/def_images/rows.png" alt="function">
<img width="350" height="200" src="./assets/images/def_images/columns.png" alt="function">
<img width="350" height="200" src="./assets/images/def_images/diagonals.png" alt="function">

The next function would be check_game_is_on() before continuing need to check if there are any empty positions, if not- announce win/loss/draw

<img width="330" height="150" src="./assets/images/def_images/game_on.png" alt="function">

print_board()

<img width="330" height="150" src="./assets/images/def_images/print_board.png" alt="function">

Change active player 

<img width="300" height="150" src="./assets/images/def_images/act_player.png" alt="function">

And the last function would be decide winn/loss/draw def decide_winner()

<img width="300" height="150" src="./assets/images/def_images/decide_winner.png" alt="function">
