from day03.solution import (
    filter_active_instructions,
    part_1,
    part_2,
    perform_instruction,
    scan_corrupted_memory_part_1,
    scan_corrupted_memory_part_2,
)

PART_1_TEST_ANSWER = 161
PART_2_TEST_ANSWER = 48


def test_perform_instruction():
    assert perform_instruction("mul(44,46)") == 44 * 46
    assert perform_instruction("mul(123,4)") == 123 * 4


def test_scan_corrupted_memory_part_1():
    assert scan_corrupted_memory_part_1("mul(4*, mul(6,9!, ?(12,34)") == []
    assert scan_corrupted_memory_part_1("mul ( 2 , 4 )") == []

    assert scan_corrupted_memory_part_1(
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
    ) == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]


def test_scan_corrupted_memory_part_2():
    assert scan_corrupted_memory_part_2("mul(4*, mul(6,9!, ?(12,34)") == []
    assert scan_corrupted_memory_part_2("mul ( 2 , 4 )") == []

    assert scan_corrupted_memory_part_2(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
    ) == ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]


def test_filter_active_instructions():
    assert filter_active_instructions(
        ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"],
    ) == ["mul(2,4)", "mul(8,5)"]


def test_part_1():
    assert part_1("test_part_1.txt") == PART_1_TEST_ANSWER


def test_part_2():
    assert part_2("test_part_2.txt") == PART_2_TEST_ANSWER
