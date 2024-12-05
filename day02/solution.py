from collections import Counter
from itertools import pairwise
from pathlib import Path
from typing import NewType

CURRENT_FOLDER = Path(__file__).parent
Level = NewType("Level", int)
Report = NewType("Report", list[Level])
DIFFERENCE_THRESHOLD = 3


def get_report_list(filename: str) -> list[Report]:
    with (CURRENT_FOLDER / filename).open() as f:
        lines = f.readlines()

    report_list: list[Report] = []
    for line in lines:
        report = Report([Level(int(x)) for x in line.strip("\n").split(" ")])
        report_list.append(report)
    return report_list


def is_safe_without_problem_dampener(report: Report) -> bool:
    # Check if the difference between two consecutive levels is above threshold
    for level, next_level in pairwise(report):
        if abs(next_level - level) > DIFFERENCE_THRESHOLD:
            return False

    # Check if there are duplicates in the list
    counter = Counter(report)
    if max(counter.values()) > 1:
        return False

    # Check if report is monotonic
    return all(x < y for x, y in pairwise(report)) or all(
        x > y for x, y in pairwise(report)
    )


def is_safe_with_problem_dampener(report: Report) -> bool:
    if is_safe_without_problem_dampener(report):
        return True
    for index in range(len(report)):
        report_without_level = report.copy()
        report_without_level.pop(index)
        if is_safe_without_problem_dampener(Report(report_without_level)):
            return True
    return False


def part_1(filename: str) -> int:
    reports = get_report_list(filename)
    number_of_safe_reports = 0

    for report in reports:
        if is_safe_without_problem_dampener(report):
            number_of_safe_reports += 1
    return number_of_safe_reports


def part_2(filename: str) -> int:
    reports = get_report_list(filename)
    number_of_safe_reports = 0

    for report in reports:
        if is_safe_with_problem_dampener(report):
            number_of_safe_reports += 1
    return number_of_safe_reports


if __name__ == "__main__":
    print("Part 1: ", part_1("input.txt"))
    print("Part 2: ", part_2("input.txt"))
