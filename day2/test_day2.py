from day2 import day2_part1, day2_part2


def test_day2_part1():
    actual = day2_part1.solve()
    expected = 2810
    assert actual == expected


def test_day2_part2():
    answer = day2_part2.solve()
    actual_answer = 69110
    assert answer == actual_answer
