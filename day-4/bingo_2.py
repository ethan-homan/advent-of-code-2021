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

        # score boards along rows and columns.
        # a winning score is -5 which means a row or column is all -1's
        board_scores = np.minimum(
            boards.sum(axis=1).min(axis=1),
            boards.sum(axis=2).min(axis=1),
        )

        # if there's only one board left, store the index
        if (len(board_scores) - len(board_scores[board_scores == -5])) == 1:
            last_board_idx = np.argmax(board_scores)

        # once the last board "wins", compute the sum of the unmarked nums
        if board_scores.max() == -5:
            last_winning_number = i
            last_board_values = boards[last_board_idx, :, :]
            last_board_values[(last_board_values == -1)] = 0
            last_unmarked_score = last_board_values.sum()
            break

    print(last_winning_number * last_unmarked_score)
