from cmath import sqrt
from importlib.machinery import PathFinder
import math
import sys
import time
import csv
from dataTypes import Direction
from AStar import AStar
from fileParser import *

def runBoard(fileName, heuristic, count):
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

	CSVFileName = "../Data.csv"
	fields = [
		"Goal-X",
		"Goal-Y",
		"Robot-X",
		"Robot-Y",
		"Robot-Direction",
		"Distance-X",
		"Distance-Y",
		"Manhattan-Distance",
		"Diagonal-Distance",
		"A* Cost"
	]
	cummulativeCost = 0
	goalX = result[-1].state.coords.x
	goalY = result[-1].state.coords.y

	with open(CSVFileName, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		if count == 1: csvwriter.writerow(fields)

		for action in result:
			robotX = action.state.coords.x
			robotY = action.state.coords.y
			robotDir = directionInt(action.state.direction)
			distX = abs(goalX - robotX)
			distY = abs(goalY - robotY)
			manDist = distX + distY
			diagDist = math.sqrt(math.pow(distX, 2) + math.pow(distY, 2))
			aStarCost = result[-1].totalCost - cummulativeCost

			row = [
				str(goalX),
				str(goalY),
				str(robotX),
				str(robotY),
				str(robotDir),
				str(distX),
				str(distY),
				str(manDist),
				str(diagDist),
				str(aStarCost)
			]
			cummulativeCost += action.cost
			csvwriter.writerow(row)

def directionInt(dir):
    if dir == Direction.UP:
        return 0
    elif dir == Direction.RIGHT:
        return 1
    elif dir == Direction.DOWN:
        return 2
    elif dir == Direction.LEFT:
        return 3

def analyzeHeuristic(fileName, heuristic, count):
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

	CSVFileName = "../Analysis.csv"
	heuristicStr = ["Heuristic {}".format(heuristic)]
	fields = [
		"Board",
		"Nodes-Expanded",
		"Solution Depth",
		"Branching-Factor",
		"Effective-Branching-Factor",
		"Solution-Time",
		"Solution-Cost",
	]

	with open(CSVFileName, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		if count == 1:
			csvwriter.writerow(heuristicStr)
			csvwriter.writerow(fields)

		row = [
			count,
			nodesExpanded,
			solDepth,
			branchFac,
			effBranchFac,
			solTime,
			solCost
		]
		csvwriter.writerow(row)
