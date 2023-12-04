"""Day 3, Part 2"""

import math
from collections import defaultdict
from pathlib import Path

surrounding: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def determine_gear_location(x: int, y: int, lines: list[str]):
    """Determine whether given gear position is adjacent to a part number"""
    for xo, yo in surrounding:
        try:
            if lines[y][x].isdigit() and lines[y + yo][x + xo] == "*":
                return (x + xo, y + yo)
        except IndexError:
            pass
    return None


def find_sum_of_all_gear_ratios(lines: list[str]):
    """Find all gears; return sum of their ratios"""
    m = defaultdict(list)
    loc = None
    for y, line in enumerate(lines):
        part_num = ""
        for x, c in enumerate(line):
            if c.isnumeric():
                part_num += c
                _loc = determine_gear_location(x, y, lines)
                if _loc:
                    loc = _loc
                    print(f"Found gear at {loc}")

            else:
                if part_num:
                    if loc:
                        print(f"PN: {part_num}")
                        m[loc].append(int(part_num))
                        loc = None
                    else:
                        print(f"NOT PN: {part_num}")
                part_num = ""
        if part_num and loc:
            print(f"PN: {part_num}")
            m[loc].append(int(part_num))
            loc = None
    return [math.prod(v) for k, v in m.items() if len(v) == 2]


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    part_nums = find_sum_of_all_gear_ratios(lines)
    answer = sum(part_nums)
    return answer


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input_p1.txt")
    part_nums = find_sum_of_all_gear_ratios(lines)
    actual = sum(part_nums)
    expected = 467835
    print(f"{actual=}")
    assert actual == expected


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
