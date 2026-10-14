SOLVED = list(range(1,16)) + [0]

class Board:
    def __init__(self):
        self.tiles = list(SOLVED)

    def is_solved(self):
        return self.tiles == SOLVED

    def find_blank(self):
        return self.tiles.index(0)
    
board = Board()
board.tiles[4],  board.tiles[15]= board.tiles[15],  board.tiles[4]
print(board.find_blank())

