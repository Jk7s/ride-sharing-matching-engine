# Algorithms

## 1. City Grid
The city is represented as a grid. Each open cell is a graph node and adjacent open cells are connected.

## 2. Shortest Path
BFS is used because every grid movement has equal cost.

Time complexity: O(V + E), where V is the number of open cells and E is the number of connections.

## 3. Greedy Bipartite Matching
Every available driver is paired with every rider that can be reached. A cost is calculated:

`cost = waiting distance + detour distance`

Pairs are sorted by cost. The lowest-cost feasible pair is selected first, and its driver and rider are removed from future matching.

This is a greedy heuristic, so it is fast but does not guarantee the globally optimal assignment.

## 4. Detour
For a driver D and rider R:

`detour = distance(D, pickup) + distance(pickup, destination) - distance(D, destination)`

Negative values are converted to zero.
