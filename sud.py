import tkinter as tk
from tkinter import messagebox

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # Solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def is_valid(board, num, pos):
    row, col = pos


    if num in board[row]:
        return False


    for i in range(9):
        if board[i][col] == num:
            return False


    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit() and 1 <= int(value) <= 9:
                row.append(int(value))
            elif value == "":
                row.append(0)
            else:
                messagebox.showwarning("Неверный ввод", f"В ячейке ({i + 1}, {j + 1}) должно быть число от 1 до 9.")
                return None
        board.append(row)


    return board


def solve():
    board = get_board()
    if board is None:
        return
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    entries[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("Решить", "Решения нет:).")


def show_solver():
    start_frame.pack_forget()
    solver_frame.pack()


def show_instructions():
    messagebox.showinfo("Инструкция",
                        "Введите цифру от 1 до 9 в клетку. В случае неккоректного ввода выведется два числа. Назовем их (a, b), где a - номер ряда, b - номер ячейки.  Нажмите 'Решить', чтобы найти решение.")


def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    if dark_theme:
        root.config(bg='black')
        start_frame.config(bg="black")
        start_label.config(bg="black", fg="white")
        for entry in entries_flat:
            entry.config(bg='black', fg='white')
        solve_button.config(bg='black', fg='white')
        solver_frame.config(bg='black')

        solve_button.bind("<Enter>", lambda e: solve_button.config(bg='white', fg='black'))
        solve_button.bind("<Leave>", lambda e: solve_button.config(bg='black', fg='white'))
    else:
        root.config(bg='white')
        start_frame.config(bg="white")
        start_label.config(bg="white", fg="black")
        for entry in entries_flat:
            entry.config(bg='white', fg='black')
        solve_button.config(bg='white', fg='black')


def clear_all():
    for entry in entries_flat:
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("saentsstress")


start_frame = tk.Frame(root)
start_frame.pack(pady=40)

start_label = tk.Label(start_frame, text="Добро пожаловать в Судоку Решатель",
                       font=('Arial', 36))
start_label.pack(pady=20)
solve_button_start = tk.Button(start_frame, text="Перейти в режим решения", command=show_solver, font=('Arial', 18),
                               width=30)
solve_button_start.pack(pady=10)



instructions_button = tk.Button(start_frame, text="Инструкция", command=show_instructions, font=('Arial', 18),
                                width=30)
instructions_button.pack(pady=10)

settings_button = tk.Button(start_frame, text="🌕 / ☀️", command=toggle_theme, font=('Arial', 18),
                            width=30)
settings_button.pack(pady=10)


solver_frame = tk.Frame(root)


frames = [[None for _ in range(3)] for _ in range(3)]
entries = [[None for _ in range(9)] for _ in range(9)]
entries_flat = []

for box_row in range(3):
    for box_col in range(3):
        frame = tk.Frame(solver_frame, bd=2, relief='solid')
        frame.grid(row=box_row, column=box_col, padx=2, pady=2)
        frames[box_row][box_col] = frame


        for i in range(3):
            for j in range(3):
                row = box_row * 3 + i
                col = box_col * 3 + j
                entry = tk.Entry(frame, width=3, font=('Arial', 24), justify='center')
                entry.grid(row=i, column=j, padx=1, pady=1)
                entries[row][col] = entry
                entries_flat.append(entry)

solve_button = tk.Button(solver_frame, text="Решить", command=solve, font=('Arial', 18),
                         width=30)
solve_button.grid(row=3, column=0, columnspan=3, pady=20)

clear_button = tk.Button(solver_frame, text="Очистить", command=clear_all, font=('Arial', 18),
                         width=30)
clear_button.grid(row=4, column=0, columnspan=3)
dark_theme = False

root.mainloop()