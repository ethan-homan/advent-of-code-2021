import numpy as np

if __name__ == "__main__":

    raw_input = open("input.txt").read()
    boards = []
    nums = []
    for i, item in enumerate(raw_input.split("\n\n")):
        if i == 0:
            nums = [int(k) for k in item.strip().split(",")]
        else:
            board = []
            for j in item.splitlines():
                board.append([int(k) for k in j.split()])
            boards.append(board)

    boards = np.array(boards)

    # make sure no values are negative since we will use -1 to mark numbers drawn on boards
    assert boards.min() >= 0

    for i in nums:

        # mark  drawn numbers
        boards[(boards == i)] = -1

        # score boards along rows and columns
        board_scores = np.minimum(
            boards.sum(axis=1).min(axis=1),
            boards.sum(axis=2).min(axis=1),
        )

        # check if a board has a column or row with all -1's
        if board_scores.min() == -5:
            winning_board_idx = np.argmin(board_scores)
            winning_number = i
            winning_board_values = boards[winning_board_idx, :, :]
            # set -1's to 0 so they don't affect the sum
            winning_board_values[(winning_board_values == -1)] = 0
            print(winning_number * winning_board_values.sum())
            break
