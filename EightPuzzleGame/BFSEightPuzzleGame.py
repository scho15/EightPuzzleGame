import queue
import time
import sys

def GraphSearch(initialState):

    start_time = time.time()
    frontier = queue.Queue()
    path = queue.Queue()
    explored = set()
    state = tuple()
    frontierSet = set()
    neighbour = list()
    initialPath = list()
    currentPath = list()
    nodesExpanded = 0
    frontier.put(initialState)
    frontierSet.add(tuple(initialState))
    goalTest = (0,1,2,3,4,5,6,7,8)
    maxDepth = 0
    maxDepthIndicator = bool()

    while frontier.empty() == False:        
        ## print ("Length of frontier before expansion is ", len(frontier))
        state = frontier.get()
        frontierSet.remove(state)
        if path.empty() == False:
            initialPath = path.get()

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

		## Determine Up neighbour
        if (state.index(0) > 2):
            neighbour = list(state)
            currentPath = list(initialPath)
            a, b = neighbour.index(0),neighbour.index(0) - 3
            neighbour[b], neighbour[a] = neighbour[a], neighbour[b]
            ## print ("Up", neighbour)
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in list(frontierSet):
                frontier.put(tuple(neighbour))
                frontierSet.add(tuple(neighbour))
                currentPath.append("Up")
                path.put(list(currentPath))
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
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in list(frontierSet):
                frontier.put(tuple(neighbour))
                frontierSet.add(tuple(neighbour))
                currentPath.append("Down")
                path.put(list(currentPath))
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
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in list(frontierSet):
                frontier.put(tuple(neighbour))
                frontierSet.add(tuple(neighbour))
                currentPath.append("Left")
                path.put(list(currentPath))
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
            if tuple(neighbour) not in list(explored) and tuple(neighbour) not in list(frontierSet):
                frontier.put(tuple(neighbour))
                frontierSet.add(tuple(neighbour))
                currentPath.append("Right")
                path.put(list(currentPath))
            if len(currentPath) > maxDepth:
                maxDepth = len(currentPath)
                maxDepthIndicator = True
        nodesExpanded += 1
        if maxDepthIndicator:
            print("maxDepth:", maxDepth, "Frontier Size", frontier.qsize(), "nodesExpanded", nodesExpanded)
        maxDepthIndicator = False
    print(initialState)
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
## GraphSearch((6,1,8,4,0,2,7,3,5))
## GraphSearch((8,6,4,2,1,3,5,7,0))
GraphSearch((3,1,2,0,4,5,6,7,8))