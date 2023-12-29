from re import S
import sys
import time
from AStar import AStar
from fileParser import *
import math

# Parse command line inputs
fileName = sys.argv[1]
heuristic: int = int(sys.argv[2])
board = parseFile(fileName)

# Initialize, run, and time the pathfinder
pathfinder = AStar(board, heuristic)

print("Running on {} using heuristic {}...\n".format(fileName, heuristic))

startTime = time.time()
result = pathfinder.doAStar()
timeTaken = time.time() - startTime

nodesExpanded = pathfinder.numExplored
solDepth = len(result)
branchFac = round(nodesExpanded / solDepth, 3)
effBranchFac = round(math.pow(nodesExpanded, 1 / solDepth), 3)
solTime = round(timeTaken, 3)
solCost = result[-1].totalCost

# Print results
print("Actions")
for action in result:
	print("{:<10} ({}, {}) Cost: {}".format(str(action.actionType), action.state.coords.x, action.state.coords.y, action.cost))

print("\nExplored Nodes: {}".format(nodesExpanded))
print("Solution Depth: {}".format(solDepth))
print("Branching Factor: {}".format(branchFac))
print("Effective Branching Factor: {}".format(effBranchFac))
print("Time Taken: {} secs".format(solTime))
print("Total Cost: {}\n".format(solCost))
