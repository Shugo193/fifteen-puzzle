from puzzle.board import Board, SOLVED

def test_new_board_is_solved():
    board = Board()
    assert board.is_solved()


def test_is_adjacent_not_across_rows():
    board = Board()
    board.tiles[15], board.tiles[4] = board.tiles[4], board.tiles[15]
    assert not board.is_adjacent(3)
    assert board.is_adjacent(0)
    assert board.is_adjacent(5)
    assert board.is_adjacent(8)


def test_move_passed():
    board = Board()
    assert board.move(14)
    assert board.tiles[14] == 0
    assert board.tiles[15] == 15

def test_move_failed():
    board = Board()
    assert not board.move(1)
    assert board.tiles == SOLVED


def test_solved_not_modified():
    board = Board()
    board.shuffle()

    assert SOLVED == list(range(1,16)) + [0]

def test_shuffle():
    board = Board()
    board.shuffle()
    complete = True

    for i in range(16):
        if i not in board.tiles:
            complete = False

    assert complete

def test_neighbors_solved():
    board = Board()
    neighbors = board.neighbors()

    indexes = {i for i, tiles in neighbors}

    assert len(neighbors) == 2
    assert board.tiles == list(range(1,16)) + [0]
    assert indexes == {11, 14}

def test_neighbors_innerindex():
    board = Board()
    board.tiles[15], board.tiles[5] = board.tiles[5], board.tiles[15]
    neighbors = board.neighbors()
    indexes = {i for i, tiles in neighbors}

    assert len(neighbors) == 4
    assert indexes == {1,4,6,9}



