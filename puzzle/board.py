import random
SOLVED = list(range(1,16)) + [0]


def is_adjacent(tiles, index):
    row = index // 4
    column = index % 4

    index_blank= tiles.index(0)
    row_blank = index_blank //4
    column_blank = index_blank % 4

    if (row == row_blank)and(abs(column-column_blank)==1):
        return True
    elif (column == column_blank)and(abs(row-row_blank)==1):
        return True
    else : 
        return False

        
def neighbors(tiles):
    boards_available = []
    index_blank = tiles.index(0)
    for i in range(16):
        if not is_adjacent(tiles, i):
            continue

        tiles_copy = list(tiles)
        tiles_copy[i], tiles_copy[index_blank] = tiles_copy[index_blank], tiles_copy[i]

        boards_available.append([i,tuple(tiles_copy)])

    return boards_available


def distance(tiles):
    total = 0
    for number in range(1, 16):
        index_now = tiles.index(number)
        row_now = index_now // 4
        column_now = index_now % 4

        index_solved = number -1
        row_solved = index_solved//4
        column_solved = index_solved % 4

        total += abs(row_now-row_solved)+abs(column_now-column_solved)

    return total


class Board:
    def __init__(self):
        self.tiles = list(SOLVED)

    def is_solved(self):
        return self.tiles == SOLVED

    def find_blank(self):
        return self.tiles.index(0)


    def move(self, index):
        index_blank = self.find_blank()
        if is_adjacent(self.tiles, index):
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


    