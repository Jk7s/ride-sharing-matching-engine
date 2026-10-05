from collections import deque
from typing import Iterable

from .models import Position


class CityGrid:
    def __init__(self, rows: int, cols: int, blocked: Iterable[Position] = ()) -> None:
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be positive.")
        self.rows = rows
        self.cols = cols
        self.blocked = set(blocked)

        for cell in self.blocked:
            if not self.in_bounds(cell):
                raise ValueError(f"Blocked cell {cell} is outside the grid.")

    def in_bounds(self, position: Position) -> bool:
        r, c = position
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_open(self, position: Position) -> bool:
        return self.in_bounds(position) and position not in self.blocked

    def neighbors(self, position: Position):
        r, c = position
        for nxt in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if self.is_open(nxt):
                yield nxt


def shortest_path(grid: CityGrid, start: Position, goal: Position) -> list[Position]:
    """Return the shortest path using BFS. Empty list means no path."""
    if not grid.is_open(start) or not grid.is_open(goal):
        return []
    if start == goal:
        return [start]

    queue = deque([start])
    parent: dict[Position, Position | None] = {start: None}

    while queue:
        current = queue.popleft()

        for nxt in grid.neighbors(current):
            if nxt in parent:
                continue
            parent[nxt] = current

            if nxt == goal:
                path = [goal]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])  # type: ignore[index]
                return list(reversed(path))

            queue.append(nxt)

    return []


def path_distance(path: list[Position]) -> int:
    return max(0, len(path) - 1)
