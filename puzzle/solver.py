import heapq
from puzzle.board import SOLVED, neighbors, distance

def solve(tiles):
    board_start = tuple(tiles)
    board_goal = tuple(SOLVED)

    queue = []
    steps_moved = 0
    steps_prospect = distance(tiles)
    steps_total = steps_moved + steps_prospect

    heapq.heappush(queue, (steps_total, steps_moved, board_start, []))

    board_history = set()

    while len(queue) > 0:
        steps_total, steps_moved, board, process = heapq.heappop(queue)
        if board ==board_goal:
            return process
        if board in board_history:
            continue

        board_history.add(tuple(board))

        for index, board_next in neighbors(board):
            process_next = process +  [index]

            steps_moved_next = steps_moved + 1
            steps_prospect = distance(board_next)
            steps_total = steps_moved_next + steps_prospect

            heapq.heappush(queue, (steps_total, steps_moved_next, board_next, process_next))

    return None
