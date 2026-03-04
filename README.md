### AI Tic-Tac-Toe Game

Group Members : Bultez Charlotte, Ito-Russo Kana, Ribeiro Nell, Raux Lily

### 1. Project Overview

Our application is a Tic-Tac-Toe engine that uses a Minimax algorithm to simulate a full tree of game possibilities. The goal was to solve the problem of optimal decision-making in a zero-sum environment, creating an AI that evaluates every potential move to ensure it never loses. We built this to practice implementing recursive search patterns and to understand how heuristic functions can be used to score game states in real-time."
The application also includes multiple game modes (Player vs Player and Player vs AI), difficulty levels, and symbol customization to enhance user experience.

### 2. Quick Start

-How to run our projet ? 

The project was:
Developed and version-controlled using GitHub
Tested and executed in Jupyter Notebook
Written in Python 3
No additional installation is required since the project only uses standard Python libraries.

-Running in Jupyter 

Open Jupyter Notebook.
Open the .ipynb file or paste the Python code into a cell.
Run the cell containing the full script.
The Tkinter window will open automatically.
Make sure Tkinter is installed (it is included by default in most Python distributions).


### 3. Technical Architecture

The board is implemented as a 3×3 list:

self.board = [["" for _ in range(3)] for _ in range(3)]

- Each cell contains:

"X" → Human player

"O" → AI or second player

"" → Empty cell

- The function check_winner(board):

Checks rows
Checks columns
Checks diagonals
Detects tie situations

- Returns:

"X" if player X wins

"O" if player O wins

"TIE" if board is full

None if the game continues

- The AI uses a recursive Minimax algorithm:

minimax(board, depth, is_max)

- Logic:

The AI ("O") is the maximizing player.

The human ("X") is the minimizing player.

In Hard mode, the algorithm explores the full game tree.
In Medium mode, the depth is limited to reduce computation and make the AI beatable.

It assigns scores:

+1000 → AI wins

-1000 → Player wins

0 → Tie

The AI selects the move with the highest score.

- Difficulty Level :

Easy : Random move, Can lose easily
Medium : Minimax depth = 2, Makes decent moves
Difficult : Its often a Tie, impossible to win 

You can choose the design of your player, cant have the same ( error message : "Players must choose different symbols") 

- Game Modes : 

Player vs Player (PVP)

Player vs AI

The application manages screen navigation using multiple Tkinter frames (menu, difficulty selection, symbol customization, game board).

### 4.  Testing & Validation

- The project was tested by:

Verifying all win conditions:
Horizontal
Vertical
Diagonal

Testing all difficulty levels

Testing symbol customization constraints

Verifying that the AI never loses in Hard mode


### 5. Dependencies

The project only uses standard Python libraries:

tkinter

random

math

No external libraries are required.

### 6. Future Roadmap

- Possible enhancements:

Improve the design 
Add an online mode 
Implement a web version 
