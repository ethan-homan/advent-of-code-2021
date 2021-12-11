import numpy as np

if __name__ == "__main__":

    with open("input.txt") as infile:
        data = []
        for i, line in enumerate(infile):
            data.append([int(j) for j in line.strip()])
    data = np.array(data)

    def filter_by_freq(data: np.ndarray, type: str) -> int:
        width = data.shape[1]
        for i in range(width):
            most_common = int(data[:, i].sum() / len(data) * 2)
            if type == "most common":
                data = data[(data[:, i] == most_common)]
            elif type == "least common":
                data = data[(data[:, i] != most_common)]
            if len(data) == 1:
                data = data[0]
                break
        decimal = 0
        for i, bit in enumerate(data):
            decimal += bit * (2 ** (len(data) - i - 1))
        return decimal

    print(filter_by_freq(data, "least common") * filter_by_freq(data, "most common"))
