from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Naughts and Crosses")
x_turn = False

label = Label(window, text="Naught's Turn")
label.grid(row=10, column=1)
buttons = []


def click(row, col):
    global x_turn
    global label
    if buttons[row][col]["text"] == "-":
        label["text"] = "Space chosen."
        buttons[row][col]["text"] = "X" if x_turn is True else "O"
        x_turn = not x_turn
    else:
        label["text"] = "Invalid space."


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
