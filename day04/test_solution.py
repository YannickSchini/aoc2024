from day04.solution import (
    create_grid,
    find_diagonal_patterns,
    find_horizontal_patterns,
    find_pattern_in_array,
    find_vertical_patterns,
    get_low_left_to_up_right_diagonal_grid,
    get_up_left_to_low_right_diagonal_grid,
    part_1,
)

PART_1_TEST_ANSWER = 18
NUMBER_OF_HORIZONTAL_XMAS_IN_TEST = 5
NUMBER_OF_VERTICAL_XMAS_IN_TEST = 3
NUMBER_OF_DIAGONAL_XMAS_IN_TEST = 10


def test_part_1():
    assert part_1("test.txt") == PART_1_TEST_ANSWER


def test_find_pattern_in_array():
    array_with_two_patterns = list("XMASMMMXMASM")
    assert find_pattern_in_array(array_with_two_patterns) == 2  # Noqa: PLR2004
    array_with_no_patterns = list("MASMMMSAMXM")
    assert find_pattern_in_array(array_with_no_patterns) == 0


def test_find_horizontal_patterns():
    grid = create_grid("test.txt")
    assert find_horizontal_patterns(grid) == NUMBER_OF_HORIZONTAL_XMAS_IN_TEST


def test_find_vertical_patterns():
    grid = create_grid("test.txt")
    assert find_vertical_patterns(grid) == NUMBER_OF_VERTICAL_XMAS_IN_TEST


def test_find_diagonal_patterns():
    grid = create_grid("test.txt")
    assert find_diagonal_patterns(grid) == NUMBER_OF_DIAGONAL_XMAS_IN_TEST


def test_get_low_left_to_up_right_diagonal_grid():
    grid = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    expected_resulting_grid = [["a"], ["b", "d"], ["c", "e", "g"], ["f", "h"], ["i"]]
    assert get_low_left_to_up_right_diagonal_grid(grid) == expected_resulting_grid

    grid = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]
    expected_resulting_grid = [
        ["a"],
        ["b", "e"],
        ["c", "f", "i"],
        ["d", "g", "j", "m"],
        ["h", "k", "n"],
        ["l", "o"],
        ["p"],
    ]
    assert get_low_left_to_up_right_diagonal_grid(grid) == expected_resulting_grid


def test_get_up_left_to_low_right_diagonal_grid():
    grid = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    expected_resulting_grid = [["g"], ["d", "h"], ["a", "e", "i"], ["b", "f"], ["c"]]
    assert get_up_left_to_low_right_diagonal_grid(grid) == expected_resulting_grid

    grid = [
        ["a", "b", "c", "d"],
        ["e", "f", "g", "h"],
        ["i", "j", "k", "l"],
        ["m", "n", "o", "p"],
    ]
    expected_resulting_grid = [
        ["m"],
        ["i", "n"],
        ["e", "j", "o"],
        ["a", "f", "k", "p"],
        ["b", "g", "l"],
        ["c", "h"],
        ["d"],
    ]
    assert get_up_left_to_low_right_diagonal_grid(grid) == expected_resulting_grid
