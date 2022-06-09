First called function is choose_level()

<img width="400" height="250" src="./assets/images/def_images/level.png" alt="function">

After we need to check if data is valid

<img width="350" height="150" src="./assets/images/def_images/level_validation.png" alt="function">

When level is chosen, need to decide who will begin the game. 
- For E(easy) the Player starts the game 
- For H(hard) the Bot starts the game

<img width="350" height="150" src="./assets/images/def_images/level_is_chosen.png" alt="function">

- For E(easy) the Player starts the game and brings us to position_inputs()
- For H(hard) the Bot starts the game and brings us to bot_position_choose()

<img width="350" height="150" src="./assets/images/def_images/init_game.png" alt="function">

Next picture shows that the Player must choose a position in the board to make a move

<img width="350" height="150" src="./assets/images/def_images/position_inputs.png" alt="function">

The Bot chooses random position, by running positions with condition to get 'o' in it

<img width="350" height="150" src="./assets/images/def_images/bot_position.png" alt="function">

Then we check if we got any lines to score points.<br>
We must run all functions together before continuing the game so we use threading

<img width="350" height="150" src="./assets/images/def_images/check_lines.png" alt="function">