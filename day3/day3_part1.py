"""

"""
from pathlib import Path

surrounding = [
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


def is_symbol(c: str):
    if c.isdigit() or c == ".":
        return False
    return True


def is_adjacent_to_symbol(x: int, y: int, lines: list[str]):
    for xo, yo in surrounding:
        try:
            if lines[y][x].isdigit() and is_symbol(lines[y + yo][x + xo]):
                return True

        except IndexError:
            pass
    return False


def get_part_numbers(lines: list[str]):
    part_nums = []
    for y, line in enumerate(lines):
        part_num = ""
        is_pn = False
        for x, c in enumerate(line):
            if c.isnumeric():
                part_num += c
                if is_adjacent_to_symbol(x, y, lines):
                    is_pn = True
            else:
                if part_num:
                    if is_pn:
                        print(f"PN: {part_num}")
                        part_nums.append(int(part_num))
                        is_pn = False
                    else:
                        print(f"NOT PN: {part_num}")
                part_num = ""
        if part_num and is_pn:
            print(f"PN: {part_num}")
            part_nums.append(int(part_num))
    return part_nums


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    part_nums = get_part_numbers(lines)
    answer = sum(part_nums)
    return answer


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input_p1.txt")
    part_nums = get_part_numbers(lines)
    actual = sum(part_nums)
    expected = 4361
    print(f"{actual=}")
    assert actual == expected


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
