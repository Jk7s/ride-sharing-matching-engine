import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.grid import CityGrid
from app.matching import greedy_match
from app.models import Driver, Rider


def test_greedy_match():
    grid = CityGrid(5, 5)
    drivers = [Driver("D1", (0, 0)), Driver("D2", (4, 4))]
    riders = [
        Rider("R1", (0, 1), (0, 4)),
        Rider("R2", (4, 3), (4, 0)),
    ]

    matches = greedy_match(grid, drivers, riders, max_wait=10)

    assert len(matches) == 2
    assert {m.driver_id for m in matches} == {"D1", "D2"}
    assert {m.rider_id for m in matches} == {"R1", "R2"}
