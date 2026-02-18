import tkinter as tk
from tkinter import messagebox
import math

# --- LOGIQUE MINIMAX (Extraite du document PBL) ---
def check_winner(board):
    lines = board + [list(x) for x in zip(*board)]
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])
    for line in lines:
        if all(c == "O" for c in line): return "O"
        if all(c == "X" for c in line): return "X"
    if all(c != "" for row in board for c in row): return "TIE"
    return None

def evaluate(board):
    winner = check_winner(board)
    if winner == "O": return 1000
    if winner == "X": return -1000
    if winner == "TIE": return 0
    # Score basé sur les pions alignés (p.8 du document)
    return 0 # (Simplifié ici pour la clarté, voir code précédent pour détails)

def minimax(board, depth, is_max):
    res = check_winner(board)
    if res or depth == 0: return evaluate(board)
    scores = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == "":
                board[r][c] = "O" if is_max else "X"
                scores.append(minimax(board, depth - 1, not is_max))
                board[r][c] = ""
    return max(scores) if is_max else min(scores)

# --- INTERFACE GRAPHIQUE ---
class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Morpion IA")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                                              command=lambda r=r, c=c: self.play(r, c))
                self.buttons[r][c].grid(row=r, column=c)
        self.root.mainloop()

    def play(self, r, c):
        if self.board[r][c] == "":
            self.board[r][c] = "X"
            self.buttons[r][c].config(text="X", state="disabled")
            if not check_winner(self.board):
                self.ai_move()
            self.check_end()

    def ai_move(self):
        best_score = -float('inf')
        move = None
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "":
                    self.board[r][c] = "O"
                    score = minimax(self.board, 3, False)
                    self.board[r][c] = ""
                    if score > best_score:
                        best_score = score
                        move = (r, c)
        if move:
            self.board[move[0]][move[1]] = "O"
            self.buttons[move[0]][move[1]].config(text="O", state="disabled")

    def check_end(self):
        w = check_winner(self.board)
        if w:
            messagebox.showinfo("Fin", "Gagnant : " + w)
            self.root.destroy()

if __name__ == "__main__":
    TicTacToe()
  
