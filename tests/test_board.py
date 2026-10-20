from puzzle.board import Board, SOLVED, is_adjacent, neighbors, distance
from puzzle.solver import solve

def test_new_board_is_solved():
    board = Board()
    assert board.is_solved()


def test_is_adjacent_not_across_rows():
    board = Board()
    board.tiles[15], board.tiles[4] = board.tiles[4], board.tiles[15]
    assert not is_adjacent(board.tiles, 3)
    assert is_adjacent(board.tiles, 0)
    assert is_adjacent(board.tiles, 5)
    assert is_adjacent(board.tiles, 8)


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
    result = neighbors(board.tiles)

    indexes = {i for i, tiles in result}

    assert len(result) == 2
    assert board.tiles == list(range(1,16)) + [0]
    assert indexes == {11, 14}

def test_neighbors_innerindex():
    board = Board()
    board.tiles[15], board.tiles[5] = board.tiles[5], board.tiles[15]
    result = neighbors(board.tiles)
    indexes = {i for i, tiles in result}

    assert len(result) == 4
    assert indexes == {1,4,6,9}


def test_distance_solved():
    board = Board()
    assert distance(board.tiles) == 0


def test_distance_moved():
    board = Board()
    board.move(14)
    assert distance(board.tiles) == 1


def test_solver_solved():
    board = Board()
    process = solve(board.tiles)

    assert process == []

def test_solver_1stepmoved():
    board = Board()
    board.move(14)
    process = solve(board.tiles)

    assert process == [15]

def test_solver_shuffle():
    shuffle = 10
    for _ in range(10):
        board = Board()
        board.shuffle(shuffle)

        process = solve(board.tiles)

        for i in process:
            assert board.move(i)

        assert board.tiles == SOLVED
        assert len(process) <= shuffle