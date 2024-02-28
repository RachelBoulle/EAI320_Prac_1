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

# Global variable to keep track of the levels
depth=0
move=0
# Global variable to keep track op opponets previous move
prev=None
# Creating root for my tree
rootC= TreeNode("0")
# To avoid pointint to a none variable assign roots parent to be itself
rootC.path=rootC
#initialise
lastNodeAdded= rootC # varibale to avoid search


#tree builder for DFS, 
# a global variable called lastNodeAdded was created. This node is assigned in adderDFS. This node is the last node added
#to the tree as well as the last move to be played in this round of the game. nodes are added top to bottom, left to right
# first filling in the depth(equal to the number of moves) befor filling in the breath

# Maybe should change depth to always stop at 5 as repetition will max be 5?????????????????????????
# RESPONSE: That might be a good idea, but we also need the depth to be dynamic and only limited by memory (as per prac guide)
def AdderDFS(Node):

    global count
    global depth
    global lastNodeAdded
    global move

    # recursive case
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

    #base case 
    else:

        if (Node!= rootC):
            move-=1
            AdderDFS(Node.path)


# use path data structure to add the path all the way from the most receitly added node up to the the root (add this path 
#to a stack)
def DFS():

    node=lastNodeAdded
    seq=[]

    while (node!= rootC):
        seq.append(node.data)
        node=node.path

    return seq
################################################## END OF SEARCH STRUCTURES ########################################################

# def combined():
#     AdderDFS()
#     out = DFS()
#     return out

#///////////////////////////////////////////////////////////Rachel//////////////////////////////////////////////////////////////////

# SeqBFS = None #
# SeqBFSTracker = 0
# rootBFS = TreeNode("0")
# inputPrev = "N" #will be used to store previous input from breakable.py (will be compared to input to detect repitition)
# BPoint = ""
# BPointTracker = 0
# FoundBP = False
# TryBP = False
# Repetition = False

#This is very rough and all over the place!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def tempSolution():
    #be able to manipulate globle variables
    # global SeqBFS 
    # global SeqBFSTracker
    # global inputPrev
    # global BPoint
    # global BPointTracker
    # global FoundBP
    # global TryBP
    # global Repetition

    if (input == ""): #start of new match
        #add and initialise new variables that will be used in match
        SeqBFS = None 
        SeqBFSTracker = 0 #to iterate through SeqBFS
        rootBFS = TreeNode("0")
        inputPrev = "N" #will be used to store previous input from breakable.py (will be compared to input to detect repitition)
        BPoint = ""
        BPointTracker = 0 #to iterate through BPoint
        FoundBP = False
        TryBP = False
        
        #start adding nodes that will be searched to tree
        SeqBFS = AdderBFS(rootBFS)
        output = SeqBFS[SeqBFSTracker]
        SeqBFSTracker = SeqBFSTracker + 1  

    else:
        if (input == inputPrev): #repitition detected
            if (SeqBFSTracker == len(SeqBFS) and len(SeqBFS) > 1): #if whole of SeqBFS has been iterated through
                #breakpoint potentially found
                SeqBFSTracker = 0
                TryBP = True

            if (TryBP == True and SeqBFSTracker == len(SeqBFS)): 
                #if the possible breakpoint is being tested (and finished iterating) and causes input to repeat again
                #test of possible breakpoint was a success
                Repetition = True
                BPointTracker = 0
                BPoint = SeqBFS
                FoundBP = True

                #no need to continue trying because already confirmed breakpoint, therefore reset these variables
                TryBP = False 
                SeqBFSTracker = 0

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
            if (SeqBFSTracker < len(SeqBFS)): #sequence still being iterated through
                output = SeqBFS[SeqBFSTracker]
                SeqBFSTracker = SeqBFSTracker + 1

            elif (SeqBFSTracker == len(SeqBFS) and Repetition == False): #false triggering of breakpoint
                #whole of potential breakpoint has been iterated through without triggering repetition
                TryBP = False
                #continue with search by adding new node
                SeqBFSTracker = 0
                SeqBFS = AdderBFS(rootBFS)
                output = SeqBFS[SeqBFSTracker]
                SeqBFSTracker = SeqBFSTracker + 1

        elif (SeqBFSTracker == len(SeqBFS)): #SeqBFSTracker has already iterated through SeqBFS
            #add new node to get new cannidate for breakpoint
            SeqBFSTracker = 0 #reset iteration
            SeqBFS = AdderBFS(rootBFS)
            output = SeqBFS[SeqBFSTracker]
            SeqBFSTracker = SeqBFSTracker + 1

        else: #sequence still being iterated through without triggering anything
            output = SeqBFS[SeqBFSTracker]
            SeqBFSTracker = SeqBFSTracker + 1
    
    inputPrev = input

#///////////////////////////////////////////////////////////Carli//////////////////////////////////////////////////////////////////

#use search algorithms to search for breaksequence
def SearchForBreak():
# temperary variable--------------------------------------------------------------------------------------
    bot2Prev=None # the opponents previous know move that was played, to get form scrip
    play=None     # what we play in this round
# --------------------------------------------------------------------------------------------------------
    if (bfs_dfs == 0):
        print() #temp fix to an error REMOVE LATER!!!!!!!!!!!!!!

    elif (bfs_dfs == 1):
        # maybe add an option for bfs!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!----Ask Racheal
            #Rachel: I added the if statement (:
        tempbreakseq=DFS()
        breakseq= None

        while (tempbreakseq.empty==False):
            # input to game // don't know how that interfaces exactly, what do i assign
            play=tempbreakseq.pop()

            # if an accidental breack sequence is detected
            if (prev==bot2Prev):
                # Use accidental break to obtain point and resume search for break sequence one break end
                while (prev==bot2Prev):
                    if (prev=="R"):
                        play="P"
                    elif (prev=="P"):
                        play="S"
                    else:
                        play="R"
    # asign bot2Prev as new value!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
            
            #Reassign tempbreakseq to start the search again, starting the interupted step again
            tempbreakseq=DFS()

# Check when previous is given to us for checking might need to change prev assignment to happen earlier!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
     # check if sequence caused a repeat
    if (prev==bot2Prev):
        breakseq==DFS()
        return breakseq
    else:
        prev=bot2Prev
        # return none to indicate that break sequence had not been found

        return None

def Play():
# temperary variable--------------------------------------------------------------------------------------
    bot2Prev=None # the opponents previous know move that was played, to get form scrip
    play=None     # what we play in this round
# --------------------------------------------------------------------------------------------------------
    
    breakseq=None
    loopbreak=None

    # check if breaksequenc was found
    while (breakseq==None): #Rachel: I'm a bit confused on how this will be entered since breakseq is initialized to None
        AdderDFS(lastNodeAdded)
        breakseq=SearchForBreak
        loopbreak=breakseq

#///////////////////////////////////begining of while game runs loop/////////////////---check for endless loop?
    while (loopbreak.empty==False):
        play=loopbreak.pop

        if (prev=="R"):
            play="P"
        elif (prev=="P"):
            play="S"
        else:
            play="R"

        while (prev==bot2Prev):
                    if (prev=="R"):
                        play="P"
                    elif (prev=="P"):
                        play="S"
                    else:
                        play="R"
        
    loopbreak=breakseq
# asign bot2Prev as new value!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# /////////////////////////////////////////////////////end of loop to put in///////////////////////////////////////////////

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
    

# ////////////////////////////////////////////RESULT//////////////////////////////////////////////////////////