from random import randint

from minesweeper import ROW_SIZE, NUMBER_OF_TILES, NUMBER_OF_MINES

def testDisplay(board):
    """ Display Grid """
    grid = board.grid
    print("\n  MINE PLACEMENT")
    row = ""
    for index in range(len(grid)):
        if grid[index].containsMine:
            row += "* "
        else:
            row += grid[index].displayCharacter + " "
        if (index+1) % ROW_SIZE == 0:
            print(row)
            row = ""

    """ Display Neighbor Count """
    print("\n NEIGHBORING MINES")
    row = ""
    for index in range(len(grid)):
        row += str(grid[index].neighboringMineCount) + " "
        if (index+1) % ROW_SIZE == 0:
            print(row)
            row = ""

def testClearNeighbors(board):
    grid = board.grid
    print("\n  INITIAL BOARD")
    board.displayGrid()
    for _ in range(100):
        randomIndex = randint(0,(NUMBER_OF_TILES-1))
        if grid[randomIndex].containsMine:
            continue
        board.clearNeighbors(randomIndex)
    print("\n CLEAR NEIGHBORS")
    board.displayGrid()
