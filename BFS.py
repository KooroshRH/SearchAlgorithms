from array import *
import re
from copy import copy, deepcopy
import numpy as np

createdNodes = 0

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

class Node:
    def __init__(self, parent, board, depth, x, y):
        self.parent = parent
        self.board = board
        self.childs = []
        self.depth = depth
        self.x = x
        self.y = y

    def getHValue(self):
        decreaseRows = 0
        oneColorRows = 0
        for row in self.board:
            if len(row) == 0:
                decreaseRows = decreaseRows + 1
                oneColorRows = oneColorRows + 1
                continue
            isDecrease = True
            isOneColor = True
            rowColor = row[0].color
            key = pow(10, 5)
            for card in row:
                if card.number >= key:
                    isDecrease = False
                if card.color != rowColor:
                    isOneColor = False
                key = card.number
            if isDecrease:
                decreaseRows = decreaseRows + 1
            if isOneColor:
                oneColorRows = oneColorRows + 1
        return -1 * (decreaseRows + oneColorRows - self.depth)

def getInput(rowCount):
    rootBoard = []
    for i in range(int(rowCount)):
        boardRow = []
        j = 0
        for card in input().split():
            if card == "#":
                break
            cardInfo = re.compile("([0-9]+)([a-zA-Z]+)").match(card).groups()
            boardRow.insert(j, Card(cardInfo[1], int(cardInfo[0])))
            j = j + 1
        rootBoard.insert(i, boardRow)
    return rootBoard

def isTarget(node):
    for row in node.board:
        if len(row) == 0:
            continue
        rowColor = row[0].color
        key = pow(10, 5)
        for card in row:
            if row.index(card) == 0:
                continue
            if card.color != rowColor or card.number > key:
                return False
            else:
                key = card.number
    return True

def makeChilds(node):
    childs = []
    for rowIndex in range(len(node.board)):
        if len(node.board[rowIndex]) == 0:
            continue
        lastCard = node.board[rowIndex][len(node.board[rowIndex]) - 1]
        for targetRowIndex in range(len(node.board)):
            if rowIndex == targetRowIndex:
                continue
            if len(node.board[targetRowIndex]) != 0:
                targetLastCard = node.board[targetRowIndex][len(node.board[targetRowIndex]) - 1]
            if len(node.board[targetRowIndex]) == 0 or lastCard.number < targetLastCard.number:
                childBoard = deepcopy(node.board)
                removingCard = childBoard[rowIndex].pop(len(childBoard[rowIndex]) - 1)
                childBoard[targetRowIndex].append(removingCard)
                childs.append(Node(node, childBoard, node.depth + 1, rowIndex + 1, targetRowIndex + 1))
    return childs

def printNode(node):
    print("-------------------")
    for row in node.board:
        string = ""
        for card in row:
            string = string + str(card.number) + card.color + " "
        if string == "":
            print("#")
        else:
            print(string)
    print("-------------------")

def isContain(nodeList, node):
    for newNode in nodeList:
        isEqual = True
        for rowIndex in range(len(newNode.board)):
            if len(newNode.board[rowIndex]) != len(node.board[rowIndex]):
                isEqual = False
                break
            for cardIndex in range(len(newNode.board[rowIndex])):
                nodeCard = node.board[rowIndex][cardIndex]
                newCard = newNode.board[rowIndex][cardIndex]
                if (newCard.number != nodeCard.number) or (newCard.color != nodeCard.color):
                    isEqual = False
                    break
        if isEqual:
            return True
    return False

def bfsSearch(root):
    frontier = [root]
    explored = [root]
    if isTarget(root):
        return root, len(explored)
    while True:
        if len(frontier) == 0:
            return None, len(explored)
        node = frontier.pop(0)
        node.childs = makeChilds(node)
        global createdNodes
        createdNodes += len(node.childs)
        for child in node.childs:
            if not isContain(explored, child) and not isContain(frontier, child):
                if isTarget(child):
                    return child, len(explored)
                frontier.append(child)
                explored.append(child)

def showResults(target, exploredNodes):
    if target is None:
        print("We reach to no target in " + str(exploredNodes))
        return
    print("Target is :")
    printNode(target)
    print("Target depth is " + str(target.depth))
    solution = []
    currentNode = target
    while True:
        if currentNode.parent is None:
            break;
        solution.append(currentNode)
        currentNode = currentNode.parent
    solution.reverse()
    for node in solution:
        print("Move from " + str(node.x) + "th row to " + str(node.y) + "th row")
    print("Explored nodes are " + str(exploredNodes))
    print("Created nodes are " + str(createdNodes))

if __name__ == "__main__":
    inputString = input()
    rowCount = inputString.split()[0]
    colorCount = inputString.split()[1]
    maxNum = inputString.split()[2]

    rootBoard = getInput(rowCount)
    root = Node(None, rootBoard, 0, None, None)

    target, exploredNodes = bfsSearch(root)
    showResults(target, exploredNodes)