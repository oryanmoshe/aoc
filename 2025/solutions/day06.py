import re
from io import UnsupportedOperation

from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/a9470ce8b7bfbb8ed06eb70c445a4a75/raw/2358d289a1c3d368d0878bcda761ee5b4e0b5bf9/aoc_2025_day6_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def parse_nums(line: str) -> list[int]:
    matches = re.findall(r"(\d+)\s*", line)
    return [int(num.strip()) for num in matches]


def run_op(n1: int, n2: int, op: str) -> int:
    if op == "*":
        return n1 * n2
    # elif op == "-":
    # return n1 - n2
    elif op == "+":
        return n1 + n2
    # elif op == "-":
    # return n1 // n2
    else:
        raise UnsupportedOperation()


def calc_problem(numbers: list[int], op: str) -> int:
    numlen: int = len(numbers)
    total: int = numbers[0]

    for i in range(1, numlen):
        total = run_op(total, numbers[i], op)

    return total


def parse_problems(raw: str) -> list[tuple[list[int], str]]:
    lines: list[str] = raw.splitlines()
    line_len: int = len(lines)

    ops: list[str] = re.findall(r"([+\-*/])\s*", lines[-1])
    ops = [op.strip() for op in ops if op.strip() != ""]

    numbers: list[list[int]] = [[] for _ in range(len(ops))]

    for i in range(line_len - 1):
        nums: list[int] = parse_nums(lines[i])
        for j in range(len(nums)):
            numbers[j].append(nums[j])

    problems: list[tuple[list[int], str]] = []

    for i in range(len(numbers)):
        problems.append((numbers[i], ops[i]))

    return problems


def split_problems(raw: str) -> list[list[int]]:
    lines: list[str] = raw.splitlines()
    line_len = len(lines)
    col_len = len(lines[-1])

    problems: list[list[int]] = [[]]

    curr = 0
    last: str = lines[-1]
    for j in range(col_len - 1, -1, -1):
        tot = ""
        for i in range(line_len - 2, -1, -1):
            char = lines[i][j]
            tot = char + tot
        if tot.strip() != "":
            problems[curr].append(int(tot.strip()))

        if last[j] != " ":
            curr += 1
            problems.append([])

    return problems


def parse_problems_part2(raw: str) -> list[tuple[list[int], str]]:
    lines: list[str] = raw.splitlines()

    ops: list[str] = re.findall(r"([+\-*/])\s*", lines[-1])
    ops = [op.strip() for op in ops if op.strip() != ""]
    ops.reverse()

    numbers: list[list[int]] = split_problems(raw)

    problems: list[tuple[list[int], str]] = []
    for i in range(len(numbers)):
        if len(numbers[i]) > 0:
            problems.append((numbers[i], ops[i]))
    return problems


def solve_part1(raw: str) -> int:
    problems: list[tuple[list[int], str]] = parse_problems(raw)
    total: int = 0
    for numbers, op in problems:
        total += calc_problem(numbers, op)
    return total


def solve_part2(raw: str) -> int:
    problems: list[tuple[list[int], str]] = parse_problems_part2(raw)
    total: int = 0
    for numbers, op in problems:
        total += calc_problem(numbers, op)
    return total


def main() -> None:
    print("AoC 2025 Day 6")

    demo_result: int = solve_part1(get_demo_input())
    print(f"Part 1 Demo: {demo_result}")

    real_result: int = solve_part1(get_raw_input())
    print(f"Part 1 Real: {real_result}")

    print()

    demo_result_2: int = solve_part2(get_demo_input())
    print(f"Part 2 Demo: {demo_result_2}")

    real_result_2: int = solve_part2(get_raw_input())
    print(f"Part 2 Real: {real_result_2}")


if __name__ == "__main__":
    main()
