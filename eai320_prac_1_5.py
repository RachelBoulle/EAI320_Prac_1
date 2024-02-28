# EAI 320 Practical 1
# Group 5
# Carli Jansen van Rensburg u22493990
# Rachel Boulle u22523830

# input = "" # needed for Test4R() to work

# global variable for choosing whether to use BFS or DFS
    # BFS: bfs_dfs=0
    # DFS: bfs_dfs=1
bfs_dfs=0

############################################## START OF TREE CREATION FUNCTIONS ######################################################
# define the nodes which tree consist of, will be used for search tree
class TreeNode:
    def __init__(self, data):
        self.data = data             #"R", "P" or "S"    // saves data of the move
        self.left = None             #"R"                // link
        self.middle = None           #"P"                // link   
        self.right = None            #"s"                // link
        self.path = data

# global variable used in BFS and AdderBFS
queue = []

# create root of tree (foundation to build tree on)
# used to test searching algorithms
def createTree(depthL):
    root = buildTree(depthL)
    return root

# build tree recursivly
# used to test searching algorithms
def buildTree(depthL):
    if (depthL < 0):
        return
    newNode = TreeNode("0")
    if (depthL > 0):
        newNode.left = buildTree(depthL - 1)
        (newNode.left).data = "R"
        (newNode.left).path = "R"

        newNode.middle = buildTree(depthL - 1)
        (newNode.middle).data = "P"
        (newNode.middle).path = "P"

        newNode.right = buildTree(depthL - 1)
        (newNode.right).data = "S"
        (newNode.right).path = "S"
    return newNode
############################################### END OF TREE CREATION FUNCTIONS #######################################################


################################################## START OF SEARCH STRUCTURES ########################################################
# searches a preexisting tree and returns an array of search paths to all nodes represented as strings
# not used in outcome of RPS game, because does not dynamiclly search tree as it is being built
def BFS(root):
    searchSeq = []

    queue.append(root)

    while queue:
        p = queue.pop(0)
        
        if (p.data != "0"):
            searchSeq.append(p.path)

        if (p.left != None):
            queue.append(p.left)
            if (p.data != "0"):
                (p.left).path = p.path + (p.left.path)

        if (p.middle != None):
            queue.append(p.middle)
            if (p.data != "0"):
                (p.middle).path = p.path + (p.middle.path)

        if (p.right != None):
            queue.append(p.right)
            if (p.data != "0"):
                (p.right).path = p.path + (p.right.path)

    # reset each node's search path so that the next search does not build on current search's paths
    queue.append(root)
    while queue:
        p = queue.pop(0)
        

        if (p.left != None):
            queue.append(p.left)
            if (p.data != "0"):
                (p.left).path = "R"

        if (p.middle != None):
            queue.append(p.middle)
            if (p.data != "0"):
                (p.middle).path = "P"

        if (p.right != None):
            queue.append(p.right)
            if (p.data != "0"):
                (p.right).path = "S"

    return searchSeq

# searches a prexisting tree, adds a node at first available space (according to BFS) and returns
# an array of search paths to all nodes represented as strings (including newly added node)
def AdderBFS(root):
    searchSeq = []
    found = False
    queue.append(root) # queue of nodes that must be searched

    while queue:
        p = queue.pop(0)
        
        if (p.data != "0"): # if node is root
            # add the path used to find this node to the sequence of search paths that will be returned by AdderBFS
            searchSeq.append(p.path) 

        if (p.left != None):
            queue.append(p.left) # add newly found node to queue of nodes to be searched
            if (p.data != "0"): # if node is root
                (p.left).path = p.path + (p.left.path) # update serach path used to find node by adding current node

        elif (p.left == None and found == False): # if a node must be added
            p.left = TreeNode("R")
            queue.append(p.left) # add newly created node to queue of nodes to be searched
            if (p.data != "0"): # if node is root
                (p.left).path = p.path + (p.left.path) # update serach path used to find node by adding current node
            found = True # a node no longer needs to be added (one already added)

        if (p.middle != None):
            queue.append(p.middle) # add newly found node to queue of nodes to be searched
            if (p.data != "0"): # if node is root
                (p.middle).path = p.path + (p.middle.path) # update serach path used to find node by adding current node

        elif (p.middle == None and found == False): # if a node must be added
            p.middle = TreeNode("P")
            queue.append(p.middle) # add newly created node to queue of nodes to be searched
            if (p.data != "0"): # if node is root
                (p.middle).path = p.path + (p.middle.path) # update serach path used to find node by adding current node
            found = True # a node no longer needs to be added (one already added)

        if (p.right != None):
            queue.append(p.right) # add newly found node to queue of nodes to be searched
            if (p.data != "0"):
                (p.right).path = p.path + (p.right.path) # update serach path used to find node by adding current node

        elif (p.right == None and found == False): # if a node must be added
            p.right = TreeNode("S")
            queue.append(p.right) # add newly created node to queue of nodes to be searched
            if (p.data != "0"):
                (p.right).path = p.path + (p.right.path) # update serach path used to find node by adding current node
            found = True # a node no longer needs to be added (one already added)

    # reset each node's search path so that the next search does not build on current search's paths
    queue.append(root)
    while queue:
        p = queue.pop(0)
        

        if (p.left != None):
            queue.append(p.left)
            if (p.data != "0"):
                (p.left).path = "R"

        if (p.middle != None):
            queue.append(p.middle)
            if (p.data != "0"):
                (p.middle).path = "P"

        if (p.right != None):
            queue.append(p.right)
            if (p.data != "0"):
                (p.right).path = "S"
    
    return searchSeq


# initialise variables that must only be initialised at the beginning of a match
if (input==""):
    # global variable to keep track of the levels
    depth=5
    move=0
    
    prev=None # global variable to keep track op opponets previous move

    rootC=TreeNode("0") # creating root for the tree that will be searched using DFS
    
    rootC.path=rootC # assign root's parent to be itself, to avoid pointing to a unititialised node 
    
    lastNodeAdded=rootC # variable to avoid having redundent searches of the tree take place

# tree builder for DFS, 
# a global variable called lastNodeAdded was created. This node is assigned in AdderDFS. This node is the last node added
# to the tree as well as the last move to be played in this round of the game. Nodes are added top to bottom, left to right
# first filling in the depth (equal to the number of moves) before filling in the breath (as in accordance to the DFS algorithm)
def AdderDFS(Node):

    global depth
    global lastNodeAdded
    global move

    if (move < depth):

        # build from top to bottom (downwards), left to right
        if (Node.left==None or Node.middle==None or Node.right==None):
            newNode=TreeNode("0")
        
            # add new node where there is a space available
            if (Node.left==None):
                Node.left=newNode
                newNode.data="R"
                newNode.path=Node
            elif (Node.middle==None):
                Node.middle=newNode
                newNode.data="P"
                newNode.path=Node
            elif (Node.right==None):
                Node.right=newNode
                newNode.data="S"
                newNode.path=Node

            # move down level
            move+=1
            lastNodeAdded = newNode
            
            # stop recursion to build from top down and also stop path before reach bottom
            return lastNodeAdded
        
        # recursive calls to go up a node
        move-=1
        return AdderDFS(Node.path)

    else:

        if (Node!= rootC):
            move-=1
            return AdderDFS(Node.path)


# use path data structure to add the path all the way from the most receitly added node up to the the root (add this path to a stack)
def DFS():

    global depth
    global move
    global prev
    global rootC
    global lastNodeAdded

    node=AdderDFS(lastNodeAdded)

    seq=""

    while (node!= rootC):
        seq=node.data+seq
        node=node.path

    return seq
################################################## END OF SEARCH STRUCTURES ########################################################


################################################## START OF GAMEPLAY FUNCTIONS #####################################################
# used to pass results from the chosen search algorithm into the code used to detect the breakpoint
def pickSearchAlgorithms(root): 
    global bfs_dfs

    seq=""

    if (bfs_dfs==1):
        seq=DFS()
    else:
        seq=(AdderBFS(root)).pop()

    return seq

if (input == ""): # start of new match
    # add and initialise new variables that will be used in match
    Seq = None #
    SeqTracker = 0      # variable used to iterate through Seq
    root = TreeNode("0")
    inputPrev = "N"     # will be used to store previous input from breakable.py (will be compared to input to detect repitition)
    BPoint = ""         # breakpoint
    BPointTracker = 0   # variable used to iterate through BPoint
    FoundBP = False     # whether or not the breakpoint has been found
    TryBP = False       # whether or not a sequence is being tested to see whether it is the breakpoint or not
    Repetition = False  # whether or not the sequence being tested has triggered breakable.py to repeat its output

    # start adding nodes that will be searched to tree
    Seq = pickSearchAlgorithms(root)    #assign Seq to be search path of selected search algorithm
    SeqTracker = 1
    output = Seq[0]  

else:

    if (input == inputPrev): # repitition detected
        if (SeqTracker == len(Seq) and len(Seq) > 1): # if whole of Seq has been iterated through (if end of Seq has been reached)
            SeqTracker = 0
            TryBP = True

        if (TryBP == True and SeqTracker == len(Seq)): 
            # if the possible breakpoint is being tested (and finished iterating) and causes input to repeat again
            # test of possible breakpoint was a success
            Repetition = True
            BPointTracker = 0
            BPoint = Seq
            FoundBP = True

            # no need to continue trying to find possible breakpoint,
            # because confirmed breakpoint has already been found, therefore reset these variables
            TryBP = False 
            SeqTracker = 0

            # try to win games while breakable.py is repeating its output
        if (input == "R"):
            output = "P"
        elif (input == "P"):
            output = "S"
        elif (input == "S"):
            output == "R"
        else:
            output = "R"

    elif (FoundBP == True): # breakpoint has been found and is now being used to win the game
        if (BPointTracker == len(BPointTracker)):
            BPointTracker = 0

        output = BPoint[BPointTracker]
        BPointTracker = BPointTracker + 1

    elif (TryBP == True): # possible breakpoint has been found and is now being tested
        if (SeqTracker < len(Seq)): # sequence still being iterated through
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1

        elif (SeqTracker == len(Seq) and Repetition == False): # false triggering of breakpoint
            # whole of potential breakpoint has been iterated through without triggering repetition
            TryBP = False
            # continue with search by adding new node to search tree
            SeqTracker = 0
            Seq = pickSearchAlgorithms(root)
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1

    elif (SeqTracker == len(Seq)): # SeqBFSTracker has already iterated through Seq
        # add new node to get new cannidate for breakpoint
        SeqTracker = 0 # reset iteration
        Seq = pickSearchAlgorithms(root)
        output = Seq[SeqTracker]
        SeqTracker = SeqTracker + 1

    else: # sequence still being iterated through without triggering anything
        output = Seq[SeqTracker]
        SeqTracker = SeqTracker + 1

inputPrev = input

################################################## END OF GAMEPLAY FUNCTIONS #######################################################


#################################################### START OF TESTS ################################################################
def displayTree(Node):
    global input
    input = ""

    if (Node==None or Node.left==None):
        return
    else:
        print(Node.data, " children are: ")


        if (Node.left!=None and Node.middle!=None and Node.right!=None):
            print(Node.left.data, Node.middle.data, Node.right.data)

        if (Node.left!=None and Node.middle!=None and Node.right==None):
            print(Node.left.data, Node.middle.data)

        if (Node.left!=None and Node.middle==None and Node.right==None):
            print(Node.left.data)

        displayTree(Node.left)
        displayTree(Node.middle)
        displayTree(Node.right)


def testDFS():
    global input
    input = ""

    global depth
    depth = 3
    seq=[]

    for i in range(9):
        # print(AdderDFS(rootC,rootC,0))
    #    print("check ",lastNodeAdded.data," parent ",lastNodeAdded.path.data)
    #    print()
       AdderDFS(lastNodeAdded)


def Test1R():
    global input
    input = ""

    root = createTree(2)

    BFS_out = BFS(root)

    print(BFS_out)
    print(BFS_out.pop())


def Test2R():
    global input
    input = ""

    root = createTree(2)

    AdderBFS_out = AdderBFS(root)

    print(AdderBFS_out)

    AdderBFS_out = AdderBFS(root)

    print(AdderBFS_out)

    AdderBFS_out = AdderBFS(root)

    print(AdderBFS_out)

    for i in range (0, 27):
        AdderBFS_out = AdderBFS(root)

    print(AdderBFS_out)

    lastElement = AdderBFS_out.pop() #search path of most recently added node
    print(lastElement) 

    print(lastElement[0]) #accessing each letter in search path so that we can pass it into breakable

    for j in range(0,len(lastElement)): #accessing all letters of string
        print(lastElement[j])


def Test3R():
    global input
    input = ""

    rootTemp = TreeNode("0")
    AdderBFS_out = AdderBFS(rootTemp)

    print(AdderBFS_out)

    print(AdderBFS(rootTemp))

    print(AdderBFS(rootTemp).pop())
    print(AdderBFS(rootTemp).pop())

# need to specify that input = "" at beginnning of code for this test to work
def Test4R():
    for j in range(0,15):
        print(DFS())
    

# Test1R()
# Test2R()
# Test3R()
# Test4R()
# testDFS()
# displayTree(rootC)
##################################################### END OF TESTS ###############################################################


    if (input == ""): # start of new match
        # add and initialise new variables that will be used in match
        Seq = None #
        SeqTracker = 0   # iteration variable
        root = TreeNode("0")
        inputPrev = "N"     # will be used to store previous input from breakable.py (will be compared to input to detect repitition)
        BPoint = ""         # breakpoint
        BPointTracker = 0   # iterative var
        FoundBP = False
        TryBP = False
        Repetition = False

        # start adding nodes that will be searched to tree
        Seq = pickSearchAlgorithms(root)
        SeqTracker = 1
        output = Seq[0]  

    else:

        if (input == inputPrev): # repitition detected
            if (SeqTracker == len(Seq) and len(Seq) > 1): # if whole of SeqBFS has been iterated through
                SeqTracker = 0
                TryBP = True

            if (TryBP == True and SeqTracker == len(Seq)): 
                # if the possible breakpoint is being tested (and finished iterating) and causes input to repeat again
                # test of possible breakpoint was a success
                Repetition = True
                BPointTracker = 0
                BPoint = Seq
                FoundBP = True

                # no need to continue trying because already confirmed breakpoint, therefore reset these variables
                TryBP = False 
                SeqTracker = 0

                # try to win games
            if (input == "R"):
                output = "P"
            elif (input == "P"):
                output = "S"
            elif (input == "S"):
                output == "R"
            else:
                output = "R"

        elif (FoundBP == True): # breakpoint has been found and is now being used to win the game
            if (BPointTracker == len(BPointTracker)):
                BPointTracker = 0

            output = BPoint[BPointTracker]
            BPointTracker = BPointTracker + 1

        elif (TryBP == True): # possible breakpoint has been found and is now being tested
            if (SeqTracker < len(Seq)): # sequence still being iterated through
                output = Seq[SeqTracker]
                SeqTracker = SeqTracker + 1

            elif (SeqTracker == len(Seq) and Repetition == False): # false triggering of breakpoint
                # whole of potential breakpoint has been iterated through without triggering repetition
                TryBP = False
                # continue with search by adding new node
                SeqTracker = 0
                Seq = pickSearchAlgorithms(root)
                output = Seq[SeqTracker]
                SeqTracker = SeqTracker + 1

        elif (SeqTracker == len(Seq)): # SeqBFSTracker has already iterated through Seq
            # add new node to get new cannidate for breakpoint
            SeqTracker = 0 # reset iteration
            Seq = pickSearchAlgorithms(root)
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1

        else: # sequence still being iterated through without triggering anything
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1
    
    inputPrev = input

    return output  

#################################################### START OF RESULTS ############################################################

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((RAW DATA))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

#//////////////////////////////////////////Breadth First Search//////////////////////////////////////////////

#================================== 20 Matches, 500 Rounds =====================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 20 matches per pairing.
# Running matches in 6 threads
# 20 matches run
# total run time: 0.98 seconds

# breakable.py: won 10.0% of matches (2 of 20)
#     won 26.6% of rounds (2659 of 10000)
#     avg score -94.0, net score -1881.0

# eai320_prac_1_5.py: won 90.0% of matches (18 of 20)
#     won 45.4% of rounds (4540 of 10000)
#     avg score 94.0, net score 1881.0
#===============================================================================================

#================================== 20 Matches, 1500 Rounds ====================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 20 matches per pairing.
# Running matches in 6 threads
# 20 matches run
# total run time: 1.83 seconds

# breakable.py: won 0.0% of matches (0 of 20)
#     won 23.7% of rounds (7106 of 30000)
#     avg score -408.1, net score -8161.0

# eai320_prac_1_5.py: won 100.0% of matches (20 of 20)
#     won 50.9% of rounds (15267 of 30000)
#     avg score 408.1, net score 8161.0
#===============================================================================================

#================================== 200 Matches, 1500 Rounds ===================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 200 matches per pairing.
# Running matches in 6 threads
# 200 matches run
# total run time: 13.50 seconds

# breakable.py: won 3.0% of matches (6 of 200)
#     won 24.2% of rounds (72557 of 300000)
#     avg score -401.9, net score -80376.0

# eai320_prac_1_5.py: won 96.5% of matches (193 of 200)
#     won 51.0% of rounds (152933 of 300000)
#     avg score 401.9, net score 80376.0
#==============================================================================================

#==================================  Matches,  Rounds ====================================

#===============================================================================================

#////////////////////////////////////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////Depth First Search////////////////////////////////////////////////
#================================== 20 Matches, 500 Rounds =====================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 20 matches per pairing.
# Running matches in 6 threads
# 20 matches run
# total run time: 0.88 seconds

# breakable.py: won 20.0% of matches (4 of 20)
#     won 28.3% of rounds (2833 of 10000)
#     avg score -79.1, net score -1582.0

# eai320_prac_1_5.py: won 80.0% of matches (16 of 20)
#     won 44.1% of rounds (4415 of 10000)
#     avg score 79.1, net score 1582.0
#===============================================================================================

#================================== 20 Matches, 1500 Rounds ====================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 20 matches per pairing.
# Running matches in 6 threads
# 20 matches run
# total run time: 1.48 seconds

# breakable.py: won 0.0% of matches (0 of 20)
#     won 27.7% of rounds (8308 of 30000)
#     avg score -295.3, net score -5906.0

# eai320_prac_1_5.py: won 100.0% of matches (20 of 20)
#     won 47.4% of rounds (14214 of 30000)
#     avg score 295.3, net score 5906.0
#===============================================================================================

#================================== 200 Matches, 1500 Rounds ===================================
# Pool 1: 1 bots loaded
# Pool 2: 1 bots loaded
# Playing 200 matches per pairing.
# Running matches in 6 threads
# 200 matches run
# total run time: 3.64 seconds

# breakable.py: won 11.0% of matches (22 of 200)
#     won 28.0% of rounds (27956 of 100000)
#     avg score -85.5, net score -17096.0

# eai320_prac_1_5.py: won 88.0% of matches (176 of 200)
#     won 45.1% of rounds (45052 of 100000)
#     avg score 85.5, net score 17096.0
#===============================================================================================

#==================================  Matches,  Rounds ====================================

#===============================================================================================

#///////////////////////////////////////////////////////////////////////////////////////////////////////////


#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

#(((((((((((((((((((((((((((((((((((((((((((((((((((((((SUMMARY)))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#/////////////////////////////////////COMPARISON OF SEARCH METHODS///////////////////////////////////////////

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


#(((((((((((((((((((((((((((((((((((((((((((((((((((((((CONCLUSION))))))))))))))))))))))))))))))))))))))))))))))))))))))

#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

##################################################### END OF RESULTS #############################################################