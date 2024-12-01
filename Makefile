.DEFAULT_GOAL := help

NAME = aoc2024

# ------------------------------------
#  Setup
# ------------------------------------

.PHONY: create-day
create-day:
	mkdir day${DAY}/
	touch day${DAY}/input.txt
	touch day${DAY}/test.txt
	touch day${DAY}/solution.py
	touch day${DAY}/test_solution.py


# ------------------------------------
#  Run
# ------------------------------------

.PHONY: test
test:
	@[ "${DAY}" ] && pytest day${DAY}/ || pytest

.PHONY: lint
lint:
	ruff format
	ruff check --fix
	mypy .

# Implements this pattern for autodocumenting Makefiles:
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
#
# Picks up all comments that start with a ## and are at the end of a target definition line.
.PHONY: help
help:  ## Display command usage
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
