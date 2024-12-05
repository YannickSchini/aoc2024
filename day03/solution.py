import re
from pathlib import Path

CURRENT_FOLDER = Path(__file__).parent
MULTIPLICATION_INSTRUCTION_REGEX = r"mul\(\d*,\d*\)"
DO_REGEX = r"do\(\)"
DONT_REGEX = r"don't\(\)"


def scan_corrupted_memory_part_1(corrupted_memory: str) -> list[str]:
    return re.findall(MULTIPLICATION_INSTRUCTION_REGEX, corrupted_memory)


def scan_corrupted_memory_part_2(corrupted_memory: str) -> list[str]:
    regex_pattern = MULTIPLICATION_INSTRUCTION_REGEX + "|" + DO_REGEX + "|" + DONT_REGEX
    return re.findall(regex_pattern, corrupted_memory)


def perform_instruction(instruction: str) -> int:
    a, b = instruction.strip("mul(").strip(")").split(",")
    return int(a) * int(b)


def filter_active_instructions(instruction_list: list[str]) -> list[str]:
    result = []
    enabled = True
    for instruction in instruction_list:
        if re.match(MULTIPLICATION_INSTRUCTION_REGEX, instruction) and enabled:
            result.append(instruction)
        elif re.match(DO_REGEX, instruction):
            enabled = True
        elif re.match(DONT_REGEX, instruction):
            enabled = False
    return result


def part_1(filename: str) -> int:
    with (CURRENT_FOLDER / filename).open() as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        for instruction in scan_corrupted_memory_part_1(line):
            result += perform_instruction(instruction)

    return result


def part_2(filename: str) -> int:
    with (CURRENT_FOLDER / filename).open() as f:
        lines = f.readlines()

    instruction_list = scan_corrupted_memory_part_2("".join(lines))
    print(instruction_list)

    filtered_instruction_list = filter_active_instructions(instruction_list)
    print(filtered_instruction_list)

    result = 0
    for instruction in filtered_instruction_list:
        result += perform_instruction(instruction)

    return result


if __name__ == "__main__":
    print("Part 1: ", part_1("input.txt"))
    print("Part 2: ", part_2("input.txt"))
