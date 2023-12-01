from day1 import day1_part1, day1_part2


def test_day1_part1():
    actual = day1_part1.solve()
    expected = 55834
    assert actual == expected


def test_day1_part2():
    answer = day1_part2.solve()
    actual_answer = 53221
    assert answer == actual_answer
