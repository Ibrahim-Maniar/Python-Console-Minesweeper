# MINESWEEPER

# imports
import Grid  
import Input

vals = {}

EASY = 9,9
MEDIUM = 11,12
HARD = 13,15
INSANE = 15,20

height, width = MEDIUM # grid size (CHANGEABLE, recommended to use easy, medium and hard values but you can try others. Under 9X9 is unrecommended. Do not use anything past 26X99)
                    
for i in range(height):
    for i in range(width):             # values of tiles initialisation
        vals[height, width] = ""


Board = Grid.Board(height, width, vals) # Board Class initialisation

grid = Board.makeGrid()  # initialises the grid


Display = Grid.Display(height,width, grid) # Display Class initialisation


Display.display()
print("Enter a tile. First tile is always safe. e.g A1 or D3.\n")      # first coordinates input 
rawfcoords = input()
fcoords = Input.format(rawfcoords, height,width)


while fcoords == -1:        # first coordinates fallback
    Display.display()
    rawfcoords = input("Those coordinates were not valid. Try again.\n")
    fcoords = Input.format(rawfcoords, height, width)


vals[tuple(fcoords)] = 0     

totalMines = height*width // 8 # Used to decide when player wins (CHANGEABLE, see line 40, 83)
mines = []
for i in range(height*width//8):  # Amount of mines in comparison to grid size (CHANGEABLE, see line 38, 83)

    coordinates = (Board.initialiseMines(fcoords))    # mine initialisation (ignoring first coordinates)

    if coordinates == -1: continue # fallback if mine is not valid

    mines.append(coordinates) 
    vals[coordinates[0], coordinates[1]] = "M" # mine value



vals = Board.initialiseNums(mines)  # tile values from mines


Board.floodFill(fcoords, grid)  # flood fill for values of 0

Display.display() # displays and formats the grid on the terminal


# game loop

while True:


    rawcoords = input("")
    coords = Input.format(rawcoords, height, width) # validates + cleans input
    
    if coords == -1:  # fall back for invalid input
        Display.display()
        print("Those coordinates were not valid. Try again.") 
        continue 

    grid[coords[0]][coords[1]] = vals[tuple(coords)]   # if  valid coordinates it uncovers that tile

    if vals[tuple(coords)] == 0:
        Board.floodFill(coords, grid)    # if the tile is 0 it runs a flood fill to uncover all connected 0 tiles 

    Display.display()  # displays grid with new tile

    mineCount = 0      
    for row in grid:
        for i in row:       # checks amount of empty space in the grid
            if i == "*":
                mineCount += 1

    if mineCount == totalMines: # amount of empty spaces (mines) before game ends (CHANGEABLE, see line 38, 40)
        Display.endGame(mines)          # once empty space == amount of mines the player wins as theyve unvcovered all other tiles
        print("YOU WIN!!")
        break



    if tuple(coords) in mines:
        Display.endGame(mines)           # if the tile is a mine the player loses
        print("GAME OVER!!")
        break