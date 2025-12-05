from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/017a5b82f7502993f3e01a9ea35ba7ab/raw/486becf755480c55885872671ba69a7a697caa8c/aoc_2025_day5_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def parse_fresh_ranges(raw_ranges: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    for line in raw_ranges.splitlines():
        ends: list[int] = [int(end.strip()) for end in line.split("-")]
        ranges.append((ends[0], ends[1]))

    return ranges


def parse_ing(raw_ing: str) -> list[int]:
    return [int(ing.strip()) for ing in raw_ing.splitlines()]


def parse_raw(raw: str) -> tuple[list[tuple[int, int]], list[int]]:
    parts: list[str] = raw.split("\n\n")
    ranges: list[tuple[int, int]] = parse_fresh_ranges(parts[0])
    ings: list[int] = parse_ing(parts[1])

    return (ranges, ings)


def count_fresh_ings(ranges: list[tuple[int, int]], ings: list[int]) -> int:
    total: int = 0
    for ing in ings:
        for ends in ranges:
            if ing >= ends[0] and ing <= ends[1]:
                total += 1
                break

    return total


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    sortedranges: list[tuple[int, int]] = ranges.copy()
    sortedranges.sort(key=lambda x: x[0])

    rangeslen: int = len(sortedranges)

    currmin: int = sortedranges[0][0]
    currmax: int = sortedranges[0][1]

    for i in range(1, rangeslen):
        start, end = sortedranges[i]
        if start > currmax:
            merged.append((currmin, currmax))
            currmin, currmax = start, end
            continue
        if end > currmax:
            currmax = end

    merged.append((currmin, currmax))

    return merged


def count_total_fresh(ranges: list[tuple[int, int]]) -> int:
    return sum((end - start) + 1 for start, end in ranges)


def solve_part1(raw: str) -> int:
    ranges, ings = parse_raw(raw)
    return count_fresh_ings(ranges, ings)


def solve_part2(raw: str) -> int:
    ranges, _ = parse_raw(raw)
    merged = merge_ranges(ranges)

    return count_total_fresh(merged)


def main() -> None:
    print("AoC 2025 Day 5")

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
