
class TreeNode:
    def __init__(self, data):
        self.data = data             #"R", "P" or "S"
        self.left = None             #"R"
        self.middle = None           #"P"
        self.right = None            #"s"
        self.path = data


def createTree(depth):
    root = buildTree(depth)
    return root

def buildTree(depth):
    if (depth < 0):
        return
    newNode = TreeNode("0")
    if (depth > 0):
        newNode.left = buildTree(depth - 1)
        (newNode.left).data = "R"
        (newNode.left).path = "R"

        newNode.middle = buildTree(depth - 1)
        (newNode.middle).data = "P"
        (newNode.middle).path = "P"

        newNode.right = buildTree(depth - 1)
        (newNode.right).data = "S"
        (newNode.right).path = "S"
    return newNode
    
queue = []
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

root = createTree(2)

BFS_out = BFS(root)

print(BFS_out)

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

AdderBFS_out = AdderBFS(TreeNode("0"))

print(AdderBFS_out)