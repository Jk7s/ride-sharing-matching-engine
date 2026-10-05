from .grid import CityGrid, path_distance, shortest_path
from .models import Driver, Match, Rider


def detour_distance(grid: CityGrid, driver: Driver, rider: Rider) -> int | None:
    direct = shortest_path(grid, driver.position, rider.destination)
    via_pickup = shortest_path(grid, driver.position, rider.pickup)
    rider_trip = shortest_path(grid, rider.pickup, rider.destination)

    if not direct or not via_pickup or not rider_trip:
        return None

    detour = path_distance(via_pickup) + path_distance(rider_trip) - path_distance(direct)
    return max(0, detour)


def build_candidates(
    grid: CityGrid,
    drivers: list[Driver],
    riders: list[Rider],
) -> list[Match]:
    candidates: list[Match] = []

    for driver in drivers:
        if not driver.available:
            continue

        for rider in riders:
            pickup_path = shortest_path(grid, driver.position, rider.pickup)
            detour = detour_distance(grid, driver, rider)

            if not pickup_path or detour is None:
                continue

            wait = path_distance(pickup_path)
            candidates.append(
                Match(
                    driver_id=driver.id,
                    rider_id=rider.id,
                    wait_distance=wait,
                    detour_distance=detour,
                    total_cost=wait + detour,
                    path_to_pickup=tuple(pickup_path),
                )
            )

    return candidates


def greedy_match(
    grid: CityGrid,
    drivers: list[Driver],
    riders: list[Rider],
    max_wait: int,
) -> list[Match]:
    """Greedily choose the lowest-cost feasible driver-rider pairs."""
    candidates = [
        m for m in build_candidates(grid, drivers, riders)
        if m.wait_distance <= max_wait
    ]

    candidates.sort(key=lambda m: (m.total_cost, m.wait_distance, m.driver_id, m.rider_id))

    used_drivers: set[str] = set()
    used_riders: set[str] = set()
    matches: list[Match] = []

    for match in candidates:
        if match.driver_id in used_drivers or match.rider_id in used_riders:
            continue
        matches.append(match)
        used_drivers.add(match.driver_id)
        used_riders.add(match.rider_id)

    return matches
