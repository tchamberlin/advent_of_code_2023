"""Day 2, Part 1

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

"""
import re
from pathlib import Path

COLOR = re.compile(r"(\d+) (red|green|blue)")


MAX = {"red": 12, "green": 13, "blue": 14}


def get_data(path: Path | str):
    """Return lines of text from file at given path"""
    return Path(path).read_text().splitlines()


def show_is_possible(show: str):
    for c in show.split(","):
        m = COLOR.match(c.strip())
        print(f"{m=}; {c=}")
        if m:
            num, color = m.group(1), m.group(2)
            num = int(num)
            print(f"{num=}; {MAX[color]=}; {color=}")
            if num > MAX[color]:
                print(f"{show=} is impossible")
                return False
    print(f"{show=} is possible")
    return True


def parse_data(
    lines: list[str],
):
    total = 0
    for line in lines:
        game, rest = line.split(":")
        _, game_id = game.split(" ")
        shows = rest.split(";")
        if all(show_is_possible(show.strip()) for show in shows):
            total += int(game_id)
    return total


def solve():
    """Compute final puzzle answer from input file"""
    lines = get_data(Path(__file__).parent / "input.txt")
    answer = parse_data(lines)
    return answer


def test():
    """Check puzzle test case"""
    lines = get_data(Path(__file__).parent / "test_input_p1.txt")
    actual = parse_data(lines)
    assert actual == 8


if __name__ == "__main__":
    test()
    answer = solve()
    print(answer)
