from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/f534dbd0fc4d9de638b805d27939d6f4/raw/5b3a7df617cb5aef05d61c71a9ffc49c7b6f648c/aoc_2025_day2_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def raw_to_ranges(raw: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for range_str in raw.split(","):
        ends: list[int] = [int(end) for end in range_str.split("-")]
        ranges.append((ends[0], ends[1]))

    return ranges


def is_invalid_id_part1(id: int) -> bool:
    chars: str = str(id)
    charlen: int = len(chars)
    middle: int = charlen // 2

    if charlen == 1:
        return False
    elif chars[:middle] == chars[middle:]:
        return True

    return False


def sum_invalid_ids_part1(ranges: list[tuple[int, int]]) -> int:
    sum: int = 0
    for ends in ranges:
        for id in range(ends[0], ends[1] + 1):
            if is_invalid_id_part1(id):
                sum += id

    return sum


def is_invalid_id_part2(id: int) -> bool:
    chars: str = str(id)
    charlen: int = len(chars)
    divisors: list[int] = []
    for i in range(1, charlen):
        if charlen % (i) == 0:
            divisors.append(i)

    for divisor in divisors:
        parts: list[str] = [chars[i : i + divisor] for i in range(0, charlen, divisor)]
        if all(part == parts[0] for part in parts):
            return True

    return False


def sum_invalid_ids_part2(ranges: list[tuple[int, int]]) -> int:
    sum: int = 0
    for ends in ranges:
        for id in range(ends[0], ends[1] + 1):
            if is_invalid_id_part2(id):
                sum += id

    return sum


def solve_part1(raw: str) -> int:
    ranges: list[tuple[int, int]] = raw_to_ranges(raw)
    return sum_invalid_ids_part1(ranges)


def solve_part2(raw: str) -> int:
    ranges: list[tuple[int, int]] = raw_to_ranges(raw)
    return sum_invalid_ids_part2(ranges)


def main() -> None:
    print("AoC 2025 Day 2")

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
