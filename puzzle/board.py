SOLVED = list(range(1,16)) + [0]

class Board:
    def __init__(self):
        self.tiles = list(SOLVED)

    def is_solved(self):
        return self.tiles == SOLVED

    
board = Board()
print(board.is_solved())

