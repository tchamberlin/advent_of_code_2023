"""Day 2, Part 2

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the
minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five
powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

import math
import re
from collections import defaultdict
from pathlib import Path

COLOR_REGEX = re.compile(r"(\d+) (\w+)")


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def get_show_power(line: str):
    """Determine power of given show

    Power is the product of the smallest possible value for each color
    """
    d = defaultdict(int)
    matches = COLOR_REGEX.findall(line)
    for num, color in matches:
        if int(num) > d[color]:
            d[color] = int(num)

    return math.prod(d.values())


def get_total_show_power(lines: list[str]):
    """Determine the total power of the show

    The total power is the sum of all show powers
    """
    total = 0
    for line in lines:
        total += get_show_power(line)
    return total


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    answer = get_total_show_power(lines)
    return answer


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input_p1.txt")
    actual = get_total_show_power(lines)
    expected = 2286
    assert actual == expected


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
