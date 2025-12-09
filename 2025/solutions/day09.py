from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/28658b867de487fc65affc2b49487664/raw/de664c9da40d68744066912c2f6094f06ae13ba3/aoc_2025_day9_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def parse_pos(raw: str) -> list[tuple[int, int]]:
    lines: list[str] = raw.splitlines()
    positions: list[list[str]] = [line.split(",") for line in lines]
    return [(int(pos[0]), int(pos[1])) for pos in positions]


def calc_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    height: int = abs(a[0] - b[0]) + 1
    width: int = abs(a[1] - b[1]) + 1

    return height * width


def max_area(positions: list[tuple[int, int]]) -> int:
    pos_len: int = len(positions)

    area: int = 0
    for i in range(pos_len):
        a: tuple[int, int] = positions[i]
        for j in range(i + 1, pos_len):
            b: tuple[int, int] = positions[j]
            curr: int = calc_area(a, b)
            # print(f"a: {a}, b:{b}, curr: {curr}, area: {area}")
            area = max(area, curr)

    return area


def find_walls(
    positions: list[tuple[int, int]],
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    walls: list[tuple[tuple[int, int], tuple[int, int]]] = []
    pos_len: int = len(positions)

    for i in range(pos_len):
        a: tuple[int, int] = positions[i]
        b: tuple[int, int] = positions[(i + 1) % pos_len]

        walls.append((a, b))

    return walls


def is_rect_intersecting_wall(
    a: tuple[int, int],
    b: tuple[int, int],
    walls: list[tuple[tuple[int, int], tuple[int, int]]],
) -> bool:
    x_min: int = min(a[0], b[0])
    x_max: int = max(a[0], b[0])
    y_min: int = min(a[1], b[1])
    y_max: int = max(a[1], b[1])

    for w1, w2 in walls:
        wx_min: int = min(w1[0], w2[0])
        wx_max: int = max(w1[0], w2[0])
        wy_min: int = min(w1[1], w2[1])
        wy_max: int = max(w1[1], w2[1])

        if wx_min == wx_max:
            wall_x: int = wx_min
            within_x: bool = x_min < wall_x < x_max
            crashes_y: bool = wy_min < y_max and y_min < wy_max

            if within_x and crashes_y:
                return True

        else:
            wall_y: int = wy_min
            within_y: bool = y_min < wall_y < y_max
            crashes_x: bool = wx_min < x_max and x_min < wx_max

            if crashes_x and within_y:
                return True
    return False


def max_area_within_walls(
    positions: list[tuple[int, int]],
    walls: list[tuple[tuple[int, int], tuple[int, int]]],
) -> int:
    pos_len: int = len(positions)

    area: int = 0
    for i in range(pos_len):
        a: tuple[int, int] = positions[i]
        for j in range(i + 1, pos_len):
            b: tuple[int, int] = positions[j]
            if not is_rect_intersecting_wall(a, b, walls):
                curr: int = calc_area(a, b)
                # print(f"a: {a}, b:{b}, curr: {curr}, area: {area}")
                area = max(area, curr)

    return area


def solve_part1(raw: str) -> int:
    positions: list[tuple[int, int]] = parse_pos(raw)

    return max_area(positions)


def solve_part2(raw: str) -> int:
    positions: list[tuple[int, int]] = parse_pos(raw)
    walls: list[tuple[tuple[int, int], tuple[int, int]]] = find_walls(positions)

    return max_area_within_walls(positions, walls)


def main() -> None:
    print("AoC 2025 Day 8")

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
