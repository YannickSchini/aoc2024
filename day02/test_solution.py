from day02.solution import (
    Report,
    is_safe_with_problem_dampener,
    is_safe_without_problem_dampener,
)


def test_is_safe_without_problem_dampener():
    # safe: strictly going down
    report = Report([7, 6, 4, 2, 1])
    assert is_safe_without_problem_dampener(report)

    # unsafe: too big of an increase
    report = Report([1, 2, 7, 8, 9])
    assert not is_safe_without_problem_dampener(report)

    # unsafe: too big of a decrease
    report = Report([9, 7, 6, 2, 1])
    assert not is_safe_without_problem_dampener(report)

    # unsafe: increase AND decrease
    report = Report([1, 3, 2, 4, 5])
    assert not is_safe_without_problem_dampener(report)

    # unsafe: unsafe because not strictly monotonous
    report = Report([8, 6, 4, 4, 1])
    assert not is_safe_without_problem_dampener(report)

    # safe: strictly going up
    report = Report([1, 3, 6, 7, 9])
    assert is_safe_without_problem_dampener(report)


def test_is_safe():
    # safe
    report = Report([7, 6, 4, 2, 1])
    assert is_safe_with_problem_dampener(report)

    # unsafe
    report = Report([1, 2, 7, 8, 9])
    assert not is_safe_with_problem_dampener(report)

    # unsafe
    report = Report([9, 7, 6, 2, 1])
    assert not is_safe_with_problem_dampener(report)

    # safe by removing 3
    report = Report([1, 3, 2, 4, 5])
    assert is_safe_with_problem_dampener(report)

    # safe by removing 4
    report = Report([8, 6, 4, 4, 1])
    assert is_safe_with_problem_dampener(report)

    # safe
    report = Report([1, 3, 6, 7, 9])
    assert is_safe_with_problem_dampener(report)
