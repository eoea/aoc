#!/usr/bin/env python3
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=C0103

"""
In the protocol being used by the Elves, the start of a
packet is indicated by a sequence of four characters that
are all different.

"""
from typing import List

def start_of_packet(datastream: str) -> int:
    """
    Takes a packet and returns the start of the
    packet marker. According to this protocol the
    start of a packet is indicated by a sequence of
    four characters that are all different.
    """
    c = 0
    j = 4
    d_stream: List[str] = []
    for data in datastream:
        c+=1
        if len(d_stream) == 4:
            break
        if data in datastream[c:j]:
            d_stream.clear()
        j+=1
        d_stream.append(data)

    return c

def main() -> None:
    datastreams: List[str] = [
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    ]

    for datastream in datastreams:
        print(start_of_packet(datastream))

if __name__ == "__main__":
    main()
