from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Naughts and Crosses")
x_turn = False

label = Label(window, text="Naught's Turn")
label.grid(row=10, column=1)
buttons = []
turns = 0


def run_check(li: list):
    string = ""
    for space in li:
        string += buttons[space[0]][space[1]]['text']
    print(string)
    if string is "XXX" or "OOO":
        return True
    return False


def check_win():
    rows = [[0, 0], [0, 1], [0, 2]]
    columns = [[0, 0], [1, 0], [2, 0]]
    diagonal1 = [[0, 0], [1, 1], [2, 2]]
    diagonal2 = [[0, 2], [1, 1], [2, 0]]

    if run_check(rows) or run_check(columns) or run_check(diagonal1) or run_check(diagonal2) is True:
        label["text"] = "Game over. Restart?"
        label.bind("<Button-1>", restart)


def click(row, col):
    global x_turn
    global label
    global turns

    if buttons[row][col]["text"] == "-":
        turns += 1  # Only increments the turn if the space is valid
        buttons[row][col]["text"] = "X" if x_turn is True else "O"
        x_turn = not x_turn
        label["text"] = "Crosses' turn." if x_turn else "Naught's turn."
    else:
        label["text"] = "Invalid space."

    check_win()

    if turns >= 9:
        label["text"] = "Game over. Restart?"
        label.bind("<Button-1>", restart)


def restart(event):
    for row in buttons:
        for col in row:
            col["text"] = "-"
    label.unbind("<Button-1>")
    label["text"] = "Crosses' turn." if x_turn else "Naught's turn."


def setup():
    row = 0
    col = 0
    while row < 3:
        col = 0
        row_values = []
        while col < 3:
            # Could not pass in the button as only the last entered values were used
            # Had to assign r and c to row and col otherwise the values of row and col at the end of the loop were used
            b = Button(window, text="-", bg="Grey", height=10, width=20, command=lambda r=row, c=col: click(r, c))
            b.grid(column=col, row=row)
            row_values.append(b)
            col += 1
        buttons.append(row_values)
        row += 1


setup()
window.mainloop()
