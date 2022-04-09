from decimal import Overflow
from tkinter import *
from functools import *
from random import *
import os
import sys


def clicked(i, j):

    if(currontIndex != []):
        n, m = currontIndex[0]
        gridButtosList[n][m].configure(bg=activeColor)
        currontIndex.pop()
    currontIndex.append([i, j])
    gridButtosList[i][j].configure(bg=currentColor)

def gridBorder(r, c, n):
    for i in range(r, n):
        l = []
        for j in range(c, n):
            if j not in spaceCheck:
                if i not in spaceCheck:
                    Grid.columnconfigure(root, i, weight=1)
                    Grid.rowconfigure(root, j, weight=1)
                    b = Button(root, text=" " if board[i][j] == 0 else board[i][j], font=elementFont, command=None if board[i][j] != 0 else partial(
                        clicked, i, j), bg=inactiveColor if board[i][j] != 0 else activeColor)
                    b.grid(row=i, column=j, padx=(space, padding) if j in spaceCheck else padding, pady=(space, padding) if i in spaceCheck else padding,
                           ipadx=5, ipady=5, sticky=N+S+E+W)
                    l.append(b)
                else:
                    Grid.columnconfigure(root, i, weight=1)
                    Grid.rowconfigure(root, j, weight=1)
                    b = Button(root, text=" " if board[i][j] == 0 else board[i][j], font=elementFont, command=None if board[i][j] != 0 else partial(
                        clicked, i, j), bg=inactiveColor if board[i][j] != 0 else activeColor)
                    b.grid(row=i, column=j, padx=(space, padding) if j in spaceCheck else padding, pady=(space, padding) if i in spaceCheck else padding,
                           ipadx=5, ipady=5, sticky=N+S+E+W)
                    l.append(b)
            else:
                if i in spaceCheck:
                    Grid.columnconfigure(root, i, weight=1)
                    Grid.rowconfigure(root, j, weight=1)
                    b = Button(root, text=" " if board[i][j] == 0 else board[i][j], font=elementFont, command=None if board[i][j] != 0 else partial(
                        clicked, i, j), bg=inactiveColor if board[i][j] != 0 else activeColor)
                    b.grid(row=i, column=j, padx=(space, padding) if j in spaceCheck else padding, pady=(space, padding) if i in spaceCheck else padding,
                           ipadx=5, ipady=5, sticky=N+S+E+W)
                    l.append(b)
                else:
                    Grid.columnconfigure(root, i, weight=1)
                    Grid.rowconfigure(root, j, weight=1)
                    b = Button(root, text=" " if board[i][j] == 0 else board[i][j], font=elementFont, command=None if board[i][j] != 0 else partial(
                        clicked, i, j), bg=inactiveColor if board[i][j] != 0 else activeColor)
                    b.grid(row=i, column=j, padx=(space, padding) if j in spaceCheck else padding, pady=(space, padding) if i in spaceCheck else padding,
                           ipadx=5, ipady=5, sticky=N+S+E+W)
                    l.append(b)
        gridButtosList.append(l)

def gridUPDate(n):
    i, j = currontIndex[0]
    board[i][j] = n
    gridButtosList[i][j].configure(text=board[i][j])

def gridEntry():
    for i in range(boardSize):
        Grid.columnconfigure(root, i, weight=1)
        Grid.rowconfigure(root, boardSize, weight=1)
        Button(root, text=i+1, font=("Arial", 10), bg="#54d6f0", command=partial(
            gridUPDate, i+1)).grid(row=boardSize, column=i,
                                   pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)

def sudokuCheck(scoreCount):
    if soluation != board:
        submitButton.configure(bg='red')
        # TODO
        scoreCount -= 5
        score.configure(text=scoreCount)

    else:
        submitButton.configure(bg=currentColor)
        # TODO
        scoreCount += 10
        score.configure(text=scoreCount)

def sudokuBoardGenorator():
    base = int(boardSize/3)
    side = base*base

    def pattern(r, c):
        return (base*(r % base)+r//base+c) % side

    def shuffle(s):
        return sample(s, len(s))

    rBase = range(base)

    rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base*base+1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]

def sudokuProblemGenorator():
    base = int(boardSize/3)
    side = base*base

    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares), empties):
        board[p//side][p % side] = 0

def sudokuAutoComplete():
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != soluation[i][j]:
                board[i][j] = soluation[i][j]
                gridButtosList[i][j].configure(text=board[i][j])

def newGame():
    print('reload')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def menu():
    Button(root, text=" NEW ", font=("Arial", 12), bg="#54d6f0",
           command=partial(newGame)).grid(row=boardSize+2, column=0, columnspan=3,
                                          pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)
    
    submitButton.grid(row=boardSize+2, column=6, columnspan=3,
                      pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)

    Button(root, text=" AUTO ", font=("Arial", 12), bg="#54d6f0",
           command=sudokuAutoComplete).grid(row=boardSize+2, column=3, columnspan=3,
                                            pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)

    Label(root, text="Score:", font=("Arial", 15), justify="center").grid(row=boardSize+1, column=0, columnspan=2,
                                                                          pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)

    score.grid(row=boardSize+1, column=1, columnspan=8,
               pady=space, padx=padding, ipadx=5, ipady=5, sticky=N+S+E+W)

if __name__ == "__main__":
    scoreCount = 0
    padding = 1
    space = 15
    currontIndex = []
    inactiveColor = '#f59449'
    activeColor = 'white'
    currentColor = "#54FA9B"
    gridButtosList = []
    spaceCheck = []

    sizes = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    n = 2
    boardSize = sizes[n]
    if(sizes[n]-1 % 2 == 0):
        div = 2
    else:
        div = 3

    for i in range(sizes[n]):
        if (i % 3 == 0):
            spaceCheck.append(i)

    elementFont = ("Arial", int(boardSize/3) if int(boardSize/3) > 10 else 10)

    mainRoot = Tk()
    mainRoot.title("Sudoku Game")
    Grid.rowconfigure(mainRoot, 0, weight=1)
    Grid.columnconfigure(mainRoot, 0, weight=1)
    root = Frame(mainRoot)
    root.grid(row=0, column=0, sticky=N+S+E+W)

    score = Label(root, text=scoreCount, font=("Arial", 15), justify="center")
    submitButton = Button(root, text=" SUBMIT ", font=("Arial", 12), bg="#54d6f0",command=partial(sudokuCheck,scoreCount))

    board = sudokuBoardGenorator()
    soluation = []

    for i in board:
        l = []
        for j in i:
            l.append(j)
        soluation.append(l)

    sudokuProblemGenorator()

    gridBorder(0, 0, len(board))
    gridEntry()
    menu()
    root.mainloop()
