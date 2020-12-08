from view.token_piece import TokenPiece


class Grid:
    def __init__(self, rows: int, columns: int):
        self.__rows = rows
        self.__columns = columns

        self.__token_positions = []
        for row in range(0, rows):
            self.__token_positions.append([None] * self.__columns)

    def __str__(self) -> str:
        """
        Naive implementation of printing a grid. I'm sure there
        is a cleaner more pythonic way of doing this.
        :return: string representing a printed grid with columns and rows.
        """
        grid = " "
        for i in range(self.__columns):
            grid += " " * 5 + str(i) + " " * 5
        grid += "\n"

        for row in range(self.__rows):
            grid += "  "
            grid += ("+" + "- " * 5) * self.__columns + "+\n"
            for line in range(3):
                if line == 1:
                    wild = str(row) + " "
                else:
                    wild = "  "
                grid += wild
                column_decrement = self.__columns
                for column in range(self.__columns):
                    grid += "|" + self.check_for_tokens(
                        row, self.__columns - column_decrement, line
                    )
                    column_decrement -= 1
                grid += "|\n"
        grid += "  "
        grid += ("+" + "- " * 5) * self.__columns + "+"
        return grid

    def check_for_tokens(self, row: int, column: int, line: int) -> str:
        token_found = self.__token_positions[row][column]
        if token_found is None:
            return "  " * 5
        else:
            return token_found.draw_token(line)

    def add_token_position(self, token: TokenPiece, row: int, column: int):
        self.__token_positions[row].pop(column)
        self.__token_positions[row].insert(column, token)

    def check_if_position_available(self, row: int, column: int) -> bool:
        if row is None or column is None:
            return False
        token_found = self.__token_positions[row][column]
        if token_found is None:
            return True
        else:
            print("That place is taken already!")
            return False

    def is_full(self):
        if any(None in row for row in self.__token_positions):
            return False
        else:
            print("Grid is full! No winners! :(")
            return True

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    @property
    def token_positions(self):
        return self.__token_positions
