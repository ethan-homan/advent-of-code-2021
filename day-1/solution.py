
if __name__ == "__main__":
    data = []

    with open("input.txt") as infile:
        for line in infile:
            data.append(int(line.strip()))

    num_bigger = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            num_bigger += 1

    print(f"Part 1: {num_bigger}")

    num_bigger = 0
    for i in range(1, len(data)):
        sum_1 = data[i] + data[i-1] + data[i-2]
        sum_2 = data[i-3] + data[i-1] + data[i-2]
        if sum_1 > sum_2:
            num_bigger += 1

    print(f"Part 2: {num_bigger}")
