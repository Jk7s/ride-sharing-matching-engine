# Complexity

Let:
- V = number of open grid cells
- E = number of grid edges
- D = number of drivers
- R = number of riders

One BFS is O(V + E).

The matching stage may perform several BFS searches for driver-rider combinations, so the simple implementation is approximately O(D * R * (V + E)).

Candidate sorting adds O(K log K), where K is the number of feasible driver-rider pairs.

Space is O(V) for one BFS plus O(K) for candidate matches.
