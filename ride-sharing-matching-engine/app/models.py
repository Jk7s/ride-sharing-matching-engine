from dataclasses import dataclass
from typing import Tuple

Position = Tuple[int, int]


@dataclass(frozen=True)
class Driver:
    id: str
    position: Position
    available: bool = True


@dataclass(frozen=True)
class Rider:
    id: str
    pickup: Position
    destination: Position


@dataclass(frozen=True)
class Match:
    driver_id: str
    rider_id: str
    wait_distance: int
    detour_distance: int
    total_cost: int
    path_to_pickup: tuple[Position, ...]
