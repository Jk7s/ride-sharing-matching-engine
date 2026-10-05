import asyncio
from dataclasses import dataclass

from .grid import CityGrid
from .matching import greedy_match
from .models import Driver, Match, Rider
from .simulation import simulate_requests


@dataclass
class RideSharingEngine:
    grid: CityGrid
    drivers: list[Driver]
    riders: list[Rider]

    def match(self, max_wait: int) -> list[Match]:
        return greedy_match(self.grid, self.drivers, self.riders, max_wait)

    async def simulate(self) -> list[str]:
        return await simulate_requests(self.riders)


def run_async_simulation(riders: list[Rider]) -> list[str]:
    return asyncio.run(simulate_requests(riders))
