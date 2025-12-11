import re

from utils.input import get_input_from_gist

MAX_NUM = 100


def get_demo_input() -> str:
    return """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """.strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/0a8e6599e24cd6bb401e7228ae7243f9/raw/2c54b1de9940653eb4f76a6ad746eae6503633fe/aoc_2025_day1_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def split_moves(moves_raw: str) -> list[str]:
    return [move.strip() for move in moves_raw.split("\n") if move.strip() != ""]


def convert_to_operation(move: str) -> int:
    matches = re.match(r"^([RL]{1})(\d+)", move)
    if matches is None:
        print(f"Invalid move: {move}")
        return 0
    dir = matches.group(1)
    dist = 0

    try:
        dist = int(matches.group(2))
    except ValueError:
        print(f"Distance is not int. Move: {move}")
        return 0

    if dir == "L":
        return -dist
    elif dir == "R":
        return dist

    return 0


def list_to_ops(moves: list[str]) -> list[int]:
    ops = []
    for move in moves:
        ops.append(convert_to_operation(move))
    return ops


def calc_pos(curr_pos: int, op: int) -> int:
    return (curr_pos + op) % MAX_NUM


def count_zeros(ops: list[int], starting_pos: int = 50) -> int:
    count: int = 0
    curr_pos: int = starting_pos

    for op in ops:
        curr_pos = calc_pos(curr_pos, op)
        if curr_pos == 0:
            count += 1
    return count


def count_zeros_part2(ops: list[int], starting_pos: int = 50) -> int:
    count: int = 0
    curr_pos: int = starting_pos

    for op in ops:
        cycles: int = abs(op) // MAX_NUM
        remainder: int = abs(op) % MAX_NUM

        count += cycles

        if op < 0:
            tmp_pos = curr_pos - remainder
            if tmp_pos <= 0 and curr_pos != 0:
                count += 1
        else:
            tmp_pos = curr_pos + remainder
            if tmp_pos >= MAX_NUM:
                count += 1

        curr_pos = tmp_pos % MAX_NUM

    return count


def solve_part1(raw: str) -> int:
    moves = split_moves(raw)
    ops = list_to_ops(moves)
    return count_zeros(ops)


def solve_part2(raw: str) -> int:
    moves = split_moves(raw)
    ops = list_to_ops(moves)
    return count_zeros_part2(ops)


def main() -> None:
    print("AoC 2025 Day 1")

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
