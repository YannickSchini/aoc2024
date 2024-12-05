from collections import Counter
from functools import partial
from pathlib import Path
from typing import NewType

LocationList = NewType("LocationList", list[int])
CURRENT_FOLDER = Path(__file__).parent


def get_lists(filename: str) -> tuple[LocationList, LocationList]:
    with (CURRENT_FOLDER / filename).open() as f:
        lines = f.readlines()

    list_a = []
    list_b = []
    for line in lines:
        line_content = line.split(" ")
        list_a.append(int(line_content[0]))
        list_b.append(int(line_content[-1]))

    return LocationList(list_a), LocationList(list_b)


def compute_distance(a: int, b: int) -> int:
    return abs(a - b)


def compute_similarity(a: int, right_list: LocationList) -> int:
    counter = Counter(right_list)
    return counter[a] * a


def part_1(filename: str) -> int:
    list_a, list_b = get_lists(filename)
    list_a.sort()
    list_b.sort()

    total_distance = 0
    for a, b in zip(list_a, list_b, strict=False):
        total_distance += compute_distance(a, b)

    return total_distance


def part_2(filename: str) -> int:
    list_a, list_b = get_lists(filename)
    compute_similarity_on_list_b = partial(compute_similarity, right_list=list_b)

    total_similarity = 0
    for element in list_a:
        total_similarity += compute_similarity_on_list_b(element)

    return total_similarity


if __name__ == "__main__":
    print("Part 1: ", part_1("input.txt"))
    print("Part 2: ", part_2("input.txt"))
