import math
from collections import defaultdict

from utils.input import get_input_from_gist


def get_demo_input() -> str:
    return """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()


def get_raw_input() -> str:
    INPUT_GIST_URL: str = "https://gist.githubusercontent.com/oryanmoshe/7390ea45eae30206d20215ed92dd0859/raw/e560f356911984291755eb28c08c17845ecc491e/aoc_2025_day8_input.txt"
    return get_input_from_gist(INPUT_GIST_URL)


def parse_pos(raw: str) -> list[tuple[int, int, int]]:
    lines: list[str] = raw.splitlines()
    positions: list[list[str]] = [line.split(",") for line in lines]
    return [(int(pos[0]), int(pos[1]), int(pos[2])) for pos in positions]


def calc_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    unrooted: int = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
    return math.sqrt(unrooted)


def get_connections(
    positions: list[tuple[int, int, int]],
) -> dict[tuple[tuple[int, int, int], tuple[int, int, int]], float]:
    pos_len: int = len(positions)

    distances: dict[tuple[tuple[int, int, int], tuple[int, int, int]], float] = {}

    for i in range(pos_len):
        a = positions[i]
        for j in range(i + 1, pos_len):
            b = positions[j]
            distances[a, b] = calc_distance(a, b)

    return distances


def sort_connections(
    distances: dict[tuple[tuple[int, int, int], tuple[int, int, int]], float],
) -> list[tuple[tuple[tuple[int, int, int], tuple[int, int, int]], float]]:
    ret = sorted(distances.items(), key=lambda x: x[1])
    return ret


def get_top_connections(
    connections: list[tuple[tuple[tuple[int, int, int], tuple[int, int, int]], float]],
    max_boxes: int = 10,
) -> dict[tuple[int, int, int], list[tuple[int, int, int]]]:
    mapping: dict[tuple[int, int, int], list[tuple[int, int, int]]] = defaultdict(list)
    for i in range(max_boxes):
        boxes, distance = connections[i]
        a, b = boxes
        mapping[a].append(b)
        mapping[b].append(a)

    return mapping


def count_circuits(
    mapping: dict[tuple[int, int, int], list[tuple[int, int, int]]], top: int = 3
) -> int:
    visited: set[tuple[int, int, int]] = set()
    proc: list[tuple[int, int, int]] = []

    sizes: list[int] = []

    for box in mapping.keys():
        if box not in visited:
            count: int = 0
            proc.append(box)
            while len(proc) > 0:
                b = proc.pop(0)
                if b not in visited:
                    visited.add(b)
                    count += 1
                    proc.extend(mapping[b])

            sizes.append(count)

    sizes.sort(reverse=True)
    total: int = 1
    for s in sizes[:top]:
        total *= s

    return total


def merge_circuits(
    pairs: list[tuple[tuple[tuple[int, int, int], tuple[int, int, int]], float]],
    coords: dict[tuple[int, int, int], int],
) -> int:
    boxes_len: int = len(coords.keys())
    groups: list[int] = [i for i in range(boxes_len)]
    remaining: int = boxes_len

    for pair, _ in pairs:
        a, b = pair
        id_a = coords[a]
        id_b = coords[b]

        group_a = groups[id_a]
        group_b = groups[id_b]
        if group_a != group_b:
            for i in range(len(groups)):
                if groups[i] == group_b:
                    groups[i] = group_a
            remaining -= 1

        if remaining == 1:
            return a[0] * b[0]

    return 0


def solve_part1(raw: str, max_boxes: int, top_circuits: int) -> int:
    positions: list[tuple[int, int, int]] = parse_pos(raw)
    distances = get_connections(positions)
    sorted_conns = sort_connections(distances)
    top_connections = get_top_connections(sorted_conns, max_boxes)

    return count_circuits(top_connections, top_circuits)


def solve_part2(raw: str) -> int:
    positions: list[tuple[int, int, int]] = parse_pos(raw)
    coords: dict[tuple[int, int, int], int] = {
        positions[i]: i for i in range(len(positions))
    }
    distances = get_connections(positions)
    sorted_conns = sort_connections(distances)

    return merge_circuits(sorted_conns, coords)


def main() -> None:
    print("AoC 2025 Day 8")

    demo_result: int = solve_part1(get_demo_input(), 10, 3)
    print(f"Part 1 Demo: {demo_result}")

    real_result: int = solve_part1(get_raw_input(), 1000, 3)
    print(f"Part 1 Real: {real_result}")

    print()

    demo_result_2: int = solve_part2(get_demo_input())
    print(f"Part 2 Demo: {demo_result_2}")

    real_result_2: int = solve_part2(get_raw_input())
    print(f"Part 2 Real: {real_result_2}")


if __name__ == "__main__":
    main()
