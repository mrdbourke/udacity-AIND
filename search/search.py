# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
     Returns the start state for the search problem
     """
     util.raiseNotDefined()

  def isGoalState(self, state):
     """
       state: Search state

     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state

     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  def is_goal(x):
      """
      Determine whether or not x is a goal state
      """
      return problem.isGoalState(x)

  # Set the starting state
  start = problem.getStartState()

  # Create the stack data structure
  stack = util.Stack() # From util library (Stack class)
  stack.push((start, []))
  # Set explored to be an empty set
  explored = set()

  # Loop through while the stack isn't empty
  while not stack.isEmpty():
      # Choose a leaf node (end node) and remove it from the frontier
      (node, path) = stack.pop()
      # Check to see if the node is a goal node, if so, return that path
      if is_goal(node):
          return path
      # If not a goal node, add it to the explored set
      explored.add(node)
      # Define the next (successor) nodes
      successors = problem.getSuccessors(node)
      for state, action, cost in successors:
          if state not in explored:
              # Only add the node if not already in the froniter or explored set
              stack.push((state, path + [action]))

  """
  ### Graph search algorithm - Page 77 AIMA textbook ###
    function GRAPH-SEARCH(problem) returns a solution or failure
      initialize the frontier using the initial state of the problem
      initialize the explored set to be empty
      loop do
          if the frontier is empty than return failure
          choose a leaf node and remove it from the frontier
          if the node contains a goal state then return the corresponding solution
          add the node to the explored set
          expand the chosen node, adding the resulting nodes to the frontier
              only if not in the frontier or explored set
  """


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """

  def is_goal(x):
    """
    Determine whether or not x is a goal state
    """
    return problem.isGoalState(x)

  # Define the starting state
  start = problem.getStartState()
  # Setup the Queue data stack
  queue = util.Queue()
  queue.push((start, []))
  # Initialise explored as an empty set
  explored = set()

  # Loop through while there's still more moves in the queue
  while not queue.isEmpty():
      # Pop off the shallowest node in the frontier
      (node, path) = queue.pop()
      # If the node is a goal node, return the solution
      if is_goal(node):
          return path
      # Define successors for the leaf node
      successors = problem.getSuccessors(node)
      for state, action, cost in successors:
          # If state not already explored, add it to the list
          if state not in explored:
              # Add the tree node to the explored list
              explored.add(node)
              # Push the state, path and action onto the queue
              queue.push((state, path + [action]))
  """
  ### Breadth-first search on a graph - Page 82 AIMA textbook ###

  fucntion Breafth-First-Search(problem) returns a solution or failure
  node <- a node with State = problem.Initial-State, Path-Cost = 0
  if problem.Goal-Test(node.State) then return Solution(node)
  frontier <- a FIFO queue with node as the only element
  explored <- an empty set
  loop do
    if Empty?(frontier) then return failure
    node <- Pop(frontier) /* chooses the shallowest node in frontier */
    add node.State to explored
    for each action in problem.Actions(node.State) do
        child <- Child-Node(problem, node, action)
        if child.State is not in explored or frontier then
            if problem.Goal-Test(child.State) then return SOLUTION(child)
            froniter <- Insert(child, froniter)
   """

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  # Use the PriorityQueue as the data structure when implementing the algorithm
  # Data structures are available in util.py

  def is_goal(x):
      """
      Determine whether or not x is a goal state
      """
      return problem.isGoalState(x)

  # Define the starting state
  start = problem.getStartState()
  # Setup the priority queue data structure
  frontier = util.PriorityQueue()
  frontier.push((start, []), 0)
  # Initialise explored as an empty set
  explored = set()

  # Loop through while the frontier is not empty
  while not frontier.isEmpty():
      # Pop off the shallowest node in the frontier
      (node, path) = frontier.pop()
      # If the node is a goal node, return the solution
      if is_goal(node):
          return path
      # Define successors for the leaf node
      successors = problem.getSuccessors(node)
      print successors
      if node not in explored:
          explored.add(node)
      for state, action, cost in successors:
          # If state not already explored, add it to the list
          if state not in explored:
              # Add the tree node to the frontier
              frontier.push((state, path+[action]),
                               problem.getCostOfActions(path+[action])+cost)


  """
  ### Pseudocode of the uniformCostSearch algorithm - Page 84 AIMA textbook ###

  function Uniform-Cost-Search(problem) returns a solution, or failure
  node <- a node with State = problem.Initial-State, Path-Cost = 0
  frontier <- a priority queue ordered by Path-Cost, with node as the only element
  explored <- an empty set
  loop do
    if Empty?(frontier) then return failure
    node <- Pop(frontier) /* chooses the lowest-cost node in frontier */
    if problem.Goal-Test(node.State) then return Solution(node)
    add node.State to explored
    for each action in problem.Actions(node.State) do
      child <- Child-Node(problem, node, action)
      if child.State is not in explored or frontier then
        frontier <- Insert(child, frontier)
      else if child.State is in frontier with higher Path-Cost then
        replace that frontier node with child
  """

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
