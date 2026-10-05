import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import asyncio

from app.engine import RideSharingEngine
from app.grid import CityGrid
from app.models import Driver, Rider


def test_async_simulation():
    riders = [
        Rider("R1", (0, 0), (1, 1)),
        Rider("R2", (2, 2), (1, 1)),
    ]
    engine = RideSharingEngine(CityGrid(3, 3), [], riders)
    messages = asyncio.run(engine.simulate())
    assert len(messages) == 2
    assert "R1" in messages[0]
