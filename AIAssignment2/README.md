## Need Python 3 with PIP3

## Run following commands. Skip these commands if you are using the ai2 environment
```
$ python -m venv ai2
$ ai2\Scripts\activate
$ pip3 install python-stack
$ pip3 install pythonds
```

## The state.txt contains the input dataset of the graph

## Output of the program will be as follows
```
(ai2) C:\Users\Hafeez\Documents\Msc\Lecture Notes\AI\Assignment2\repo\msc-ai-assignment-2\AIAssignment2>python AlgoExperiment.py
state:  [8, 1, 7, 2, 0, 6, 3, 4, 5]
goal:  [1, 2, 7, 8, 4, 6, 3, 0, 5]

************ RUNNING BFS ALGORITHM ************
5  moves
Current memory: 0.010296MB | Peak memory: 0.167208MB
Time elapsed(nanoseconds):  3811200
***********************************************


************ RUNNING DFS ALGORITHM ************
No solution found
Current memory: 0.001744MB | Peak memory: 0.010296MB
Time elapsed(nanoseconds):  583300
***********************************************


************ RUNNING GREEDY ALGORITHM *********
5  moves
Current memory: 0.0014MB | Peak memory: 0.00564MB
Time elapsed(nanoseconds):  619900
***********************************************


************ RUNNING A* ALGORITHM *************
5  moves
Current memory: 0.000952MB | Peak memory: 0.005792MB
Time elapsed(nanoseconds):  434200
***********************************************
```
