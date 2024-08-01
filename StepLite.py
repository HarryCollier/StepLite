class node:
    def __init__(self, digits, history):
        self.digits = digits
        self.history = history

    def getChildrenFor1move(self, move, result):
        children = []
        for i in range(len(self.digits)-len(move)+1):
            if self.digits[i:i+len(move)] == move:
                newDigits = self.digits[:i] + result + self.digits[i+len(move):]
                children.append(node(newDigits, self.history+self.digits+"/"))

        return children

    def checkNotLooped(self):
        valid = True
        for i in self.history.split("/"):
            if self.digits == i:
                valid = False
        return valid



class frontier:
    def __init__(self, finishState):
        self.frontier = []
        self.finishState = finishState

    def add(self, node):
        self.frontier.insert(0, node)

    def remove(self):
        n = self.frontier[-1]
        self.frontier.pop(-1)
        return n

    def checkNodeInFrontier(self, n):
        valid = True
        for i in self.frontier:
            if n.digits == i.digits:
                valid = False
        return valid

    def solve(self, moves, results):
        while len(self.frontier) != 0:
            n = f.remove()
            if n.digits == self.finishState:
                return(n.digits, n.history)
            elif n.checkNotLooped and self.checkNodeInFrontier(n) and len(n.digits) < 10:
                children = []
                for i in range(len(moves)):
                    children.append(n.getChildrenFor1move(moves[i], results[i]))
                for i in children:
                    for j in i:
                        f.add(j)

        return "No solutions"




print("this program will find a way to get from one string of characters to another given a set of possible moves, aslong as the string is never longer than 9 characters during the process")
startingPoint = input("What is the starting point")
endPoint = input("What is the end point")
move = ""
result = ""
moves = []
results = []
print("press x at any point during these inputs to cancel a set of inputs, and x for both to stop inputting moves")
while move != "x" or result != "x":
    move = input("Enter a string of characters that can be used to replace another string")
    result = input("Enter what that string is replaced with")
    if move != "x" and result != "x":
        moves.append(move)
        results.append(result)


a = node(startingPoint, "")
f = frontier(endPoint)
f.add(a)
print(f.solve(moves, results))

