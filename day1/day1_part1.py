"""Day 1, Part 1

> On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to
  form a single two-digit number
"""

from pathlib import Path


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def get_first_number(string: str):
    """Return the first numeric character in given string"""
    for c in string:
        if c.isnumeric():
            return c
    msg = f"Given string {string} does not contain a number!"
    raise ValueError(msg)


def parse_cal_value(line: str):
    """Find the first and last digit in given line; compose and return as an int"""
    first_num = get_first_number(line)
    last_num = get_first_number(line[::-1])

    if first_num is None or last_num is None:
        msg = f"Expected values for both {first_num=} and {last_num=} with {line=}"
        raise AssertionError(msg)

    return int(first_num + last_num)


def parse_cal_values(lines: list[str]):
    """Find the calibration values in all given lines"""
    for line in lines:
        yield parse_cal_value(line)


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    cal_values = parse_cal_values(lines)
    cal = sum(cal_values)
    return cal


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input_p1.txt")
    actual_sum = sum(parse_cal_values(lines))
    expected_sum = sum([12, 38, 15, 77])
    if actual_sum != expected_sum:
        msg = f"Expected {actual_sum=} to equal {expected_sum=}"
        raise AssertionError(msg)


if __name__ == "__main__":
    test()
    answer = solve()
    actual_answer = 55834
    assert answer == actual_answer
    print(answer)
