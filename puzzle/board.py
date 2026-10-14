SOLVED = list(range(1,16)) + [0]

class Board:
    def __init__(self):
        self.tiles = list(SOLVED)

    def is_solved(self):
        return self.tiles == SOLVED

    def find_blank(self):
        return self.tiles.index(0)

    def is_adjacent(self, index):
        row = index // 4
        column = index % 4

        blank_index= self.find_blank()
        row_blank = blank_index //4
        column_blank = blank_index % 4

        if(row == row_blank)and(abs(column-column_blank)==1):
            return True
        elif(column == column_blank)and(abs(row-row_blank)==1):
            return True
        else: 
            return False
    
board = Board()
print((board.is_adjacent(14)))


