from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/83536a46319d699e15b8275244f93fc7/raw/b1d47aceee3b7fce702dc6a8a144b8a22f199e01/aoc_2025_day4_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def print_mat(mat: list[list[int]]) -> None:
    for row in mat:
        print(row)


def debug_mat(mat: list[list[int]], free: list[tuple[int, int]]) -> None:
    rows_len: int = len(mat)
    cols_len: int = len(mat[0])

    print()
    for row in range(rows_len):
        line: str = ""
        for col in range(cols_len):
            if (row, col) in free:
                line += "x"
            elif mat[row][col] == 1:
                line += "@"
            else:
                line += "."
        print(line)
    print()


def raw_to_mat(raw: str) -> list[list[int]]:
    rows: list[str] = [row.strip() for row in raw.split("\n")]
    rows_len: int = len(rows)
    cols_len: int = len(rows[0])

    mat: list[list[int]] = []

    for row in range(rows_len):
        mat.append([])
        for col in range(cols_len):
            char: str = rows[row][col]
            num: int = 1 if char == "@" else 0
            mat[row].append(num)

    return mat


def get_adjacent_positions(
    mat: list[list[int]], row: int, col: int
) -> list[tuple[int, int]]:
    rows: int = len(mat)
    cols: int = len(mat[row])
    positions: list[tuple[int, int]] = []

    for i in range(3):
        row_idx: int = row - (i - 1)
        if row_idx < 0 or row_idx >= rows:
            continue
        for j in range(3):
            col_idx: int = col - (j - 1)
            if col_idx < 0 or col_idx >= cols:
                continue
            if row_idx == row and col_idx == col:
                continue
            positions.append((row_idx, col_idx))

    return positions


def count_positions(mat: list[list[int]], positions: list[tuple[int, int]]) -> int:
    total: int = 0
    for pos in positions:
        total += mat[pos[0]][pos[1]]

    return total


def count_adjacent_rolls(mat: list[list[int]], row: int, col: int) -> int:
    positions: list[tuple[int, int]] = get_adjacent_positions(mat, row, col)
    return count_positions(mat, positions)


def sum_moveable_rolls(
    mat: list[list[int]], max_adjacent: int = 4
) -> tuple[int, list[tuple[int, int]]]:
    rows_len: int = len(mat)
    cols_len: int = len(mat[0])

    free: list[tuple[int, int]] = []
    total: int = 0
    for row in range(rows_len):
        for col in range(cols_len):
            if mat[row][col] == 0:
                continue

            adjacent: int = count_adjacent_rolls(mat, row, col)
            if adjacent < max_adjacent:
                free.append((row, col))
                total += 1

    # debug_mat(mat, free)
    return (total, free)


def solve_part1(raw: str) -> int:
    mat: list[list[int]] = raw_to_mat(raw)
    movable, _ = sum_moveable_rolls(mat, 4)
    return movable


def solve_part2(raw: str) -> int:
    mat: list[list[int]] = raw_to_mat(raw)
    total: int = 0

    movable: int = 1
    free_pos: list[tuple[int, int]] = []

    while movable > 0:
        for pos in free_pos:
            mat[pos[0]][pos[1]] = 0
            total += 1

        movable, free_pos = sum_moveable_rolls(mat, 4)

    return total


def main() -> None:
    print("AoC 2025 Day 4")

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
