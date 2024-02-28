# EAI 320 Practical 1
# Group 5
# Carli Jansen van Rensburg u22493990
# Rachel Boulle u22523830

# global variable for choosing wheter to use BFS or DFS
    # BFS: bfs_dfs=0
    # DFS: bfs_dfs=1
bfs_dfs=0

# define the nodes which tree consiste of, will be used for search tree
class TreeNode:
    def __init__(self, data):
        self.data = data             #"R", "P" or "S"    // saves data of the move
        self.left = None             #"R"                // link
        self.middle = None           #"P"                // link   
        self.right = None            #"s"                // link
        self.path = data


# //////////////////////////////////////////////////Rachel///////////////////////////////////////////////////////////////////////
# global variable used in BFS and AdderBFS
queue = []

# used to test searching algorithms
def createTree(depthL):
    root = buildTree(depthL)
    return root

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

    # reset each node's search path so that the next search not build on current search's paths
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

def AdderBFS(root):
    searchSeq = []
    found = False
    queue.append(root)

    while queue:
        p = queue.pop(0)
        
        if (p.data != "0"):
            searchSeq.append(p.path)

        if (p.left != None):
            queue.append(p.left)
            if (p.data != "0"):
                (p.left).path = p.path + (p.left.path)
            # print("here 1: ", (p.left).path, p.path)

        elif (p.left == None and found == False):
            p.left = TreeNode("R")
            queue.append(p.left)
            if (p.data != "0"):
                (p.left).path = p.path + (p.left.path)
            found = True
            # print("HERE 1")

        if (p.middle != None):
            queue.append(p.middle)
            if (p.data != "0"):
                (p.middle).path = p.path + (p.middle.path)
            # print("here 2: ", (p.middle).path, p.path)

        elif (p.middle == None and found == False):
            p.middle = TreeNode("P")
            queue.append(p.middle)
            if (p.data != "0"):
                (p.middle).path = p.path + (p.middle.path)
            found = True
            # print("HERE 2")

        if (p.right != None):
            queue.append(p.right)
            if (p.data != "0"):
                (p.right).path = p.path + (p.right.path)
            # print("here 3: ", (p.right).path, p.path)

        elif (p.right == None and found == False):
            p.right = TreeNode("S")
            queue.append(p.right)
            if (p.data != "0"):
                (p.right).path = p.path + (p.right.path)
            found = True
            # print("HERE 3")

    # reset each node's search path so that the next search not build on current search's paths
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


#///////////////////////////////////////////////Carli//////////////////////////////////////////////////////////////////////

#!!!!!!!!!!!!!!!!!!!!!!!!!!!maybe don't make these global if you don't want them to be initialized each round (not sure how rpsrunner works tho)

if (input==""):
    # Global variable to keep track of the levels
    depth
    move
    # Global variable to keep track op opponets previous move
    prev
    # Creating root for my tree
    rootC
    # To avoid pointint to a none variable assign roots parent to be itself
    rootC.path
    #initialise
    lastNodeAdded # varibale to avoid search


#tree builder for DFS, 
# a global variable called lastNodeAdded was created. This node is assigned in adderDFS. This node is the last node added
#to the tree as well as the last move to be played in this round of the game. nodes are added top to bottom, left to right
# first filling in the depth(equal to the number of moves) befor filling in the breath

# Maybe should change depth to always stop at 5 as repetition will max be 5?????????????????????????
# RESPONSE: That might be a good idea, but we also need the depth to be dynamic and only limited by memory (as per prac guide)
def AdderDFS(Node):

    global depth
    global lastNodeAdded
    global move

    if (move < depth):
       

        # Build first from left to right, downwards.
        if (Node.left==Node or Node.middle==None or Node.right==None):
            newNode=TreeNode("0")
        
            # add new nodes
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
            lastNodeAdded= newNode
            
            # stop recursion to build from top down and also stop path before reach bottom
            return lastNodeAdded
        
        # recursive calls to go up a node
        move-=1
        AdderDFS(Node.path)

    else:

        if (Node!= rootC):
            move-=1
            AdderDFS(Node.path)


# use path data structure to add the path all the way from the most receitly added node up to the the root (add this path 
#to a stack)
def DFS():

    global depth
    global move
    global prev
    global rootC
    global lastNodeAdded


    if (input==""):
        depth=5
        move=0
        prev=None
        rootC= TreeNode("0")
        rootC.path=rootC
        lastNodeAdded= rootC

    node=AdderDFS(lastNodeAdded)

    seq=""

    while (node!= rootC):
        seq+=node.data
        node=node.path

    return seq
################################################## END OF SEARCH STRUCTURES ########################################################

#///////////////////////////////////////////////////////////Rachel//////////////////////////////////////////////////////////////////

#This is very rough and all over the place!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def tempSolution():



    if (input == ""): #start of new match
        #add and initialise new variables that will be used in match
        Seq = None #
        SeqTracker = 0   #iteration var
        root = TreeNode("0")
        inputPrev = "N"     # will be used to store previous input from breakable.py (will be compared to input to detect repitition)
        BPoint = ""         # breakpoint
        BPointTracker = 0   # iterative var
        FoundBP = False
        TryBP = False

# Should repetiotion be initialise???????????????????????????????????????????????????????????????????????

        #start adding nodes that will be searched to tree
        Seq = pickSearchAlgorithms(root)
        SeqTracker = 1
        output = Seq[0]  

    else:

        if (input == inputPrev): #repitition detected
            if (SeqTracker == len(Seq) and len(Seq) > 1): #if whole of SeqBFS has been iterated through
                SeqTracker = 0
                TryBP = True

            if (TryBP == True and SeqTracker == len(Seq)): 
                #if the possible breakpoint is being tested (and finished iterating) and causes input to repeat again
                #test of possible breakpoint was a success
                Repetition = True
                BPointTracker = 0
                BPoint = Seq
                FoundBP = True

                #no need to continue trying because already confirmed breakpoint, therefore reset these variables
                TryBP = False 
                SeqTracker = 0

                #Try to win games
            if (input == "R"):
                output = "P"
            elif (input == "P"):
                output = "S"
            elif (input == "S"):
                output == "R"
            else:
                output = "R"

        elif (FoundBP == True): #breakpoint has been found and is now being used to win the game
            if (BPointTracker == len(BPointTracker)):
                BPointTracker = 0

            output = BPoint[BPointTracker]
            BPointTracker = BPointTracker + 1

        elif (TryBP == True): #possible breakpoint has been found and is now being tested
            if (SeqTracker < len(Seq)): #sequence still being iterated through
                output = Seq[SeqTracker]
                SeqTracker = SeqTracker + 1

            elif (SeqTracker == len(Seq) and Repetition == False): #false triggering of breakpoint
                #whole of potential breakpoint has been iterated through without triggering repetition
                TryBP = False
                #continue with search by adding new node
                SeqTracker = 0
                Seq = pickSearchAlgorithms(root)
                output = Seq[SeqTracker]
                SeqTracker = SeqTracker + 1

        elif (SeqTracker == len(Seq)): #SeqBFSTracker has already iterated through Seq
            #add new node to get new cannidate for breakpoint
            SeqTracker = 0 #reset iteration
            Seq = pickSearchAlgorithms(root)
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1

        else: #sequence still being iterated through without triggering anything
            output = Seq[SeqTracker]
            SeqTracker = SeqTracker + 1
    
    inputPrev = input

    return output

#///////////////////////////////////////////////////////////Carli//////////////////////////////////////////////////////////////////

def pickSearchAlgorithms():
    global bfs_dfs

    seq=""

    if (bfs_dfs==1):
        seq=DFS()
    else:
        seq=BFS

    return seq

########################################### BEGINNING OF TESTS ##########################################################
# ////////////////////////////////////////////////TESTS Carli///////////////////////////////////////////////////
def displayTree(Node):

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

    global depth
    depth = 3
    seq=[]

    for i in range(9):
        # print(AdderDFS(rootC,rootC,0))
    #    print("check ",lastNodeAdded.data," parent ",lastNodeAdded.path.data)
    #    print()
       AdderDFS(lastNodeAdded)


# testDFS()
# displayTree(rootC)
# print(DFS()) #Added by Rachel

# //////////////////////////////////////////////TESTS Rachel/////////////////////////////////////////////////
def Test1R():
    root = createTree(2)

    BFS_out = BFS(root)

    print(BFS_out)
    print(BFS_out.pop())


def Test2R():


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
    AdderBFS_out = AdderBFS(TreeNode("0"))

    print(AdderBFS_out)

# Test1R()
# Test2R()
# Test3R()
    
# ///////////////////////////////////////////Runner testing////////////////////////////////////////////////////
    
output=tempSolution()   

# ////////////////////////////////////////////RESULT//////////////////////////////////////////////////////////