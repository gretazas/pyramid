### Top 
<h1 style="text-align: center;"><strong>Pyramid Game</strong></h1>
<h2 style="text-align: center;"><strong>Welcome to the README PAGE of the Pyramid Game</strong></h2>

### Link to the Pyramid Game app:  

<a href="https://pyramid-lines.herokuapp.com/">https://pyramid-lines.herokuapp.com/</a>

### Link to the GitHub page with Pyramid Game:  

<a href="https://github.com/gretazas/pyramid">https://github.com/gretazas/pyramid</a>

<img src="" style="border:3git add .  px solid green" alt="">

# Acknowledgements

# **[Game instuctions](./game_intro.md)**

# Content

* [Built with intention to practice](#built-with-intention-to-practice)
* [User experience](#user-experience)
* [Buildpacks Used](#buildpacks-used)
* [Frameworks, Libraries & Programs I Used:](#built-with-intention-to-practise-use)
* [Proved By](#proved-by)
* [Features](#features) :
    * [Random](#random)
    * [Numpy](#numpy)
    * [Threading](#threading)
* [Future feature](#future-feature)
* [Deployment](#deployment)
    * [How To Fork A Repository](#how-to-fork-a-repository)
    * [How To Clone A Repository](#how-to-clone-a-repository)
    * [How To Make A Local Clone](#how-to-make-a-local-clone)
* [Testing](#testing)
* [Code](#code)
* [Issues and bugs](#issues-and-bugs)
* [Focus group](#focus-group)
* [Contact](#contact)

# Built with intention to practice

- Implement a given algorithm as a computer program
- Adapt and combine algorithms to solve a given problem
- Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)
- Explain what a given program does
- Identify and repair coding errors in a program
- Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software
- Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- Demonstrate and document the development process through a version control system such as GitHub
- Deploy a command-line application to a cloud-based platform

# User experience
# Buildpacks Used

- heroku/python
- heroku/nodejs

# Frameworks, Libraries & Programs I Used

- Random
- Numpy
- Threading

# Proved By

- <a href="http://pep8online.com/" target="_blank">PEP8: </a> no errors found

<p align="right">(<a href="#top">Back to top</a>)</p>

# Features

- First feature in this app is printed Welcome message
- First interactive feature in this app is to choose a level. Easy/ Hard
- Then the board is printed along with scores
- Then fallowed by making the move using inputs only if Player chose easy level
     - It is easy, because in this case Player starts and ends the game
     - It gives a chance to earn extra points
- Or Bot randomly choosing position on board if level is hard
    - It is hard because in this case Bot starts and ends the game.
    - Player must predict Bot's last moves in order to earn higher score
- Printed score update
- Printed inforamtion is maintainig with each score:<p style="font-size:12px;">(There could be multiple line score at the same time)</p>
    - In Rows
    - In Columns
    - In Diagonals
- Changing active players after each move
- Print at the end of game with accouncing message stating your win/loss


# Future feature

In the future i would like to add one more level of difficulty and add bots logic where it could see potentional in scoring more points with certain position moves.

<p align="right">(<a href="#top">Back to top</a>)</p>

# Deployment

This project was deployed using personal Heroku account.

Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the builtpacks to Python and NodeJS in the order
- Link the Heroku app to repository
- Click on **Deploy**

How to Fork a Repository:
1. Login or Sign Up to [GitHub](www.github.com).
2. On GitHub, go to [https://github.com/gretazas/pyramid](https://github.com/gretazas/pyramid)".
3. In the top right corner, click "Fork".

How to Clone a Repository:
1. Login in to [GitHub](www.github.com).
2. Fork the repository [https://github.com/gretazas/pyramid](https://github.com/gretazas/pyramid) using the steps above in [How To Fork a Repository](#HOW-TO-FORK-A-REPOSITORY).
3. Above the file list, click "Code".
4. Choose if you want to close using HTTPS, SSH or GitHub CLI, then click the copy button to the right.
5. Open Git Bash.
6. Change the directory to where you want your clone to go.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter to create your clone.

How to make a Local Clone:
1. Login in to [GitHub](www.github.com).
2. Under the repository name, above the list of files, click "Code".
3. Here you can either Clone or Download the repository.
4. You should close the repository using HTTPS, clicking on the icon to copy the link.
5. Open Git Bash.
6. Change the current working directory to the new location, where you want the cloned directory to be.
7. Type git clone and then paste the URL you copied in step 4.
8. Press Enter, and your local clone will be created.

The site was deployed to Github pages using the following steps:
* In the Github repository, navigate to the settings tab.
* Scroll down and select Pages from the left side navigation menu to open Github pages.
* In the Source section, click on the dropdown menu and select the Master branch.
* Once the Master branch is selected the page will refresh to display a message stating "Your site is published at 

<p align="right">(<a href="#top">Back to top</a>)</p>

# Testing

I have manually tested this project by doing the fallowing:
- Passed the code through a PEP8 linter and comfirmed there are no problems
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Heroku terminal.

# Code

* All code was written by myself and was learnt from [www.codeinstitute.net](https://www.codeinstitute.net) and [w3schools.com](https://www.w3schools.com/).
* Inspiration for project came from my mom who passed away half year ago. R.I.P.

# Issues and bugs


<p align="right">(<a href="#top">Back to top</a>)</p>

# Focus Group

* I'd like to thank the following people for the help they gave me with this project:
  - My daughter Madelyne for helping me with README.md page and checking the game function.<br>
  - John, Alex and Gemma from Code Institute Tutor Assistance.<br>
  - Help from Slack: ...........................
  - Mentor Anthony.
  <img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" width="90">
  
 
# Contact 

![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white) https://github.com/gretazas<br>
Greta Baliunaite: [ https://www.facebook.com/greta.baliunaite]( https://www.facebook.com/greta.baliunaite)

<br>
<br>

![Safe](https://img.shields.io/badge/Stay-Safe-red?logo=data:image/svg%2bxml;base64,PHN2ZyBpZD0iTGF5ZXJfMSIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEwIDUxMCIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCA1MTAgNTEwIiB3aWR0aD0iNTEyIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnPjxnPjxwYXRoIGQ9Im0xNzQuNjEgMzAwYy0yMC41OCAwLTQwLjU2IDYuOTUtNTYuNjkgMTkuNzJsLTExMC4wOSA4NS43OTd2MTA0LjQ4M2g1My41MjlsNzYuNDcxLTY1aDEyNi44MnYtMTQ1eiIgZmlsbD0iI2ZmZGRjZSIvPjwvZz48cGF0aCBkPSJtNTAyLjE3IDI4NC43MmMwIDguOTUtMy42IDE3Ljg5LTEwLjc4IDI0LjQ2bC0xNDguNTYgMTM1LjgyaC03OC4xOHYtODVoNjguMThsMTE0LjM0LTEwMC4yMWMxMi44Mi0xMS4yMyAzMi4wNi0xMC45MiA0NC41LjczIDcgNi41NSAxMC41IDE1LjM4IDEwLjUgMjQuMnoiIGZpbGw9IiNmZmNjYmQiLz48cGF0aCBkPSJtMzMyLjgzIDM0OS42M3YxMC4zN2gtNjguMTh2LTYwaDE4LjU1YzI3LjQxIDAgNDkuNjMgMjIuMjIgNDkuNjMgNDkuNjN6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTM5OS44IDc3LjN2OC4wMWMwIDIwLjY1LTguMDQgNDAuMDctMjIuNjQgNTQuNjdsLTExMi41MSAxMTIuNTF2LTIyNi42NmwzLjE4LTMuMTljMTQuNi0xNC42IDM0LjAyLTIyLjY0IDU0LjY3LTIyLjY0IDQyLjYyIDAgNzcuMyAzNC42OCA3Ny4zIDc3LjN6IiBmaWxsPSIjZDAwMDUwIi8+PHBhdGggZD0ibTI2NC42NSAyNS44M3YyMjYuNjZsLTExMi41MS0xMTIuNTFjLTE0LjYtMTQuNi0yMi42NC0zNC4wMi0yMi42NC01NC42N3YtOC4wMWMwLTQyLjYyIDM0LjY4LTc3LjMgNzcuMy03Ny4zIDIwLjY1IDAgNDAuMDYgOC4wNCA1NC42NiAyMi42NHoiIGZpbGw9IiNmZjRhNGEiLz48cGF0aCBkPSJtMjEyLjgzIDM2MC4xMnYzMGg1MS44MnYtMzB6IiBmaWxsPSIjZmZjY2JkIi8+PHBhdGggZD0ibTI2NC42NSAzNjAuMTJ2MzBoMzYuMTRsMzIuMDQtMzB6IiBmaWxsPSIjZmZiZGE5Ii8+PC9nPjwvc3ZnPg==)

<p align="right">(<a href="#top">Back to top</a>)</p>
