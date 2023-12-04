"""Day 4, Part 2"""


from collections import deque
from pathlib import Path


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def get_card_score(string: str):
    """Parse the card string and return the card number and # of winning numbers owned by the player"""
    card_str, rest = string.split(":")
    _, card_num_str = card_str.split()
    card_num = int(card_num_str)
    winning_numbers_str, player_numbers_str = rest.split("|")
    winning_numbers = {int(n) for n in winning_numbers_str.split()}
    player_numbers = {int(n) for n in player_numbers_str.split()}
    winning_numbers_owned_by_player = player_numbers.intersection(winning_numbers)
    return card_num, len(winning_numbers_owned_by_player)


def scratch_cards(lines: list[str]):
    """Determine the total number of cards the player will have after scratching them all off"""
    scores: dict[int, int] = {}
    for line in lines:
        card_num, score = get_card_score(line)
        scores[card_num] = score
    initial_cards = {c: 1 for c in scores}
    to_process = deque(initial_cards)
    total_num_cards = len(initial_cards)
    while to_process:
        card_num = to_process.pop()
        score = scores[card_num]
        for offset in range(1, score + 1):
            # Add a copy of the card to our to_process
            to_process.append(card_num + offset)
            total_num_cards += 1

    return total_num_cards


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    return scratch_cards(lines)


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input.txt")
    total_num_cards = scratch_cards(lines)
    expected_score = 30
    assert total_num_cards == expected_score, f"Expected {total_num_cards=} to equal {expected_score=}"


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
    expected_answer = 5_667_240
    assert answer == expected_answer, f"Expected {answer=} to equal {expected_answer=}"
