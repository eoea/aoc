#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

from typing import List, Set, Tuple

def create_set(lo: int, hi: int) -> Set[int]:
    _set: Set[int] = {lo}
    while lo < hi:
        lo += 1
        _set.add(lo)
    return _set

def inclusive_count(elf_a: List[str], elf_b: List[str]) -> int:
    lo_a = int(elf_a[0])
    hi_a = int(elf_a[1])
    set_a: Set[int] = create_set(lo_a, hi_a)

    lo_b = int(elf_b[0])
    hi_b = int(elf_b[1])
    set_b: Set[int] = create_set(lo_b, hi_b)

    c: int = 0
    inter: Set[int] = (set_a.intersection(set_b))
    if len(set_a) == len(inter) or len(set_b) == len(inter):
        c+=1

    return c

def parse(cin: str) -> Tuple[List[str], List[str]]:
    section: List[str] = cin.rstrip().split(",")
    elf_a: List[str] = section[0].split("-")
    elf_b: List[str] = section[1].split("-")
    return elf_a, elf_b

def main() -> None:
    c: int = 0
    with open("input.txt", encoding="utf-8") as f:
        for line in f:
            elf_a, elf_b = parse(line)
            c += inclusive_count(elf_a, elf_b)

    print(c)

if __name__ == "__main__":
    main()
