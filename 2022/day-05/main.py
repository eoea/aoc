#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

"""
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

from typing import List

def main() -> None:
    stacks: List[List[str]] = [
        ["Z","N"],
        ["M","C","D"],
        ["P"]
    ]

    stacks[0].append(stacks[1].pop())

    i = 0
    while i < 3:
        stacks[2].append(stacks[0].pop())
        i+=1

    i = 0
    while i < 2:
        stacks[0].append(stacks[1].pop())
        i+=1

    stacks[1].append(stacks[0].pop())

    print(stacks)

if __name__ == "__main__":
    main()
