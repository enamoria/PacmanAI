# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # "*** Initial ***"
    # vertex_stack = []  # stack for vertex, store current vertex
    # visited = []  # a list, store visited vertex
    # pre = {}  # a dictionary, pre['a'] contains the edge that have 'a' as its end
    #
    # vertex_stack.append(problem.getStartState())  # push the start state (a vertex) to stack
    #
    # "*** Start looping ***"
    # while len(vertex_stack) != 0:
    #     tmp = vertex_stack.pop()
    #
    #     if tmp not in visited:  # if tmp isn't visted yet
    #         visited.append(tmp)  # visit
    #
    #         if problem.isGoalState(tmp):  # if tmp is goal state, start tracing
    #             t = tmp
    #             path = []
    #
    #             while True:
    #                 # path.append(t)
    #                 path.append(pre[t][0])
    #                 t = pre[t][1]
    #
    #                 if t == problem.getStartState():
    #                     break
    #
    #             return path[::-1]  # return the reverse list of path
    #
    #         for i in problem.getSuccessors(tmp):  # add element to pre, append stack for successors of current vertex
    #             if i[0] not in visited:
    #                 pre[i[0]] = []
    #                 pre[i[0]].append(i[1])
    #                 pre[i[0]].append(tmp)
    #                 vertex_stack.append(i[0])
    #
    # return  # no need to return anything here, just mark for the end of the function
    # # like a habit

    vertex_stack = util.Stack()
    visited = []

    vertex_stack.push((problem.getStartState(), []))

    while not vertex_stack.isEmpty():
        current_node_state, current_node_move = vertex_stack.pop()

        if current_node_state not in visited:
            visited.append(current_node_state)

            if problem.isGoalState(current_node_state):
                return current_node_move

            for successor in problem.getSuccessors(current_node_state):
                if successor[0] not in visited:
                    vertex_stack.push((successor[0], current_node_move + [successor[1]]))

    return current_node_move


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"
    # "*** Initial ***"
    # vertex_queue = []  # stack for vertex, store current vertex
    # visited = []  # a list, store visited vertex
    # pre = {}  # a dictionary, pre['a'] contains the edge that have 'a' as its end
    #
    # vertex_queue.append(problem.getStartState())  # push the start state (a vertex) to stack
    #
    # "*** Start looping ***"
    # while len(vertex_queue) != 0:
    #     tmp = vertex_queue.pop(0)
    #
    #     if tmp not in visited:  # if tmp isn't visted yet
    #         visited.append(tmp)  # visit
    #
    #         if problem.isGoalState(tmp):  # if tmp is goal state, start tracing
    #             t = tmp
    #             path = []
    #
    #             while True:
    #                 # path.append(t)
    #                 path.append(pre[t][0])
    #                 t = pre[t][1]
    #
    #                 if t == problem.getStartState():
    #                     break
    #
    #             return path[::-1]  # return the reverse list of path
    #
    #         for i in problem.getSuccessors(tmp):  # add element to pre, append stack for successors of current vertex
    #             if (i[0] not in visited) and (i[0] not in vertex_queue):
    #                 pre[i[0]] = []
    #                 pre[i[0]].append(i[1])
    #                 pre[i[0]].append(tmp)
    #                 vertex_queue.append(i[0])
    #
    # return  # no need to return anything here, just mark for the end of the function
    # # like a habit

    vertex_queue = util.Queue()
    visited = []

    vertex_queue.push((problem.getStartState(), []))

    while not vertex_queue.isEmpty():
        current_node_state, current_node_move = vertex_queue.pop()

        if current_node_state not in visited:
            visited.append(current_node_state)

            if problem.isGoalState(current_node_state):
                return current_node_move

            for successor in problem.getSuccessors(current_node_state):
                if successor[0] not in visited:
                    vertex_queue.push((successor[0], current_node_move + [successor[1]]))

    return
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    vertex_queue = util.PriorityQueue()
    visited = []

    vertex_queue.push((problem.getStartState(), [], 0), 0)

    while not vertex_queue.isEmpty():
        current_node_state, current_node_move, current_node_cost = vertex_queue.pop()

        if current_node_state not in visited:  # if not visted yet
            if problem.isGoalState(current_node_state):  # check goal state
                return current_node_move

            else:
                visited.append(current_node_state)  # Append if not goal state

                # push successors in queue for expanding
                for state, direction, cost in problem.getSuccessors(current_node_state):
                    if state not in visited:
                        vertex_queue.push((state, current_node_move + [direction], current_node_cost + cost),
                                          current_node_cost + cost)

    return  # no need to return anything here, just mark for the end of the function
    # like a habit

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    queue = util.PriorityQueue()  # the fringe
    visited = []  # flag

    g = 0
    h = heuristic(problem.getStartState(), problem)
    f = g + h

    queue.push((problem.getStartState(), [], 0), f)

    print(problem)
    while not queue.isEmpty():
        expanded_node = queue.pop()

        if expanded_node[0] not in visited:
            visited.append(expanded_node[0])
            if problem.isGoalState(expanded_node[0]):
                return expanded_node[1]

            for state, direction, cost in problem.getSuccessors(expanded_node[0]):
                if state not in visited:
                    h = heuristic(state, problem)

                    g = expanded_node[2] + cost
                    # expanded_node[2] + cost, not g + cost. If g+cost, g will be
                    # overestimate -> f is, too -> unhandlable situation

                    f = g + h
                    queue.push((state, expanded_node[1] + [direction], g), f)  # f: priority value

    return


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
