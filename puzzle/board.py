import random
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

        index_blank= self.find_blank()
        row_blank = index_blank //4
        column_blank = index_blank % 4

        if (row == row_blank)and(abs(column-column_blank)==1):
            return True
        elif (column == column_blank)and(abs(row-row_blank)==1):
            return True
        else : 
            return False

    def move(self, index):
        index_blank = self.find_blank()
        if self.is_adjacent(index):
            self.tiles[index], self.tiles[index_blank] = self.tiles[index_blank], self.tiles[index]
            return True
        else :
            return False

    def shuffle(self, moves=200):
        count = 0
        index_former_blank = None
        while count < moves:
            index_blank = self.find_blank()
            index_move = random.randint(0, 15)
            if index_move == index_former_blank:
                continue
            if self.move(index_move):
                index_former_blank = index_blank
                count += 1        


    def neighbors(self):
        boards_available = []
        index_blank = self.find_blank()
        for i in range(16):
            if not self.is_adjacent(i):
                continue

            tiles_copy = list(self.tiles)
            tiles_copy[i], tiles_copy[index_blank] = tiles_copy[index_blank], tiles_copy[i]

            boards_available.append([i,tuple(tiles_copy)])

        return boards_available

board = Board()
print(board.neighbors())
print(board.tiles)