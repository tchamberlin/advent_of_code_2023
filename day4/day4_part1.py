"""Day 4, Part 1

Determine which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one
point and each match after the first doubles the point value of that card.
"""

from pathlib import Path


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def get_card_score(string: str):
    """Parse the card string and return the card number and # of winning numbers owned by the player"""
    _, rest = string.split(":")
    winning_numbers_str, player_numbers_str = rest.split("|")
    winning_numbers = {int(n) for n in winning_numbers_str.split()}
    player_numbers = {int(n) for n in player_numbers_str.split()}

    winning_numbers_owned_by_player = player_numbers.intersection(winning_numbers)
    num_winning_numbers_owned_by_player = len(winning_numbers_owned_by_player)
    if num_winning_numbers_owned_by_player == 0:
        return 0
    return 2 ** (num_winning_numbers_owned_by_player - 1)


def get_total_score(lines: list[str]):
    """Determine total score across all cards"""
    return sum(get_card_score(line) for line in lines)


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    return get_total_score(lines)


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input.txt")
    total_score = get_total_score(lines)
    expected = 13
    assert total_score == expected, f"Expected {answer=} to equal {expected=}"


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
    expected_answer = 25_183
    assert answer == expected_answer, f"Expected {answer=} to equal {expected_answer=}"
