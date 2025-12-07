from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/6aa38b0269c1bc9363ad3d4ff7a7042b/raw/89d72f8488e1278f0fc5c6fc7f7130977a5e8fc5/aoc_2025_day7_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def solve_part1(raw: str) -> int:
    lines = raw.splitlines()

    curr_beam: set[int] = {lines[0].index("S")}
    splits: int = 0
    for line in lines[1:]:
        next_beam: set[int] = set()
        col_len = len(line)
        for col in range(col_len):
            char = line[col]
            if col in curr_beam:
                if char == ".":
                    next_beam.add(col)
                elif char == "^":
                    splits += 1
                    next_beam.add(col - 1)
                    next_beam.add(col + 1)
        curr_beam = next_beam

    return splits


def count_timelines(
    lines: list[str], row: int, col: int, dp: dict[tuple[int, int], int] = {}
) -> int:
    step: tuple[int, int] = (row, col)
    if step in dp:
        return dp[step]

    line_len: int = len(lines)
    col_len: int = len(lines[0])
    if row >= line_len:
        return 1
    if col < 0 or col >= col_len:
        return 1

    char = lines[row][col]

    if char == "^":
        dp[step] = count_timelines(lines, row + 1, col - 1, dp)
        dp[step] += count_timelines(lines, row + 1, col + 1, dp)
    elif char in (".", "S"):
        dp[step] = count_timelines(lines, row + 1, col, dp)

    return dp[step]


def solve_part2(raw: str) -> int:
    lines = raw.splitlines()

    col: int = lines[0].index("S")
    return count_timelines(lines, 0, col)


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
