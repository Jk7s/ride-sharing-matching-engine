# 🚗 Ride-Sharing Matching Engine

An interactive Python project that matches riders with nearby drivers on a simulated city grid.

## Main techniques

- Graph representation of a city grid
- BFS shortest-path search
- Greedy bipartite matching
- Object-oriented design
- Functional-style pure functions and comprehensions
- Asyncio request simulation
- Pytest
- Hypothesis property-based testing
- Coverage
- Mypy
- Ruff
- Black
- Docker
- GitHub Actions

## Run locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app/main.py
```

Then open the local Streamlit URL shown in the terminal.

## Input format

Drivers:

```text
0,0
4,1
8,8
```

Riders:

```text
1,7;8,1
6,6;0,9
9,2;3,8
```

Each rider line is:

`pickup;destination`

## Test

```bash
pytest --cov=app
```

## Quality checks

```bash
mypy app
ruff check .
black --check .
```

## Docker

```bash
docker build -t ride-sharing-engine .
docker run -p 8501:8501 ride-sharing-engine
```

## Project flow

Real-world problem
→ computational thinking
→ graph abstraction
→ shortest path
→ greedy matching
→ Python/OOP
→ async simulation
→ testing
→ quality checks
→ Docker/CI
→ live demonstration
