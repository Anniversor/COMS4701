# Homework 1
## Part 1 Navigating Bugs
1. a) Partially observable. Although all insects know the map, they don't know the existences or the positions of other insects, so they only know partial information to complete the task. 
b) Stochastic. For every time step, although insects know the map, they don't know the next steps that other insects will make, so the next state of the environment isn't perfectly predictable.
c) Episodic. Because we don't need memory of past actions to determine the next best action of the insects.
d) Static. For each time step, we deal with data source that don't change to make our next step, the data sources don't change frequently over time.
e) Discrete. It has a fixed location and a fixed time step.
f) Multi-agent/single agent. If there are multiple insects, it is multi-agent. If there is only one insect, it is single-agent.

2. a) The insects' locations.
b) The size of the state space should be the number of the squares, which is here 17. We can use the Manhattan distance between the insect and the goal as our non-trivial admissible heuristic.
3. a) The insects' locations, Booleans indicating goals.
b) The size should be the number of the combinations. Suppose there are n squares of the map, the size of the state space should be $(A_{m}^{k})^{2}$. Use the sum of the Manhattan distances between each insect and its goal as the non-trivial admissible heuristic.
4. a) No.
b) The combination of insect' location and the time step it's at.
c) Infinite. We can use the Manhattan distance between the insect and the goal as our non-trivial admissible heuristic.
5. a) It becomes episodic.
b) The insects' locations, the steps it made in the latest time step.
c) Infinite. We can use the Manhattan distance between the insect and the goal as our non-trivial admissible heuristic.
6. a)No.
b)The location of the insect and the time steps it spends in the pesticide squares.
c) Suppose there are $N$ squares in the map, the size of the state space should be $N*(L+1)$.We can use the Manhattan distance between the insect and the goal as our non-trivial admissible heuristic.

## Part 2 Comparing Search and Heuristics
1. The order is $A-B-D-G$. 
The path solution is $A-B-D-G$.
2. The order is $A-B-C-D-F$.
The path solution is $A-C-F$.
3. The order is $A-B-C-D-G$.
The path solution is $A-B-D-G$.
4. h1, h2, h3 are admissible.
5. h1, h2 are consistent.
6. $A-B-C-D-F-D-G$ 
7. $A-C-B-D-G$
8. $A-C-D-G$
9. $A-C-D-G$

## Part2 Train CSP
