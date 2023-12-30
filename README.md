# ML Enhanced A-Star Solver

## How to Run

**You must use python 3.10 to run this project.**  
Enter the ./src directory and run:

```
python main.py [file_path] [heuristic]
```

- `file_path` is the file path for the board in the standard notation of your os
- `heuristic` is a number from 1-6 as listed in the projects spec

#### ML Data Collection

For 1000 boards of size 75, whenever A star search ends, for each square on the path, we recorded the
actual path cost to the goal from this node and our feature values in a csv file.

Enter the ./src directory and run:

```
python collectData.py
```

#### Analysis for 10 Boards

Data was obtained by running our algorithm through 10 different boards of size 75 that could be solved
by heuristics 5, 6, and 7 in about 10 seconds. You must execute this command for each of the three heuristics
by changing the `heuristicNum` variable inside of `boardAnalysis.py`.

Enter the ./src directory and run:

```
python boardAnalysis.py
```

## Heuristic Functions

The implementation of the heuristic functions are located in datatypes.py within the 'BoardState' class

- heuristics 1-4 are as listed in the project spec
- heuristic 5 is the (manhattan distance to the goal) \* min(3, lowest complexity on the board)
- heuristic 6 is 5\*(heuristic 5) as listed in the project spec. It is not admissible
- heuristic 7 is the learned function generated through linear regression in Weka
