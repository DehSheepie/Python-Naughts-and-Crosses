from tkinter import *


class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Naughts and Crosses")
        self.x_turn = False
        self.label = Label(self.window, text="Naught's Turn")
        self.label.grid(row=10, column=1)
        self.buttons = []
        self.turns = 0
        self.setup()
        self.end_game_string = ""
        self.menu = Menu(self.window)
        self.menu.add_command(label="Restart", command=self.restart)
        self.window.config(menu=self.menu)
        self.window.mainloop()

    def run_check(self, li: list):
        string = ""
        for space in li:
            string += self.buttons[space[0]][space[1]]['text']
        print(string)
        if string == "XXX" or string == "OOO":
            self.end_game_string = string
            return True
        return False

    def check_win(self):
        rows = [[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]]
        columns = [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]]
        diagonal1 = [[0, 0], [1, 1], [2, 2]]
        diagonal2 = [[0, 2], [1, 1], [2, 0]]

        if (self.run_check(rows[0])) or (self.run_check(rows[1])) or (self.run_check(rows[2])) \
                or (self.run_check(columns[0])) or (self.run_check(columns[1])) or (self.run_check(columns[2])) or \
                (self.run_check(diagonal1)) or (self.run_check(diagonal2)):
            # self.label["text"] = "Game over. Restart?"
            if self.end_game_string == "XXX":
                self.label["text"] = "Nice one Crosses! Restart?"
            if self.end_game_string == "OOO":
                self.label["text"] = "Noice Naughts! Restart?"

            for row in self.buttons:
                for col in row:
                    col.bind("<Button-1>", self.restart)
            self.label.bind("<Button-1>", self.restart)

    def click(self, row, col):
        if self.buttons[row][col]["text"] == "-":
            self.turns += 1  # Only increments the turn if the space is valid
            self.buttons[row][col]["text"] = "X" if self.x_turn is True else "O"
            self.x_turn = not self.x_turn
            self.label["text"] = "Crosses' turn." if self.x_turn else "Naught's turn."
        else:
            self.label["text"] = "Invalid space."

        self.check_win()

        if self.turns >= 9:
            self.label["text"] = "A Draw! Restart?"
            self.label.bind("<Button-1>", self.restart)

    def setup(self):
        row = 0
        col = 0
        while row < 3:
            col = 0
            row_values = []
            while col < 3:
                # Could not pass in the button as only the last entered values were used
                # Had to assign r and c to row and col otherwise the values of row and col at the end of the loop were used
                b = Button(self.window, text="-", bg="Grey", height=10, width=20,
                           command=lambda r=row, c=col: self.click(r, c))
                b.grid(column=col, row=row)
                row_values.append(b)
                col += 1
            self.buttons.append(row_values)
            row += 1

    def restart(self, event=None):
        for row in self.buttons:
            for col in row:
                col.unbind("<Button-1>")
                col["text"] = "-"
        self.label.unbind("<Button-1>")
        self.label["text"] = "Crosses' turn." if self.x_turn else "Naught's turn."
        self.turns = 0


game = Game()
