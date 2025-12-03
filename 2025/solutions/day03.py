from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
        987654321111111
        811111111111119
        234234234234278
        818181911112111
        """.strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/69b4c935a637cda8a917ea68950ec07c/raw/374b150632a290c5c00771562d9a9b05f7e54e6a/aoc_2025_day3_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def get_banks(raw: str) -> list[str]:
    return [bank.strip() for bank in raw.split("\n")]


def calculate_max_bank_joltage(bank: str) -> int:
    max_idx: int = 0
    bank_size: int = len(bank)

    # Skipping last index on purpose
    for i in range(0, bank_size - 1):
        if bank[i] > bank[max_idx]:
            max_idx = i

    tens: str = bank[max_idx]

    joltage: int = 0
    for i in range(max_idx + 1, bank_size):
        ones: str = bank[i]
        curr: int = int(tens + ones)

        if curr > joltage:
            joltage = curr

    return joltage


def calculate_total_banks_joltage(banks: list) -> int:
    total: int = 0
    for bank in banks:
        total += calculate_max_bank_joltage(bank)

    return total


def find_max_in_range(bank: str, start: int, end: int) -> int:
    max_idx: int = start

    for i in range(start, end):
        if bank[i] > bank[max_idx]:
            max_idx = i

    return max_idx


def calculate_max_bank_joltage_digits(bank: str, digits: int = 2) -> int:
    bank_size: int = len(bank)

    curr_idx: int = -1
    joltage: str = ""
    remaining: int = digits - 1

    while remaining >= 0:
        curr_idx = find_max_in_range(bank, curr_idx + 1, bank_size - remaining)
        joltage += bank[curr_idx]

        # msg = f"bank: {bank}, bank_size: {bank_size}, curr_idx: {curr_idx}, joltage: {joltage}"
        # print(msg)

        remaining -= 1

    return int(joltage)


def calculate_total_banks_joltage_digits(banks: list, digits: int = 2) -> int:
    total: int = 0
    for bank in banks:
        total += calculate_max_bank_joltage_digits(bank, digits)

    return total


def solve_part1(raw: str) -> int:
    banks: list[str] = get_banks(raw)
    return calculate_total_banks_joltage(banks)


def solve_part2(raw: str) -> int:
    banks: list[str] = get_banks(raw)
    return calculate_total_banks_joltage_digits(banks, 12)


def main() -> None:
    print("AoC 2025 Day 3")

    demo_joltage: int = solve_part1(get_demo_input())
    print(f"Part 1 Demo: {demo_joltage}")

    real_joltage: int = solve_part1(get_raw_input())
    print(f"Part 1 Real: {real_joltage}")

    print()

    demo_joltage_12: int = solve_part2(get_demo_input())
    print(f"Part 2 Demo: {demo_joltage_12}")

    real_joltage_12: int = solve_part2(get_raw_input())
    print(f"Part 2 Real: {real_joltage_12}")


if __name__ == "__main__":
    main()
