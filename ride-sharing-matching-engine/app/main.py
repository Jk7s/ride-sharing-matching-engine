import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from app.engine import RideSharingEngine
from app.grid import CityGrid, shortest_path
from app.models import Driver, Rider


# ---------- INPUT ----------

def get_pos(text):
    return [
        tuple(map(int, x.split(",")))
        for x in text.splitlines()
        if x.strip()
    ]


def get_drivers(text):
    return [
        Driver(f"D{i}", p)
        for i, p in enumerate(get_pos(text), 1)
    ]


def get_riders(text):
    riders = []

    for i, x in enumerate(text.splitlines(), 1):
        if x.strip():
            p, d = x.split(";")
            riders.append(
                Rider(
                    f"R{i}",
                    tuple(map(int, p.split(","))),
                    tuple(map(int, d.split(",")))
                )
            )

    return riders


# ---------- GRID ----------

def draw_grid(grid, drivers, riders, match):

    g = [["⬜"] * grid.cols for _ in range(grid.rows)]

    # Blocked
    for r, c in grid.blocked:
        g[r][c] = "🟥"

    # Rider destinations
    for rider in riders:
        r, c = rider.destination
        g[r][c] = f"🏁{rider.id}"

    # Rider pickups
    for rider in riders:
        r, c = rider.pickup
        g[r][c] = f"🧍{rider.id}"

    # Drivers
    for driver in drivers:
        r, c = driver.position
        g[r][c] = f"🚗{driver.id}"

    # Selected match
    if match:

        driver = next(
            d for d in drivers
            if d.id == match.driver_id
        )

        rider = next(
            r for r in riders
            if r.id == match.rider_id
        )

        # Driver → Rider
        path1 = match.path_to_pickup

        # Rider → Destination
        path2 = shortest_path(
            grid,
            rider.pickup,
            rider.destination
        )

        # Blue path
        for r, c in path1:

            if (r, c) in (
                driver.position,
                rider.pickup,
                rider.destination
            ):
                continue

            g[r][c] = "🔵"

        # Purple path
        for r, c in path2:

            if (r, c) in (
                driver.position,
                rider.pickup,
                rider.destination
            ):
                continue

            g[r][c] = "🟣"

    return g
# ---------- PAGE ----------

st.set_page_config(
    page_title="Ride-Sharing Matching Engine",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Ride-Sharing Matching Engine")

# ---------- SIDEBAR ----------

with st.sidebar:

    rows = st.number_input("Rows", 3, 30, 10)
    cols = st.number_input("Columns", 3, 30, 10)

    blocked = st.text_area(
        "Blocked cells",
        "2,2\n2,3\n5,5\n6,5"
    )

    driver_text = st.text_area(
        "Drivers",
        "0,0\n4,1\n8,8"
    )

    rider_text = st.text_area(
        "Riders",
        "1,7;8,1\n6,6;0,9\n9,2;3,8"
    )

    max_wait = st.slider(
        "Maximum driver waiting distance",
        1, 50, 20
    )

    find = st.button(
        "🚀 Find Matches",
        use_container_width=True
    )


# ---------- DATA ----------

grid = CityGrid(
    rows,
    cols,
    get_pos(blocked)
)

drivers = get_drivers(driver_text)
riders = get_riders(rider_text)

engine = RideSharingEngine(
    grid,
    drivers,
    riders
)


# ---------- FIND MATCHES ----------

if find:

    st.session_state.matches = engine.match(
        max_wait
    )

    st.session_state.selected = 0

    st.session_state.simulation = asyncio.run(
        engine.simulate()
    )


# ---------- RESULTS ----------

if "matches" in st.session_state:

    matches = st.session_state.matches

    left, right = st.columns([1.2, 1])


    # ---------- GRID ----------

    with left:

        st.subheader("🗺️ City Grid")

        match = (
            matches[st.session_state.selected]
            if matches
            else None
        )

        st.dataframe(
            draw_grid(
                grid,
                drivers,
                riders,
                match
            ),
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "🚗 Driver   🧍 Rider   🏁 Destination   🟥 Blocked"
        )

        st.caption(
            "🔵 Driver → Rider    🟣 Rider → Destination"
        )


    # ---------- MATCHES ----------

    with right:

        st.subheader("🤝 Match Results")

        for i, m in enumerate(matches):

            if st.button(
                f"{m.driver_id} → {m.rider_id} | "
                f"Wait: {m.wait_distance} | "
                f"Detour: {m.detour_distance} | "
                f"Cost: {m.total_cost}",
                key=i,
                use_container_width=True
            ):

                st.session_state.selected = i
                st.rerun()


        st.metric(
            "Matched riders",
            len(matches)
        )

        st.metric(
            "Total waiting distance",
            sum(m.wait_distance for m in matches)
        )

        st.metric(
            "Total detour distance",
            sum(m.detour_distance for m in matches)
        )

else:

    st.info(
        "Click 🚀 Find Matches to start."
    )