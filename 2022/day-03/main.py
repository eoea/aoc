#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

from typing import List, Dict, Set

def priority(items: Set[str]) -> int:
    """Items are converted to their respective priority."""
    item: str = list(items)[0]
    p: int = ord(item)-96
    if p < 0:
        p = ord(item)-38
    return p

def compare(compartments: List[str]) -> Set[str]:
    """Checks if a distinct item is present in both compartments
    and returns a set containing those items"""
    same_item: Set[str] = set()
    for i in compartments[0]:
        if i in compartments[1]:
            same_item.add(i)
    return same_item

def separate(items: str) -> List[str]:
    """Returns two separate items in a compartment"""
    mid = int(len(items)/2)
    group: List[str] = []
    group.extend([items[:mid], items[mid:-1]])
    return group

def main() -> None:
    group: Dict[int,List[str]] = {}

    with open("input.txt", encoding="utf-8") as f:
        i = 0
        for items in f:
            group[i] = separate(items)
            i+=1

    a: List[int] = []
    for _, v in group.items():
        a.append(priority(compare(v)))

    print(sum(a))


if __name__ == "__main__":
    main()
