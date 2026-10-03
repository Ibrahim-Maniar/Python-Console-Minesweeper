import random
import os

class Board:

    def __init__(self,height, width, vals):
        self.height = height
        self.width = width
        self.vals = vals


    def makeGrid(self): # initialises the grid with 0 numbers or mines
        grid = []
        for i in range(self.height):  #rows
            grid.append([])  # new array
            for j in range(self.width): #cols

                grid[-1].append("*") # defines displayed grid as empty space

        return grid 
    
    
    mines = []
    def initialiseMines(self, first): # initialises mines in the grid 
        
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1], [0,0], [0,1],[1,-1],[1,0],[1,1]] # directions to check (8 directional)
        randomh = random.randrange(self.height) # random value for row
        randomw = random.randrange(self.width) # random value for collumn

        for dir in dirs: # checks each direction
            
            if (first[0] + dir[0], first[1] + dir[1]) == (randomh, randomw): # makes sure that the mine isn't near the first tile to give the player a fairer start
                self.initialiseMines(first) # recursion to pick a new mine
                return -1 # end current function

        if [randomh, randomw] in self.mines: # makes sure that it isn't redefining a mine
            self.initialiseMines(first)
            return -1 

        else: #  if mine is approved

            self.mines.append((randomh, randomw))  # mine is added to a list of mines (coordinates)
            
            return randomh, randomw # returns coordinates
        

    def initialiseNums(self, mines):  # initialises the tile values using mine positions
        
        nums = []
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]] # directions to check

        for row in range(self.height):
                for col in range(self.width):
                    num = 0
                    for dir in dirs:
                        if (row + dir[0], col + dir[1]) in mines: # if a row in immediate vicinity
                                            
                            num += 1 # mine count (value of tile) + 1

                    self.vals[row, col] = num  # update values dictionary 
                    
        return self.vals
    
    
    seen = []
    def floodFill(self, coords, grid): # fills all tiles that have a value of 0 

        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        row = coords[0]
        col = coords[1]

        for dir in dirs:
           
            try:

                grid[row + dir[0]][ col + dir[1]] = self.vals[tuple([row + dir[0], col + dir[1]])]

                if self.vals[ tuple( [row + dir[0], col + dir[1]] ) ] == 0 and (row+dir[0],col+dir[1]) not in self.seen:  #  checks if next tile is in the grid and is 0 before spreading
                    self.seen.append((row+dir[0],col+dir[1]))
                    
                    self.floodFill( [ row + dir[0], col + dir[1] ] , grid)
                   

            except:
                pass
                            

class Display():
    def __init__(self, height, width, grid):
        self.grid = grid
        self.height = height
        self.width = width

    def rgb_text(self, r, g, b, text):
        # text color 
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def display(self):
        os.system('clear')
        print("", end="     ")
        for i in range(self.width):
            if i < 9:
                print(i+1, end=" "*4)
            else:
                print(i+1, end=" "*3)
        print()
        for i,v in enumerate(self.grid):

            hindex = chr( ord("@") + (i+1) ) 
            print("\n", end= str(hindex) + "    ")
            for j in v:
                if j !=  "*":
                    
                    if j == "M":
                        print(self.rgb_text(255,255,255, j), end="    ")
                    else:
                        if j == 0:
                            print(self.rgb_text(100,100,100,j), end="    ")
                        if j == 1:
                            print(self.rgb_text(0,0,255,j), end="    ")
                        if j == 2:
                            print(self.rgb_text(0,128,0,j), end="    ")
                        if j == 3:
                            print(self.rgb_text(255,0,0,j), end="    ")
                        if j == 4:
                            print(self.rgb_text(0,0,128,j), end="    ")
                        if j == 5:
                            print(self.rgb_text(128,0,0,j), end="    ")
                        if j == 6:
                            print(self.rgb_text(0,128,128,j), end="    ")
                        if j == 7:
                            print(self.rgb_text(255,0,0,j), end="    ")
                        if j == 8:
                            print(self.rgb_text(128,128,128,j), end="    ")
                
                else:
                    print("•", end="    ")

        print("\n\n")

    def showAll(self, vals):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                col = vals.get(((((row, col)))))


    def showMines(self, mineList):
        for i in mineList:
            self.grid[i[0]][i[1]] = "M"


    def endGame(self,mineList):
        
        self.showMines(mineList)
        self.display()  