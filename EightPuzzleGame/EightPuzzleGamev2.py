import queue
import time
import sys
from collections import deque
import heapq

class EightPuzzleGamev2():
    def GraphSearch(method, initialState):

        ## Trying deque rather than queue
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
        depthNode = [nodesExpanded, maxDepth]
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
                    Goaltest(initialPath, explored, maxDepth, start_time)
                    return 

                explored.add(tuple(state))

		        ## Determine Up neighbour
                if (state.index(0) > 2):
                    neighbour = list(state)
                    currentPath = list(initialPath)
                    a, b = neighbour.index(0),neighbour.index(0) - 3
                    neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
                    ## print ("Up", neighbour)
                    if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                        bfsFrontier.append(tuple(neighbour))
                        currentPath.append("Up")
                        bfsPath.append(list(currentPath))
                    if len(currentPath) > maxDepth:
                        maxDepth = len(currentPath)
                        maxDepthIndicator = True
		        ## Determine Down neighbour
                if (state.index(0) < 6):
                    neighbour = list(state)
                    currentPath = list(initialPath)
                    a, b = neighbour.index(0),neighbour.index(0) + 3
                    neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
                    ## print ("Down", neighbour)
                    if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                        bfsFrontier.append(tuple(neighbour))
                        currentPath.append("Down")
                        bfsPath.append(list(currentPath))
                    if len(currentPath) > maxDepth:
                        maxDepth = len(currentPath)
                        maxDepthIndicator = True
		        ## Determine Left neighbour
                if (state.index(0) % 3 != 0):
                    neighbour = list(state)
                    currentPath = list(initialPath)
                    a, b = neighbour.index(0),neighbour.index(0) - 1
                    neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
                    ## print ("Left", neighbour)
                    if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                        bfsFrontier.append(tuple(neighbour))
                        currentPath.append("Left")
                        bfsPath.append(list(currentPath))
                    if len(currentPath) > maxDepth:
                        maxDepth = len(currentPath)
                        maxDepthIndicator = True
		        ## Determine Right neighbour
                if (state.index(0) % 3 != 2):
                    neighbour = list(state)
                    currentPath = list(initialPath)
                    a, b = neighbour.index(0),neighbour.index(0) + 1
                    neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
                    ## print ("Right", neighbour)
                    if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                        bfsFrontier.append(tuple(neighbour))
                        currentPath.append("Right")
                        bfsPath.append(list(currentPath))
                    if len(currentPath) > maxDepth:
                        maxDepth = len(currentPath)
                        maxDepthIndicator = True
                nodesExpanded += 1
                if maxDepthIndicator:
                    print("maxDepth:", maxDepth, "Frontier Size", len(bfsFrontier), "nodesExpanded", nodesExpanded)
                maxDepthIndicator = False
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
            manhattanDistance = Manhattan(initialState)
            astFrontier.append(manhattanDistance,initialState)    
            heapq.heappush(astFrontier)

            while len(astFrontier) != 0:
                state = heapq.heappop(astFrontier)[1]
                if len(astPath) != 0:
                    initialPath = heapq.heappop(astPath)[1]

                if goalTest == tuple(state):
                    print("path_to_goal:",initialPath)
                    print("cost_of_path:", len(initialPath))
                    print("nodes_expanded:", len(explored))
                    print("search_depth:", len(initialPath))
                    print("max_search_depth:", maxDepth)
                    print("running_time:", round(time.time() - start_time,8))
                    print("max_ram_usage:", round(SystemResource(),8))
                    return 

                explored.add(tuple(state))
                determineNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, maxDepth.maxDepth, nodesExpanded)

            print(initialState)
            return

    def Manhattan(state):
 
        distance = 0
        for number in state:
            if state.index(number) == 0:
                skip
            elif state.index(number)%3 == 1: 
                distance += 1   
            elif state.index(number)%3 == 2:    
                distance += 2
            if state.index(number)/3 == 1:
                distance += 1
            elif state.index(number)/3 == 2:
                distance += 2
        return distance

    def determineNeighbour(method, state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        nodesExpanded = depthNode[1]
        if method == 'dfs':
            ## Determine Right neighbour
            EightPuzzleGamev2.determineRightNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
	        ## Determine Left neighbour
            EightPuzzleGamev2.determineLeftNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            ## Determine Down neighbour
            EightPuzzleGamev2.determineDownNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
            ## Determine Up neighbour
            EightPuzzleGamev2.determineUpNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode)
        maxDepth = depthNode[0]
        nodesExpanded += 1
        if nodesExpanded%5000 == 0:
            print("maxDepth:", maxDepth, "Frontier Size", len(bfsFrontier), "nodesExpanded", nodesExpanded)
        maxDepthIndicator = False
        depthNode[0] = maxDepth
        depthNode[1] = nodesExpanded
        return

    def determineUpNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) > 2):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) - 3
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                bfsFrontier.append(tuple(neighbour))
                currentPath.append("Up")
                bfsPath.append(list(currentPath))
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
        depthNode[0] = maxDepth
        return

    def determineDownNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) < 6):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) + 3
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Down", neighbour)
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                bfsFrontier.append(tuple(neighbour))
                currentPath.append("Down")
                bfsPath.append(list(currentPath))
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
        depthNode[0] = maxDepth
        return

    def determineLeftNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) % 3 != 0):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) - 1
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Left", neighbour)
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in bfsFrontier:
                bfsFrontier.append(tuple(neighbour))
                currentPath.append("Left")
                bfsPath.append(list(currentPath))
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
        depthNode[0] = maxDepth
        return

    def determineRightNeighbour(state, initialPath, explored, bfsFrontier, bfsPath, depthNode):

        maxDepth = depthNode[0]
        if (state.index(0) % 3 != 2):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) + 1
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Right", neighbour)
            if tuple(neighbour) not in explored and tuple(neighbour) not in bfsFrontier:
                bfsFrontier.append(tuple(neighbour))
                currentPath.append("Right")
                bfsPath.append(list(currentPath))
                if len(currentPath) > maxDepth:
                    maxDepth = len(currentPath)
                    maxDepthIndicator = True
        depthNode[0] = maxDepth
        return

    def Goaltest(initialPath, explored, depthNode, start_time):

        maxDepth = depthNode[0]
        print("path_to_goal:",initialPath)
        print("cost_of_path:", len(initialPath))
        print("nodes_expanded:", len(explored))
        print("search_depth:", len(initialPath))
        print("max_search_depth:", maxDepth)
        print("running_time:", round(time.time() - start_time,8))
        print("max_ram_usage:", round(EightPuzzleGamev2.SystemResource(),8))
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

## GraphSearch((1,2,5,3,4,0,6,7,8))
## GraphSearch('dfs', (1,2,5,3,4,0,6,7,8))
## GraphSearch('dfs', (8,6,4,2,1,3,5,7,0))
EightPuzzleGamev2.GraphSearch('dfs', (6,1,8,4,0,2,7,3,5))
## GraphSearch('dfs', (3,1,2,0,4,5,6,7,8))