### AI Tic-Tac-Toe Game

Group Members : Bultez Charlotte, Ito-Russo Kana, Ribeiro Nell, Raux Lily

### 1. Project Overview

Our application is a Tic-Tac-Toe engine that uses a Minimax algorithm to simulate a full tree of game possibilities. The goal was to solve the problem of optimal decision-making in a zero-sum environment, creating an AI that evaluates every potential move to ensure it never loses. We built this to practice implementing recursive search patterns and to understand how heuristic functions can be used to score game states in real-time."

### 2. Quick Start

-How to run our projet ? 

The project was:
Developed and version-controlled using GitHub
Tested and executed in Jupyter Notebook
Written in Python 3

-Running in Jupyter 

Open Jupyter Notebook.
Open the .ipynb file or paste the Python code into a cell.
Run the cell containing the full script.
The Tkinter window will open automatically.


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

The algorithm simulates all possible future moves.

It assigns scores:

+1000 → AI wins

-1000 → Player wins

0 → Tie

The AI selects the move with the highest score.

- Difficulty Level :

Easy : Random move, Can lose easily
Medium : Minimax depth = 2, Makes decent moves
Difficult : Its often a Tie, impossible to win 

### 4.  Testing & Validation

- The project was tested by:

Verifying all win conditions:
Horizontal
Vertical
Diagonal

Testing again and again 


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
Choose the design of your player 
