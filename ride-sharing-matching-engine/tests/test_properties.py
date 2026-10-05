import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hypothesis import given, strategies as st

from app.grid import CityGrid, shortest_path


@given(st.integers(min_value=2, max_value=10))
def test_open_adjacent_cells_are_reachable(size):
    grid = CityGrid(size, size)
    path = shortest_path(grid, (0, 0), (0, 1))
    assert path == [(0, 0), (0, 1)]
