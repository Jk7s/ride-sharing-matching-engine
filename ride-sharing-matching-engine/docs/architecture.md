# Architecture

```text
Streamlit UI
     |
     v
RideSharingEngine
     |
     +---- CityGrid
     |
     +---- Shortest Path (BFS)
     |
     +---- Matching Engine (Greedy)
     |
     +---- Async Request Simulation
     |
     v
Results and Performance Metrics
```

The project separates models, algorithms, simulation and UI so the core logic can be tested without the UI.
