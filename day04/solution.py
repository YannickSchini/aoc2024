import re
from pathlib import Path

CURRENT_FOLDER = Path(__file__).parent
REGEX_PATTERN = r"XMAS"
XMAS_CONVOLUTION_WIDTH = 3
XMAS_CONVOLUTION_HEIGTH = 3


def create_grid(filename: str) -> list[list[str]]:
    with (CURRENT_FOLDER / filename).open() as f:
        lines = f.readlines()
    return [list(line.strip("\n")) for line in lines]


def part_1(filename: str) -> int:
    grid = create_grid(filename)

    number_of_patterns = 0
    number_of_patterns += find_horizontal_patterns(grid)
    number_of_patterns += find_vertical_patterns(grid)
    number_of_patterns += find_diagonal_patterns(grid)

    return number_of_patterns


def find_pattern_in_array(input_array: list[str]) -> int:
    string = "".join(input_array)
    return len(re.findall(REGEX_PATTERN, string))


def find_horizontal_patterns(grid: list[list[str]]) -> int:
    result = 0
    for line in grid:
        # Forwards
        result += find_pattern_in_array(line)
        # Backwards
        result += find_pattern_in_array(line[::-1])
    return result


def find_vertical_patterns(grid: list[list[str]]) -> int:
    rotated_grid = zip(*grid[::-1], strict=False)
    result = 0
    for line in rotated_grid:
        # Forwards
        result += find_pattern_in_array(line)  # type:ignore[arg-type]
        # Backwards
        result += find_pattern_in_array(line[::-1])  # type:ignore[arg-type]
    return result


def find_diagonal_patterns(grid: list[list[str]]) -> int:
    rotated_grid = get_low_left_to_up_right_diagonal_grid(grid)
    result = 0
    for line in rotated_grid:
        # Forwards
        result += find_pattern_in_array(line)
        # Backwards
        result += find_pattern_in_array(line[::-1])

    rotated_grid_other_way = get_up_left_to_low_right_diagonal_grid(grid)
    for line in rotated_grid_other_way:
        # Forwards
        result += find_pattern_in_array(line)
        # Backwards
        result += find_pattern_in_array(line[::-1])
    return result


def get_low_left_to_up_right_diagonal_grid(grid: list[list[str]]) -> list[list[str]]:
    rotated_grid = []
    if len(grid) != len(grid[0]):
        raise ValueError
    for i in range(len(grid)):
        rotated_array = [grid[j][i - j] for j in range(i + 1)]
        rotated_grid.append(rotated_array)

    for i in reversed(list(range(1, len(grid)))):
        rotated_array = [grid[len(grid) - i + j][len(grid) - j - 1] for j in range(i)]
        rotated_grid.append(rotated_array)

    return rotated_grid


def get_up_left_to_low_right_diagonal_grid(grid: list[list[str]]) -> list[list[str]]:
    rotated_grid = []
    if len(grid) != len(grid[0]):
        raise ValueError
    for i in range(len(grid)):
        rotated_array = [grid[len(grid) - i - 1 + j][j] for j in range(i + 1)]
        rotated_grid.append(rotated_array)

    for i in reversed(list(range(1, len(grid)))):
        rotated_array = [grid[j][len(grid) - i + j] for j in range(i)]
        rotated_grid.append(rotated_array)

    return rotated_grid


def part_2(filename: str) -> int:
    grid = create_grid(filename)

    result = 0
    print(len(grid))
    for x in range(len(grid) - XMAS_CONVOLUTION_WIDTH + 1):
        for y in range(len(grid[0]) - XMAS_CONVOLUTION_HEIGTH + 1):
            result += apply_xmas_convolution_to_position(grid, x, y)

    return result


def apply_xmas_convolution_to_position(grid: list[list[str]], x: int, y: int) -> bool:
    return (
        (
            grid[x][y] == "M"
            and grid[x][y + 2] == "S"
            and grid[x + 1][y + 1] == "A"
            and grid[x + 2][y] == "M"
            and grid[x + 2][y + 2] == "S"
        )
        or (
            grid[x][y] == "M"
            and grid[x][y + 2] == "M"
            and grid[x + 1][y + 1] == "A"
            and grid[x + 2][y] == "S"
            and grid[x + 2][y + 2] == "S"
        )
        or (
            grid[x][y] == "S"
            and grid[x][y + 2] == "S"
            and grid[x + 1][y + 1] == "A"
            and grid[x + 2][y] == "M"
            and grid[x + 2][y + 2] == "M"
        )
        or (
            grid[x][y] == "S"
            and grid[x][y + 2] == "M"
            and grid[x + 1][y + 1] == "A"
            and grid[x + 2][y] == "S"
            and grid[x + 2][y + 2] == "M"
        )
    )


if __name__ == "__main__":
    print("Part 1: ", part_1("input.txt"))
    print("Part 2: ", part_2("input.txt"))
