import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.grid import CityGrid, path_distance, shortest_path


def test_shortest_path():
    grid = CityGrid(3, 3, {(1, 1)})
    path = shortest_path(grid, (0, 0), (2, 2))
    assert path
    assert path_distance(path) == 4


def test_blocked_goal_has_no_path():
    grid = CityGrid(3, 3, {(2, 2)})
    assert shortest_path(grid, (0, 0), (2, 2)) == []
