#!/usr/bin/python
### Data Structures
#
# Sample current states for testing is shown below.
# Add following lines one by one into state.txt for testing:
#
# 8 1 7 2 4 6 3 0 5
# 1 0 7 8 2 6 3 4 5
# 8 1 7 0 2 6 3 4 5
# 8 1 7 3 2 6 4 0 5
# 8 1 7 0 2 6 3 4 5
# 8 1 7 0 2 6 3 4 5
# 8 1 7 2 6 0 3 4 5
# 8 0 7 2 1 6 3 4 5
# 8 1 7 2 4 6 3 0 5
#
# The 0 denotes the empty space.
goal_state = [1, 2, 7, 8, 4, 6, 3, 0, 5]

import time
import tracemalloc

from pythonds.basic.stack import Stack


def move_up(state):
    """Moves the blank tile up on the board. Returns a new state as a list."""
    # Perform an object copy
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 3, 6]:
        # Swap the values.
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None (Pythons NULL)
        return None


def move_down(state):
    """Moves the blank tile down on the board. Returns a new state as a list."""
    # Perform object copy
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [2, 5, 8]:
        # Swap the values.
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None.
        return None


def move_left(state):
    """Moves the blank tile left on the board. Returns a new state as a list."""
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [0, 1, 2]:
        # Swap the values.
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move it, return None
        return None


def move_right(state):
    """Moves the blank tile right on the board. Returns a new state as a list."""
    # Performs an object copy. Python passes by reference.
    new_state = state[:]
    index = new_state.index(0)
    # Sanity check
    if index not in [6, 7, 8]:
        # Swap the values.
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        # Can't move, return None
        return None


def create_node(state, parent, operator, depth, cost):
    return Node(state, parent, operator, depth, cost)


def expand_node(node):
    """Returns a list of expanded nodes"""
    expanded_nodes = []
    expanded_nodes.append(create_node(move_up(node.state), node, "u", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_down(node.state), node, "d", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_left(node.state), node, "l", node.depth + 1, 0))
    expanded_nodes.append(create_node(move_right(node.state), node, "r", node.depth + 1, 0))
    # Filter the list and remove the nodes that are impossible (move function returned None)
    expanded_nodes = [node for node in expanded_nodes if node.state != None]  # list comprehension!
    return expanded_nodes


def bfs(start, goal):
    """Performs a breadth first search from the start state to the goal"""
    # A list (can act as a queue) for the nodes.
    goal = goal
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    fringe.append(start_node)
    current = fringe.pop(0)
    path = []
    while (current.state != goal):
        fringe.extend(expand_node(current))
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path
    pass


def dfs(start, goal, depth=10):
    start_node = create_node(start, None, None, 0, 0)
    fringe_stack = Stack()
    fringe_stack.push(start_node)
    current = fringe_stack.pop()
    path = []
    while (current.state != goal):
        temp = expand_node(current)
        for item in temp:
            fringe_stack.push(item)
        current = fringe_stack.pop()
        if (current.depth > 10):
            return None
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def greedy(start, goal):
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    path = []
    fringe.append(start_node)
    current = fringe.pop(0)
    while (current.state != goal):
        fringe.extend(expand_node(current))
        for item in fringe:
            h(item, goal)
        fringe.sort(key=lambda x: x.heuristic)
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def a_star(start, goal):
    start_node = create_node(start, None, None, 0, 0)
    fringe = []
    path = []
    fringe.append(start_node)
    current = fringe.pop(0)
    while (current.state != goal):
        fringe.extend(expand_node(current))
        for item in fringe:
            h(item, goal)
            item.heuristic += item.depth
        fringe.sort(key=lambda x: x.heuristic)
        current = fringe.pop(0)
    while (current.parent != None):
        path.insert(0, current.operator)
        current = current.parent
    return path


def h(state, goal):
    dmatch = 0
    for i in range(0, 9):
        if state.state[i] != goal[i]:
            dmatch += 1
    state.heuristic = dmatch


# Node data structure
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

        self.heuristic = None


def readfile(filename):
    f = open(filename)
    data = f.read()
    # Get rid of the newlines
    data = data.strip("\n")
    # Break the string into a list using a space as a seperator.
    data = data.split(" ")
    state = []
    for element in data:
        state.append(int(element))
    print('state: ', state)
    print('goal: ', goal_state)
    return state


def validate_response(result):
    if result == None:
        print("No solution found")
    elif result == [None]:
        print("Start node was the goal!")
    else:
        print(len(result), " moves")


def bfs_matrics_collector(starting_state):
    print("")
    print("************ RUNNING BFS ALGORITHM ************")

    start_time = time.perf_counter_ns()
    tracemalloc.start()

    result = bfs(starting_state, goal_state)
    validate_response(result)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory: {current / 10 ** 6}MB | Peak memory: {peak / 10 ** 6}MB")
    tracemalloc.stop()
    elapsed = (time.perf_counter_ns() - start_time)
    print("Time elapsed(nanoseconds): ", elapsed)

    print("***********************************************")
    print("")


def dfs_matrics_collector(starting_state):
    print("")
    print("************ RUNNING DFS ALGORITHM ************")

    start_time = time.perf_counter_ns()
    tracemalloc.start()

    result = dfs(starting_state, goal_state)
    validate_response(result)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory: {current / 10 ** 6}MB | Peak memory: {peak / 10 ** 6}MB")
    tracemalloc.stop()
    elapsed = (time.perf_counter_ns() - start_time)
    print("Time elapsed(nanoseconds): ", elapsed)

    print("***********************************************")
    print("")


def greedy_matrics_collector(starting_state):
    print("")
    print("************ RUNNING GREEDY ALGORITHM *********")

    start_time = time.perf_counter_ns()
    tracemalloc.start()

    result = greedy(starting_state, goal_state)
    validate_response(result)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory: {current / 10 ** 6}MB | Peak memory: {peak / 10 ** 6}MB")
    tracemalloc.stop()
    elapsed = (time.perf_counter_ns() - start_time)
    print("Time elapsed(nanoseconds): ", elapsed)

    print("***********************************************")
    print("")


def a_star_matrics_collector(starting_state):
    print("")
    print("************ RUNNING A* ALGORITHM *************")

    start_time = time.perf_counter_ns()
    tracemalloc.start()

    result = a_star(starting_state, goal_state)
    validate_response(result)

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory: {current / 10 ** 6}MB | Peak memory: {peak / 10 ** 6}MB")
    tracemalloc.stop()
    elapsed = (time.perf_counter_ns() - start_time)
    print("Time elapsed(nanoseconds): ", elapsed)

    print("***********************************************")
    print("")


def main():
    starting_state = readfile(r"state.txt")

    bfs_matrics_collector(starting_state)
    dfs_matrics_collector(starting_state)
    greedy_matrics_collector(starting_state)
    a_star_matrics_collector(starting_state)


if __name__ == "__main__":
    main()
