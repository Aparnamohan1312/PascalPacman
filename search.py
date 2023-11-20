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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    st = util.Stack() # Initialize the Stack 
    st.push((problem.getStartState(),[])) # Push the Current State

    # current_State = problem.getStartState()
    
    visited = [] # List for mark nodes that are Visited
    while(not st.isEmpty()): # Until we visit all the Nodes
        current_State, route=st.pop() # Run DFS on current Node to explore new paths
        if(problem.isGoalState(current_State)): # If Current State is our Goal then stop.
            return route 
        if current_State not in visited: # If the current State is Not visited the visit the node and run DFS to explore its Successors.
            visited.append(current_State)
            for child in problem.getSuccessors(current_State):
                new_route = route+[child[1]]
                st.push((child[0], new_route))
            
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    que = util.Queue()  # Initialize the Queue 
    que.push((problem.getStartState(),[])) # # Push the Current State

    # current_State = problem.getStartState()
    
    visited = [] # List for mark nodes that are Visited
    while(not que.isEmpty()): # Until we visit all the Nodes
        current_State, route=que.pop()  # Run BFS on current Node to explore new paths
        if(problem.isGoalState(current_State)): # If Current State is our Goal then stop.
            return route
        if current_State not in visited: # If the current State is Not visited the visit the node and run BFS to explore its Successors.
            visited.append(current_State)
            for child in problem.getSuccessors(current_State):
                new_route = route+[child[1]]
                que.push((child[0], new_route))
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = [] # List to track visited states
    priorityQueue = util.PriorityQueue()  # Priority queue to manage nodes to expand
    priorityQueue.push((problem.getStartState(), [], 0), 0) # Initialize priority queue with a cost of 0

    while priorityQueue: #Traverse nodes
        state, path, cost = priorityQueue.pop()  # Remove Least cost node
        if problem.isGoalState(state):
            return path  # Return path if goal reached
        if state not in visited:
            visited.append(state)  # Mark current state as visited
            successors = problem.getSuccessors(state)  # Gets successor states and their respective actions and step costs
            for successor, action, stepCost in successors:
                if successor not in visited:
                    totalCost = cost + stepCost # Calculate total cost of path to the successor          
                    priorityQueue.push((successor, path + [action], totalCost), totalCost) # Add successor to the priority queue with cost value

    return []  # No Path? Return empty List

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    # Initialize the start state, priority queue 
    start_state = problem.getStartState()
    new_list = util.PriorityQueue()
    new_list.push((start_state, [], 0), 0)
    goal_found = False

    # Keep track of traversed states 
    traversed = set()

    while True:
        if new_list.isEmpty():
            break

        state, actions, cost = new_list.pop()

        if state in traversed:
            continue

        if problem.isGoalState(state):
            goal_found = True
            break

        traversed.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in traversed:
                # Calculate the total cost
                g = cost + step_cost
                h = heuristic(successor, problem)
                f = g + h

                new_list.push((successor, actions + [action], g), f)

    # If a solution is found, return the actions found else empty list
    if goal_found:
        return actions
    else:
        return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
