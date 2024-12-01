from solution import compute_similarity, get_lists, part_1, part_2
from solution import compute_distance
import pytest


def test_get_lists():
    list_a, list_b = get_lists("test.txt")
    assert list_a == [3, 4, 2, 1, 3, 3]
    assert list_b == [4, 3, 5, 3, 9, 3]


@pytest.mark.parametrize(["a", "b", "result"], [(1, 1, 0), (3, 1, 2), (1, 3, 2)])
def test_compute_distance(a: int, b: int, result: int):
    assert compute_distance(a, b) == result


def test_part_1():
    distance = part_1("test.txt")
    assert distance == 11


@pytest.mark.parametrize(
    ["a", "right_list", "result"], [(3, [2, 3, 3], 6), (3, [2, 4, 5], 0)]
)
def test_similarity_score(a: int, right_list: list[int], result: int):
    assert compute_similarity(a, right_list) == result


def test_part_2():
    similarity = part_2("test.txt")
    assert similarity == 31
