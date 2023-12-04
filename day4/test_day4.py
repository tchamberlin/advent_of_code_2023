from day4 import day4_part1, day4_part2


def test_day4_part1():
    actual = day4_part1.solve()
    expected = 25_183
    assert actual == expected


def test_day4_part2():
    answer = day4_part2.solve()
    actual_answer = 5_667_240
    assert answer == actual_answer
