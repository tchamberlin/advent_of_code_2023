"""Day 1, Part 2

> The newly-improved calibration document consists of lines of text; each line originally contained a specific
  calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining
  the first digit and the last digit (in that order) to form a single two-digit number.
"""
import re
from pathlib import Path

DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
_number_regex = "|".join((*DIGIT_MAP, r"\d"))
_reversed_number_regex = "|".join((*[d[::-1] for d in DIGIT_MAP], r"\d"))
# Compose a regex like '(one|two|...|\d)'
NUMBER_REGEX = re.compile(f"({_number_regex})")
# Compose a regex like '(eno|owt|...|\d)' -- intended to be used on the reversed line
NUMBER_REVERSE_REGEX = re.compile(f"({_reversed_number_regex})")


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def parse_cal_value(line: str):
    """Find the first and last digit in given line; compose and return as an int"""
    first_num_match = NUMBER_REGEX.search(line)
    if not first_num_match:
        msg = f"Expected matches for {line=}"
        raise AssertionError(msg)

    last_num_match = NUMBER_REVERSE_REGEX.search(line[::-1])
    if not last_num_match:
        msg = f"Expected matches for {line=}"
        raise AssertionError(msg)

    _first_num = str(first_num_match.group(1))
    _last_num = str(last_num_match.group(1)[::-1])
    first_num = DIGIT_MAP.get(_first_num, _first_num)
    last_num = DIGIT_MAP.get(_last_num, _last_num)
    return int(first_num + last_num)


def parse_cal_values(lines: list[str]):
    """Find the calibration values in all given lines"""
    for line in lines:
        yield parse_cal_value(line)


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    cal_values = parse_cal_values(lines)
    return sum(cal_values)


def test():
    """Check puzzle test case"""
    # Had to add a test case here to cover an edge case
    lines = get_data(Path(__file__).parent / "test_input_p2.txt")
    expected_cal_values = [29, 83, 13, 24, 42, 14, 76, 48]
    actual_cal_values = list(parse_cal_values(lines))
    if actual_cal_values != expected_cal_values:
        msg = f"Expected {actual_cal_values=} to equal {expected_cal_values=}"
        raise AssertionError(msg)

    expected_sum = 281 + 48
    actual_sum = sum(actual_cal_values)
    if actual_sum != expected_sum:
        msg = f"Expected {actual_sum=} to equal {expected_sum=}"
        raise AssertionError(msg)


if __name__ == "__main__":
    test()
    answer = solve()
    actual_answer = 53221
    assert answer == actual_answer
    print(answer)
