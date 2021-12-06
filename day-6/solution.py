import numpy as np

T = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],  # number of 6's in this period is the sum of the 0's and 7's from the prev period
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],  # number of 8's this period are the number of 0's prev period
], dtype=int).T


if __name__ == "__main__":

    data = [int(i) for i in open("input.txt").read().split(",")]

    # get the initial population in each state
    counts = np.zeros(9, dtype=int)
    for i in data:
        counts[i] += 1

    # iterate forward 80 days from the initial state
    counts = np.dot(counts, np.linalg.matrix_power(T, 80))
    print(f"Part 1: After 80 days there would be {counts.sum()} fish")

    # iterate the remaining days to 256
    counts = np.dot(counts, np.linalg.matrix_power(T, 256 - 80))
    print(f"Part 2: After 256 days there would be {counts.sum()} fish")
