"""Uniform Cost Search for Solving Rolling-Die-Maze Problem

Author: Ankan Mookherjee

"""
from heapq import heappush, heappop
from sys import argv, exit

# List Maze symbols
maze = []
# The goal location (x, y).
goal = None
# A mapping of node names to lowest found cost.
visitedNodes = {}
# A heap of States.
frontier = []
# Total moves to reach goal
totalmoves = 0
# Cost of generating Node
cost = []
# Global counters for number of states visited 
i_visited_nodes = 0
# Global counters for number of states generated.
i_generated_nodes = 0
# The heuristic function
heuristic = lambda state: 0




####################################################################################################
####################################################################################################
# Class Configuration for Configuration object
#
# Represents a configuration of the problem space
##################################################
    

class Configuration(object):
 
    # Constructor 
    def __init__(self, x, y, die, move):
        self.x = x
        self.y = y
        self.die = die
        self.move = move



    
    ##################################################    
    # Is Valid Function
    # 
    # Tests a Configuration for validity.
            
    # Returns False if the Configuration is off the 
    # board, a "*" space, or has a 6 on top.
    #
    # accepts : Configuration
    # return  : Boolean 
    ##################################################

    def is_Valid(Configuration):
        if ((valid_Space(Configuration.x, Configuration.y)) and (Configuration.die[0] != 6)) :
            return True
        else :
            return False 
    

    ##################################################    
    # Generate Neighbors Function
    # 
    # Return all valid neighbors of this Configuration.
    #
    # accepts : Configuration
    # return  : List of Configuration.
    ##################################################
    
    def generateNeighbors(self):

        # Die faces: (top, north, east)
        (top, north, east) = self.die
        return filter(Configuration.is_Valid, [
            Configuration(self.x, self.y + 1, (7 - north, top, east), "NORTH"),
            Configuration(self.x, self.y - 1, (north, 7 - top, east), "SOUTH"),
            Configuration(self.x + 1, self.y, (7 - east, north, top), "EAST"),
            Configuration(self.x - 1, self.y, (east, north, 7 - top), "WEST"),
        ])
    
    ##################################################    
    # EQUALITY Function
    # 
    # Used by built in equality function for 
    # dictionaries and set
    #
    # accepts : Configuration, Configuration
    # return  : Boolean
    ##################################################
    
    def __eq__(self, object):
        return isinstance(object, Configuration) and self.x == object.x and self.y == object.y and self.die == object.die
    
    
    ##################################################    
    # Hash Function
    # 
    # Used by Built in Hash function for dictionaries and set
    # for quick indexing while lookup
    #
    # accepts : None
    # return  : hash number
    ##################################################
    
    def __hash__(self):
        return hash((self.x, self.y, self.die))
    
    
####################################################################################################
# END OF CONFIGURATION CLASS    

  


####################################################################################################
####################################################################################################
# Class Configuration for Node object
#
# Represents a node in the algorithm search tree
##################################################

class Node(object) :

    
    # Constructor
    def __init__(self, Configuration, cost, parent):
        self.Configuration = Configuration
        self.cost = cost
        self.parent = parent
    
    ##################################################    
    # Expand Function
    # 
    # Expand this node and add its state's neighbors to the frontier.
    #
    # accepts : None
    # return  : None 
    ##################################################
        
    def expand(self) :

        global i_generated_nodes, i_visited_nodes
        visitedNodes[self.Configuration] = self.cost
        i_visited_nodes += 1
        
        
        for neighbor in self.Configuration.generateNeighbors() :
            next_cost = self.cost + heuristic(neighbor)
            
            if neighbor not in visitedNodes or next_cost < visitedNodes[neighbor]:
                heappush(frontier, Node(neighbor, next_cost, self))
                i_generated_nodes += 1
   
    ##################################################    
    # Unwind Function
    # 
    # Unwind the path of Move and states taken to reach this node.
    #
    # accepts : None
    # return  : None 
    ##################################################
    def unwind(self):
        
        if self.parent == None:
            return []
        else:
            path = self.parent.unwind()
            path.append((self.Configuration.move, self.Configuration))
            return path
    
    
    ##################################################    
    #  LT Function
    # 
    # Used by built-in sorting algorithms.
    #
    # accepts : self, other
    # return  : Node.cost
    ##################################################
    def __lt__(self, other):
        return self.cost < other.cost


####################################################################################################
# END OF Node CLASS    




####################################################################################################
####################################################################################################
# HEURISTICS 
#
# Represents HEURISTIC FUNCTIONS USED FOR A* SEARCH
##################################################



##################################################    
# A STAR SEARCH Function
# 
# Generates A Star Search to Search the optimum 
# path between Start State and Goal.
#
# accepts : Configuration
# return  : None
##################################################
 
def a_Star_Search(Configuration) :
    global frontier , goal, visitedNodes
    global i_visited_nodes, i_generated_nodes
    frontier = []
    visitedNodes = {}
    
    i_visited_nodes = 1
    i_generated_nodes = 0
    
    frontier.append(Node(Configuration, 0 , None))
    visitedNodes[Configuration] = 0
    
    while True :
        if(len(frontier)== 0) :
            return ["ROUTE NOT POSSIBLE"], i_visited_nodes, i_generated_nodes
        
        node = heappop(frontier)
        
        if is_Goal(node.Configuration) :
            return node.unwind(), i_visited_nodes, i_generated_nodes
        else :
            node.expand()



##################################################    
# VALID SPACE Function
# 
# Returns Euclidean Distance between Configuration
# and goal.
#
# accepts : Configuration
# return  : cost
##################################################
 
def euclidean_cost(Configuration) :
    cost = ((Configuration.x - goal[0]) ** 2 + (Configuration.y - goal[1]) ** 2) ** 0.5
    return cost
 

##################################################    
# MANHATTAN COST Function
# 
# Returns Manhattan distance between Configuration and 
# goal.
#
# accepts : Configuration
# return  : cost
##################################################

def manhattan_cost(Configuration) :
    cost = abs(Configuration.x - goal[0]) + abs(Configuration.y - goal[1])    
    return cost




##################################################    
# BREADTH FIRST SEARCH COST Function
# 
# A breadth first search to find distances 
# from the goal for each location.
#
# accepts : Configuration
# return  : cost
##################################################

def breadth_first_search_cost(Configuration) :
    global cost
    cost = list(map(list, maze))
    
    frontier = [(goal[0], goal[1])] 
    depth = 0
    
    while ( len(frontier) > 0) :
        queue = list(frontier)
        frontier = set([])
        for x, y in queue :
            cost[x][y] = depth
            frontier.update(generate_Valid_NextConfig(x,y))
        depth = depth + 1
        
    return cost[Configuration.x][Configuration.y]


##################################################    
# Generate Valid Next Configurations
# 
# Generates and filters Valid Next Configurations
# to the given x and y coordinates 
#
# accepts : x-coordinate, y-coordinate
# return  : List of valid (x,y)
##################################################

def generate_Valid_NextConfig(xcordinate,ycordinate) :
    return filter(new_coordinate, [(xcordinate + 1, ycordinate),(xcordinate - 1, ycordinate),(xcordinate, ycordinate + 1),(xcordinate, ycordinate - 1)])



##################################################    
# New Coordinate
# 
# Checks the validity of coordinates
#
# accepts : coordinates
# return  : Boolean
##################################################
  
def new_coordinate(cordinates) :
    xcordinate,ycordinate = cordinates
    if( (valid_Space(xcordinate, ycordinate)) and (type(cost[xcordinate][ycordinate]) != int) ) :
        return True
    else :
        return False




##################################################    
# VALID SPACE Function
# 
# Tests whether the given x, y is in the puzzle space and not a
#
# accepts : x-coordinate, y-coordinate
# return  : Boolean
##################################################
    
def valid_Space(x, y):
    
    if ((0 <= x < len(maze)) and (0 <= y < len(maze[0])) and (maze[x][y] != '*')) :
        return True
    else :
        return False
 



####################################################################################################
# END OF HEURISTIC 


            
        
##################################################    
# Is Goal Function
# 
# Tests whether Configuration is goal or not
#
# accepts : Configuration
# return  : Boolean
##################################################

def is_Goal(Configuration):
    if ( ( (Configuration.x, Configuration.y) == goal ) and (Configuration.die[0] == 1)) :
        return True
    else :
        return False
    


    
##################################################    
# Print Result Function
# 
# Prints configuration using a full path
#
# accepts : configuration
# return  : None
##################################################

def print_results(Configuration) :
    path, i_visited_nodes, i_generated_nodes = a_Star_Search(Configuration)
    for move, Configuration in path:
        print_Configration(Configuration)
        
    print("%s nodes visited out of %s generated." % (i_visited_nodes, i_generated_nodes))
    
##################################################    
# Print Configuration Function
# 
# Prints a die top and move
#
# accepts : configuration
# return  : None
##################################################

def print_Configration(Configuration):
    global totalmoves
    totalmoves += 1
    top, north, east = Configuration.die
    print ("%s -> %s, %s, %s" % (Configuration.move, top, north, east))

#######################################################################################################################
 
def main():
    if len(argv) < 2:
        print("Usage: Main.py puzzle_file")
        exit(1)
    
    
    
    with open(argv[1], 'r') as File:
        row = File.read().splitlines()
    
    row.reverse()

    start = None
    
    global goal , maze , heuristic, totalmoves
    
    maze = [[] for _ in range(len(row[0]))]

    for y, line in enumerate(row) :
        for x, char in enumerate(line) :
            maze[x].append(char)
            
            if char == 'S' :
                start = Configuration(x,y,(1,2,3),None)
            
            if char == 'G' :
                goal = (x,y)

    # Solving the Puzzle
    print("Euclidean distance:")
    print "Direction -> Die-Face, Die-North, Die-East"
    heuristic = euclidean_cost
    print_results(start)
    print "Total Moves :",
    print totalmoves
    
    totalmoves = 0 
    
    print("Manhattan distance:")
    print "Direction -> Die-Face, Die-North, Die-East"
    heuristic = manhattan_cost
    print_results(start)
    print "Total Moves :",
    print totalmoves
    
    totalmoves = 0
    
    print("Breadth First Search distance:")
    print "Direction -> Die-Face, Die-North, Die-East"
    heuristic = breadth_first_search_cost
    print_results(start)
    print "Total Moves :",
    print totalmoves


    
if __name__ == "__main__":
    main()