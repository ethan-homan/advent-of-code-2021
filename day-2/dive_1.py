
if __name__ == "__main__":
    depth = 0
    horizontal = 0

    with open("input.txt") as infile:
        for line in infile:
            direction, step = line.split()
            if direction == "forward":
                horizontal += int(step)
            elif direction == "up":
                depth -= int(step)
            elif direction == "down":
                depth += int(step)
            else:
                raise Exception

    print(depth * horizontal)
