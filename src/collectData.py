from importlib.machinery import PathFinder
from runBoard import runBoard
from fileParser import *
import csv

count = 1
numRuns = 2
while(count <= numRuns):
	# Generate a new board
	print("\nCurrent Iteration: " + str(count) + "/" + str(numRuns))
	exec(open("genBoard.py").read())
	runBoard("../TestBoard.txt", 5, count)
	count += 1
