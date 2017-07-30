import time
import sys
from collections import deque
import heapq

class EightPuzzleGamev2:
    def GraphSearch(): ##method, initialState):
        method = sys.argv[1]
        initialState = list()
        argString = sys.argv[2].split(',')
        for number in argString:
            initialState.append(int(number))
        start_time = time.time()
        bfsFrontier = deque()
        bfsPath = deque()
        explored = set()
        state = tuple()
        neighbour = list()
        initialPath = list()
        currentPath = list()
        nodesExpanded = 0
        maxDepth = 0
        depthNode = [maxDepth, nodesExpanded]
        maxDepthIndicator = bool()
        astFrontier = []  ## treat as heapq or priority queue
        astPath = []
        manhattanDistance = 0

        bfsFrontier.append(initialState)
        goalTest = (0,1,2,3,4,5,6,7,8)

        if method == 'bfs':
            while len(bfsFrontier) != 0:        
                ## print ("Length of bfsFrontier before expansion is ", len(bfsFrontier))
                state = bfsFrontier.popleft()
                if len(bfsPath) != 0:
                    initialPath = bfsPath.popleft()
                if goalTest == tuple(state):
                    EightPuzzleGamev2.Goaltest(initialPath, explored, depthNode, start_time)
                    return 
                explored.add(tuple(state))
                EightPuzzleGamev2.determineNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            print(initialState)
            return
        elif method == 'dfs':
            while len(bfsFrontier) != 0:        
                ## print ("Length of bfsFrontier before expansion is ", len(bfsFrontier))
                state = bfsFrontier.pop()
                if len(bfsPath) != 0:
                    initialPath = bfsPath.pop()
                if goalTest == tuple(state):
                    EightPuzzleGamev2.Goaltest(initialPath, explored, depthNode, start_time)
                    return 
                explored.add(tuple(state))
                EightPuzzleGamev2.determineNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            print(initialState)
            return
        elif method == 'ast':  
            manhattanDistance = EightPuzzleGamev2.Manhattan(initialState)
            astFrontier.append([manhattanDistance, initialState, [] ])    
            while len(astFrontier) != 0:
                frontier = heapq.heappop(astFrontier)
                state = frontier[1]
                initialPath = frontier[2]
                if goalTest == tuple(state):
                    EightPuzzleGamev2.Goaltest(initialPath, explored, depthNode, start_time)
                    return 
                explored.add(tuple(state))
                EightPuzzleGamev2.determineNeighbour(method, state, initialPath, explored, astFrontier, astPath, depthNode)
            print(initialState)
            return

    def Manhattan(state):
 
        distance = 0
        for number in state:
            if number == 0:
                continue
            elif abs(state.index(number)-number)/3 == 1: 
                distance += 1   
            elif abs(state.index(number)-number)/3 == 2:    
                distance += 2
            if abs(state.index(number)-number)%3 == 1:
                distance += 1
            elif abs(state.index(number)-number)%3 == 2:
                distance += 2
        return distance

    def determineNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        nodesExpanded = depthNode[1]
        if method == 'bfs' or method == 'ast':
            EightPuzzleGamev2.determineUpNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineDownNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineLeftNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineRightNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)	        
        elif method == 'dfs':
            EightPuzzleGamev2.determineRightNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineLeftNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineDownNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            EightPuzzleGamev2.determineUpNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
        maxDepth = depthNode[0]
        nodesExpanded += 1
        if nodesExpanded%5000 == 0:
            print("maxDepth:", maxDepth, "Frontier Size", len(bfsFrontier), "nodesExpanded", nodesExpanded)
        maxDepthIndicator = False
        depthNode[0] = maxDepth
        depthNode[1] = nodesExpanded
        return

    def determineUpNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) > 2):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) - 3
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in list(bfsFrontier):
                currentPath.append("Up")
                if method == 'bfs' or method == 'dfs':
                    bfsFrontier.append(tuple(neighbour))
                    bfsPath.append(list(currentPath))
                else:
                    manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                    heapq.heappush(bfsFrontier, [manhattanDistance + len(currentPath), tuple(neighbour), list(currentPath)])
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
            elif tuple(neighbour) in list(bfsFrontier):
                manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                currentKey = bfsFrontier.index(tuple(neighbour))
        depthNode[0] = maxDepth
        return

    def determineDownNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) < 6):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) + 3
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Down", neighbour)
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                currentPath.append("Down")
                if method == 'bfs' or method == 'dfs':
                    bfsFrontier.append(tuple(neighbour))
                    bfsPath.append(list(currentPath))
                else:
                    manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                    heapq.heappush(bfsFrontier, heapq.heapify(manhattanDistance + len(currentPath), tuple(neighbour), list(currentPath)))
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
            elif tuple(neighbour) in bfsFrontier:
                manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                currentKey = bfsFrontier.index(tuple(neighbour))
        depthNode[0] = maxDepth
        return

    def determineLeftNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) % 3 != 0):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) - 1
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Left", neighbour)
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                currentPath.append("Left")
                if method == 'bfs' or method == 'dfs':
                    bfsFrontier.append(tuple(neighbour))
                    bfsPath.append(list(currentPath))
                else:
                    manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                    heapq.heappush(bfsFrontier, [manhattanDistance + len(currentPath), tuple(neighbour), list(currentPath)])
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
            elif tuple(neighbour) in bfsFrontier:
                manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                currentKey = bfsFrontier.index(tuple(neighbour))
        depthNode[0] = maxDepth
        return

    def determineRightNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) % 3 != 2):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) + 1
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Right", neighbour)
            if tuple(neighbour) not in explored and tuple(neighbour) not in bfsFrontier:
                currentPath.append("Right")
                if method == 'bfs' or method == 'dfs':
                    bfsFrontier.append(tuple(neighbour))
                    bfsPath.append(list(currentPath))
                else:
                    manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                    heapq.heappush(bfsFrontier, [manhattanDistance + len(currentPath), tuple(neighbour), list(currentPath)])
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
            elif tuple(neighbour) in bfsFrontier:
                manhattanDistance = EightPuzzleGamev2.Manhattan(tuple(neighbour))
                currentKey = bfsFrontier.index(tuple(neighbour))
        depthNode[0] = maxDepth
        return

    def Goaltest(initialPath, explored, depthNode, start_time):

        fo = open('output.txt','w')
        maxDepth = depthNode[0]
        toPrint = ['path_to_goal: ',str(initialPath),'\n']
        toPrint.append("cost_of_path: " + str(len(initialPath)) + '\n')
        toPrint.append("nodes_expanded: " + str(len(explored))+ '\n')
        toPrint.append("search_depth: " + str(len(initialPath))+ '\n')
        toPrint.append("max_search_depth: " + str(maxDepth)+ '\n')
        toPrint.append("running_time: " + str(round(time.time() - start_time,8))+ '\n')
        toPrint.append("max_ram_usage: " + str(round(EightPuzzleGamev2.SystemResource(),8)))
        fo.writelines(toPrint)
        fo.close()
        return 

    def SystemResource():
        if sys.platform == "win32" or sys.platform == "win64":
            import psutil
            return psutil.Process().memory_info().rss/1000000000
        else:
        # Note: if you execute Python from cygwin,
        # the sys.platform is "cygwin"
        # the grading system's sys.platform is "linux2"
            import resource
            return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000

## EightPuzzleGamev2.GraphSearch('bfs', (3,1,2,0,4,5,6,7,8))
## Submission: 1; 1; 1; 1

## EightPuzzleGamev2.GraphSearch('dfs', (3,1,2,0,4,5,6,7,8))
## Submission: 1; 1; 1; 1

##EightPuzzleGamev2.GraphSearch('ast', (3,1,2,0,4,5,6,7,8))
EightPuzzleGamev2.GraphSearch()
## Submission: 1; 1; 1; 1

## EightPuzzleGamev2.GraphSearch('bfs', (1,2,5,3,4,0,6,7,8))
## Submission: 3; 10; 3; 4

## EightPuzzleGamev2.GraphSearch('dfs', (1,2,5,3,4,0,6,7,8))
## Submission: 3; 181437; 3; 66125

## EightPuzzleGamev2.GraphSearch('ast', (1,2,5,3,4,0,6,7,8))
## Submission: 3; 3; 3; 3

## EightPuzzleGamev2.GraphSearch('dfs', (6,1,8,4,0,2,7,3,5))
## Submission: 46142; 51015; 46142; 46142

## EightPuzzleGamev2.GraphSearch('bfs', (6,1,8,4,0,2,7,3,5))
## Submission: 20; 54094; 20; 21

## EightPuzzleGamev2.GraphSearch('ast', (6,1,8,4,0,2,7,3,5))
## Without key reduction: 20; 1461; 20; 20
## Submission: 20; 696; 20; 20

## GraphSearch('dfs', (8,6,4,2,1,3,5,7,0))
## EightPuzzleGamev2.GraphSearch('ast', (8,6,4,2,1,3,5,7,0))
## Without key reduction: 26; 8066; 26; 26
## Submission: 26; 1585; 26; 26