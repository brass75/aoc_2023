import time
from collections import deque
from collections.abc import Generator, Iterable
from typing import Any

from aoc_lib import GridBase

INPUT = open('data/day16.txt').read()

TEST_INPUT = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


class Tile:
    def __init__(self, value: str):
        self._value = value
        self._energized = False

    @property
    def energized(self) -> bool:
        return self._energized

    @energized.setter
    def energized(self, value: bool):
        self._energized = value

    @property
    def type(self) -> str:
        return self._value

    def impact(self, direction: str, energize: int = 0) -> str:
        if energize:
            self.energized = energize > 0
        match self.type:
            case '.':
                return direction
            case '/':
                match direction:
                    case 'L':
                        return 'D'
                    case 'R':
                        return 'U'
                    case 'D':
                        return 'L'
                    case 'U':
                        return 'R'
            case '\\':
                match direction:
                    case 'L':
                        return 'U'
                    case 'R':
                        return 'D'
                    case 'D':
                        return 'R'
                    case 'U':
                        return 'L'
            case '|':
                match direction:
                    case 'D' | 'U':
                        return direction
                    case 'R' | 'L':
                        return 'DU'
            case '-':
                match direction:
                    case 'D' | 'U':
                        return 'LR'
                    case 'R' | 'L':
                        return direction

    def __str__(self):
        return '#' if self.energized else self.type


class Queue:
    def __init__(self, seed: Iterable = None):
        self._q = deque()
        if seed:
            self._q.extend(seed)

    def add(self, value: Any):
        self._q.append(value)

    def next(self) -> Any:
        return self._q.popleft()

    def __next__(self) -> Any:
        return self._q.popleft()

    def __bool__(self):
        return bool(self._q)


class Grid(GridBase):
    def __init__(self, input_: str, starting: tuple[int, int] = (0, 0), direction: str = 'R'):
        super().__init__(input_, Tile)
        self._q = Queue([(starting, direction)])
        self._hash = hash((starting, direction))
        self._energize = 1

    def __hash__(self):
        return self._hash

    def traverse(self):
        seen = set()
        while self._q:
            if (nav := self._q.next()) in seen or (nav[0] not in self):
                continue
            seen.add(nav)
            (x, y), direction = nav
            tile = self[(x, y)]
            for d in tile.impact(direction, self._energize):
                match d:
                    case 'D':
                        self._q.add(((x, y + 1), d))
                    case 'U':
                        self._q.add(((x, y - 1), d))
                    case 'L':
                        self._q.add(((x - 1, y), d))
                    case 'R':
                        self._q.add(((x + 1, y), d))

    @property
    def energized(self):
        return sum(t.energized for t in self.values)


def get_starts(height: int, width: int) -> Generator[tuple[int, int], str]:
    for x in range(width):
        yield (x, 0), 'D'
        yield (x, height - 1), 'U'
    for y in range(height):
        yield (0, y), 'R'
        yield (width - 1, y), 'L'


def solve_grid(grid: Grid) -> int:
    grid.traverse()
    return grid.energized


def solve(input_: str, starts: bool = False) -> int:
    if not starts:
        return solve_grid(Grid(input_))
    lines = input_.splitlines()
    return max(
        map(
            solve_grid,
            (Grid(input_, *starting_values) for starting_values in get_starts(len(lines), len(lines[0]))),
        )
    )


if __name__ == '__main__':
    expected_1 = [(46, [])]
    for idx, e in enumerate(expected_1):
        e_total, e_params = e
        start = time.time()
        assert (total := solve(TEST_INPUT, *e_params)) == e_total, f'Test {1} for part 1 failed! {total=} {e_total=}'
        print(f'Part 1: [test {idx}] {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
    start = time.time()
    total = solve(INPUT)
    print(f'Part 1: {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')

    expected_2 = [(51, [True])]
    if expected_2:
        for idx, e in enumerate(expected_2):
            e_total, e_params = e
            start = time.time()
            assert (
                total := solve(TEST_INPUT, *e_params)
            ) == e_total, f'Test {1} for part 2 failed! {total=} {e_total=}'
            print(f'Part 2: [test {idx}] {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
        start = time.time()
        total = solve(INPUT, True)
        print(f'Part 2: {total} [elapsed time: {(time.time() - start) * 1000:.5f}ms]')
