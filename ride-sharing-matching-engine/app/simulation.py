import asyncio
from dataclasses import dataclass

from .models import Driver, Rider


@dataclass(frozen=True)
class RideRequest:
    rider: Rider


async def simulate_request(request: RideRequest, delay: float = 0.15) -> str:
    """Simulate an I/O-like ride request arriving asynchronously."""
    await asyncio.sleep(delay)
    return f"Request received: {request.rider.id}"


async def simulate_requests(riders: list[Rider]) -> list[str]:
    requests = [RideRequest(rider) for rider in riders]
    return await asyncio.gather(*(simulate_request(req) for req in requests))
