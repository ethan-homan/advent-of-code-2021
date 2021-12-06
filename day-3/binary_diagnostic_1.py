
if __name__ == "__main__":

    with open("input.txt") as infile:
        input_len = 0
        for i, line in enumerate(infile):
            line = line.strip()
            input_len += 1
            if i == 0:
                counts = [0] * len(line)
            for j, bit in enumerate(line):
                counts[j] += int(bit)

    counts = [int(i/input_len * 2) for i in counts]

    gamma = 0
    for i, bit in enumerate(counts):
        gamma += bit * (2 ** (len(counts) - i - 1))

    epsilon = 0
    for i, bit in enumerate(counts):
        epsilon += abs(bit - 1) * (2 ** (len(counts) - i - 1))

    print(gamma * epsilon)
