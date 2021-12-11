
if __name__ == "__main__":
    depth = 0
    horizontal = 0
    aim = 0

    with open("input.txt") as infile:
        for line in infile:
            direction, step = line.split()
            if direction == "forward":
                horizontal += int(step)
                depth += int(step) * aim
            elif direction == "up":
                aim -= int(step)
            elif direction == "down":
                aim += int(step)
            else:
                raise Exception

    print(depth * horizontal)
