#!/usr/bin/env python3
def main() -> None:

    with open("input.txt") as f:
        elves = dict()
        elf = 1
        cal = 0
        for line in f:
            if line == "\n":
                elf += 1
                cal = 0
            else:
                cal += int(line)
                elves[elf] = cal

    elf = 0
    cal = 0
    for k in elves:
        if elves[k] > cal:
            cal = elves[k]
            elf = k

    print(f"elf {elf} has the highest calories: {cal}")

if __name__ == "__main__":
    main()
