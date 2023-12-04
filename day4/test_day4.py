from pathlib import Path

from day4.day4_part1 import get_card_score, get_data, parse_card


def test_parse_card():
    expected = [
        (1, {41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}),
        (2, {32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}),
        (3, {1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}),
        (4, {69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}),
        (5, {32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}),
        (6, {72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}),
    ]
    lines = get_data(Path(__file__).parent / "test_input.txt")
    cards = [parse_card(line) for line in lines]
    assert cards == expected


def test_get_card_score():
    assert get_card_score({41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}) == 8
    assert get_card_score({32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}) == 2
    assert get_card_score({1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}) == 2
    assert get_card_score({69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}) == 1
    assert get_card_score({32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}) == 0
    assert get_card_score({72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}) == 0
