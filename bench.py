import time
from puzzle.board import Board
from puzzle.solver import solve

for shuffle in [50, 100, 200]:
    board = Board()
    board.shuffle(shuffle)
    for weight in [1, 2, 3]:
        if shuffle > 50 and weight == 1:
            continue
        start = time.perf_counter()
        result = solve(board.tiles, weight)
        end = time.perf_counter()
        print(f"shuflle {shuffle}、w={weight}: {len(result)}手、{end-start:.2f}秒")