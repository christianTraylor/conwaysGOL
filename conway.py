import numpy as np

class Cell():

    def __init__(self,row,col,status):
        self.row = row
        self.col = col
        self.status = status

    def check(self, board):
        count = 0
        possibilities = (
            (self.row-1,self.col-1), (self.row-1,self.col), (self.row-1,self.col+1), (self.row,self.col-1), 
            (self.row,self.col+1), (self.row+1,self.col-1), (self.row+1,self.col), (self.row+1,self.col+1) 
        )
        if self.status:
            for cord in possibilities:
                if (cord[0] < 10) and (cord[1] < 10) and (cord[0] > -1) and (cord[1] > -1):
                    if board[cord[0]][cord[1]].status == True:
                        count+=1
            if count == 2 or  count == 3:
                return self.row,self.col,True
            else:
                return self.row,self.col,False
        else:
            for cord in possibilities:
                if (cord[0] < 10) and (cord[1] < 10) and (cord[0] > -1) and (cord[1] > -1):
                    if board[cord[0]][cord[1]].status == True:
                        count+=1
            if count == 3:
                return self.row,self.col,True
            else:
                return self.row,self.col,False

    def __repr__(self):
        if self.status:
            return "."
        else:
            return "0"

class Board():
    #TODO: Change seed to work with user input
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.board = np.zeros((self.x, self.y), dtype=Cell)
        self.seed = int(np.random.randint(0,high=1000))

    def populate(self):
        np.random.seed(self.seed)
        for x in range(self.x):
            columnArr = np.random.randint(0,high=self.y,size=2)
            for y in range(self.y):
                if y in columnArr:
                    self.board[x][y] = Cell(x,y,True)
                else:
                    self.board[x][y] = Cell(x,y,False)

    def checkCells(self):
        tempBoard = np.zeros((self.x,self.y), dtype=Cell)
        for row in self.board:
            for col in range(len(row)):
                rowPos, colPos, status = row[col].check(self.board)
                tempBoard[rowPos][colPos] = Cell(rowPos,colPos,status)
        del self.board
        self.board = tempBoard

    def __repr__(self):
            return str(self.board)


board = Board(10,10)
board.populate()
print(board)
print()
print("1st gen")
board.checkCells()
print(board)

