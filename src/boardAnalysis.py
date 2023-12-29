from importlib.machinery import PathFinder
from runBoard import runBoard, analyzeHeuristic
from fileParser import *
import csv

count = 1
numBoards = 10
heuristicNum = 7
while(count <= numBoards):
	# Get number board
	print("\nCurrent Iteration: " + str(count) + "/" + str(numBoards))
	filePath = "../boards/board{}.txt".format(count)
	analyzeHeuristic(filePath, heuristicNum, count)
	count += 1
