import tkinter as tk
from tkinter import messagebox
import random
import math


def check_winner(board):
    lines = board + [list(x) for x in zip(*board)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if all(c == "O" for c in line):
            return "O"
        if all(c == "X" for c in line):
            return "X"

    if all(c != "" for row in board for c in row):
        return "TIE"

    return None


def evaluate(board):
    winner = check_winner(board)
    if winner == "O":
        return 1000
    if winner == "X":
        return -1000
    if winner == "TIE":
        return 0
    return 0


def minimax(board, depth, is_max):
    result = check_winner(board)

    if result is not None or depth == 0:
        return evaluate(board)

    if is_max:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "O"
                    score = minimax(board, depth - 1, False)
                    board[r][c] = ""
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == "":
                    board[r][c] = "X"
                    score = minimax(board, depth - 1, True)
                    board[r][c] = ""
                    best = min(best, score)
        return best



class TicTacToe:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.mode = None
        self.difficulty = None
        self.current_player = "X"

        self.symbols = {"X": "❌", "O": "⭕"}

        self.create_frames()
        self.show_frame(self.menu_frame)

        self.root.mainloop()


    def create_frames(self):
        self.menu_frame = tk.Frame(self.root)
        self.difficulty_frame = tk.Frame(self.root)
        self.symbol_frame = tk.Frame(self.root)
        self.game_frame = tk.Frame(self.root)

        self.create_menu_screen()
        self.create_difficulty_screen()
        self.create_symbol_screen()
        self.create_game_screen()

    def show_frame(self, frame):
        for f in [self.menu_frame, self.difficulty_frame,
                  self.symbol_frame, self.game_frame]:
            f.pack_forget()
        frame.pack(expand=True)


    def create_menu_screen(self):
        tk.Label(self.menu_frame, text="Tic Tac Toe",
                 font=("Arial", 24)).pack(pady=50)

        tk.Button(self.menu_frame, text="Player vs Player",
                  width=20, height=2,
                  command=self.start_pvp).pack(pady=10)

        tk.Button(self.menu_frame, text="Player vs AI",
                  width=20, height=2,
                  command=self.go_to_difficulty).pack(pady=10)

    def start_pvp(self):
        self.mode = "PVP"
        self.show_frame(self.symbol_frame)

    def go_to_difficulty(self):
        self.mode = "AI"
        self.show_frame(self.difficulty_frame)


    def create_difficulty_screen(self):
        tk.Label(self.difficulty_frame,
                 text="Select Difficulty",
                 font=("Arial", 20)).pack(pady=40)

        tk.Button(self.difficulty_frame, text="Easy",
                  width=20, height=2,
                  command=lambda: self.set_difficulty("Easy")).pack(pady=10)

        tk.Button(self.difficulty_frame, text="Medium",
                  width=20, height=2,
                  command=lambda: self.set_difficulty("Medium")).pack(pady=10)

        tk.Button(self.difficulty_frame, text="Hard",
                  width=20, height=2,
                  command=lambda: self.set_difficulty("Hard")).pack(pady=10)

        tk.Button(self.difficulty_frame, text="Back",
                  command=lambda: self.show_frame(self.menu_frame)).pack(pady=20)

    def set_difficulty(self, level):
        self.difficulty = level
        self.show_frame(self.symbol_frame)


    def create_symbol_screen(self):

        tk.Label(self.symbol_frame,
                 text="Choose Player Symbols",
                 font=("Arial", 20)).pack(pady=20)

        self.available_symbols = ["❌", "⭕", "❤️", "⭐", "🔵", "🔺"]

        self.player1_symbol = tk.StringVar(value=self.available_symbols[0])
        self.player2_symbol = tk.StringVar(value=self.available_symbols[1])

        tk.Label(self.symbol_frame, text="Player 1 Symbol").pack()
        tk.OptionMenu(self.symbol_frame,
                      self.player1_symbol,
                      *self.available_symbols).pack(pady=5)

        tk.Label(self.symbol_frame, text="Player 2 / AI Symbol").pack()
        tk.OptionMenu(self.symbol_frame,
                      self.player2_symbol,
                      *self.available_symbols).pack(pady=5)

        tk.Button(self.symbol_frame,
                  text="Start Game",
                  command=self.set_symbols).pack(pady=15)

        tk.Button(self.symbol_frame,
                  text="Back",
                  command=self.go_back_symbols).pack()

    def go_back_symbols(self):
        if self.mode == "AI":
            self.show_frame(self.difficulty_frame)
        else:
            self.show_frame(self.menu_frame)

    def set_symbols(self):
        if self.player1_symbol.get() == self.player2_symbol.get():
            messagebox.showerror("Error",
                                 "Players must choose different symbols!")
            return

        self.symbols = {
            "X": self.player1_symbol.get(),
            "O": self.player2_symbol.get()
        }

        self.start_game()


    def create_game_screen(self):
        self.board_frame = tk.Frame(self.game_frame)
        self.board_frame.pack(pady=20)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.board_frame,
                                text="",
                                font=("Arial", 28),
                                width=4,
                                height=2,
                                command=lambda r=r, c=c: self.play(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

        tk.Button(self.game_frame, text="Restart",
                  command=self.reset_game).pack(pady=5)

        tk.Button(self.game_frame, text="Main Menu",
                  command=lambda: self.show_frame(self.menu_frame)).pack()

    def start_game(self):
        self.reset_game()
        self.show_frame(self.game_frame)


    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text="", state="normal")

    def play(self, r, c):
        if self.board[r][c] != "":
            return

        self.board[r][c] = self.current_player
        self.buttons[r][c].config(
            text=self.symbols[self.current_player])

        winner = check_winner(self.board)
        if winner:
            self.end_game(winner)
            return

        if self.mode == "AI":
            if self.current_player == "X":
                self.current_player = "O"
                self.root.after(300, self.ai_move)
        else:
            self.current_player = "O" if self.current_player == "X" else "X"


    def ai_move(self):
        if self.difficulty == "Easy":
            self.random_move()
        elif self.difficulty == "Medium":
            self.best_move(depth=2)
        else:
            self.best_move(depth=9)

        winner = check_winner(self.board)
        if winner:
            self.end_game(winner)
            return

        self.current_player = "X"

    def random_move(self):
        empty = [(r, c) for r in range(3)
                 for c in range(3) if self.board[r][c] == ""]
        if empty:
            r, c = random.choice(empty)
            self.board[r][c] = "O"
            self.buttons[r][c].config(
                text=self.symbols["O"])

    def best_move(self, depth):
        best_score = -math.inf
        move = None

        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    self.board[r][c] = "O"
                    score = minimax(self.board, depth, False)
                    self.board[r][c] = ""
                    if score > best_score:
                        best_score = score
                        move = (r, c)

        if move:
            r, c = move
            self.board[r][c] = "O"
            self.buttons[r][c].config(
                text=self.symbols["O"])


    def end_game(self, winner):
        if winner == "TIE":
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            messagebox.showinfo("Game Over",
                                f"{self.symbols[winner]} Wins!")
        self.reset_game()


if __name__ == "__main__":
    TicTacToe()
