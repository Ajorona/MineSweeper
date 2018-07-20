
from tile import Tile
from random import randint

from gamesettings import ROW_SIZE, NUMBER_OF_TILES, NUMBER_OF_MINES

class Board():
    """ Board class represents a board for the MineSweeper Game """
    def __init__(self):
        self.BOARD_CLEAR = False
        self.FREE_TILE_COUNT = NUMBER_OF_TILES - NUMBER_OF_MINES
        self.grid = [Tile('?') for _ in range(NUMBER_OF_TILES)]
        self.generateMines()
        self.calculateNeighboringMines()

    def generateMines(self):
        """ Places mines at random tile positions in the entire grid list """
        for _ in range(NUMBER_OF_MINES):
            minePlaced = False
            while not minePlaced:
                randomPosition = randint(0, (NUMBER_OF_TILES-1))
                if not self.grid[randomPosition].containsMine:
                    self.grid[randomPosition].containsMine = True
                    minePlaced = True

    def calculateNeighboringMines(self):
        """ Calculates the number of mines adjacent to each tile """
        for index, tile in enumerate(self.grid):
            checkUp = index > (ROW_SIZE-1)
            checkDown = index < (NUMBER_OF_TILES-ROW_SIZE)
            checkLeft = index % ROW_SIZE != 0
            checkRight = (index+1) % ROW_SIZE != 0

            checkULD = checkUp and checkLeft
            checkURD = checkUp and checkRight
            checkLLD = checkDown and checkLeft
            checkLRD = checkDown and checkRight

            if checkUp and self.grid[index-ROW_SIZE].containsMine:
                tile.neighboringMineCount += 1
            if checkDown and self.grid[index+ROW_SIZE].containsMine:
                tile.neighboringMineCount += 1
            if checkLeft and self.grid[index-1].containsMine:
                tile.neighboringMineCount += 1
            if checkRight and self.grid[index+1].containsMine:
                tile.neighboringMineCount += 1
            if checkULD and self.grid[index-ROW_SIZE-1].containsMine:
                tile.neighboringMineCount += 1
            if checkURD and self.grid[index-ROW_SIZE+1].containsMine:
                tile.neighboringMineCount += 1
            if checkLLD and self.grid[index+ROW_SIZE-1].containsMine:
                tile.neighboringMineCount += 1
            if checkLRD and self.grid[index+ROW_SIZE+1].containsMine:
                tile.neighboringMineCount += 1

        def cascade(self, index):
            """  Clears all mines that are adjacent to a given until a tile contained a mine is encountered. """
            if not self.grid[index].isCovered:
                return

            self.clearTile(index)
            if self.grid[index].neighboringMineCount != 0:
                return

            # Only move Up, Right, Left, and Down to clear neighbors
            checkUp    = index > (ROW_SIZE-1)
            checkDown  = index < (NUMBER_OF_TILES-ROW_SIZE)
            checkLeft  = (index % ROW_SIZE) != 0
            checkRight = ( (index+1) % ROW_SIZE) != 0

            if checkUp:
                self.cascade(index-ROW_SIZE)
            if checkDown:
                self.cascade(index+ROW_SIZE)
            if checkLeft:
                self.cascade(index-1)
            if checkRight:
                self.cascade(index+1)


    def cascadeOrClearOneMine(self, index):
        """ If no top, bottom, left, or right neighboring mines call cascadeMine, else clear one mine """
        requiredConditions = ( index > (ROW_SIZE-1), ( (index+1) % ROW_SIZE ) != 0,  index < NUMBER_OF_TILES-ROW_SIZE,  (index % ROW_SIZE) != 0)
        if False in requiredConditions:
            self.clearTile(index)
        else:
            self.cascade(index)


    def clearTile(self, index):
        """ Sets a tile in the grid as uncovered """
        self.grid[index].displayCharacter = str(self.grid[index].neighboringMineCount)
        self.grid[index].isCovered = False
        self.FREE_TILE_COUNT -= 1

    def checkTile(self, index):
        """ Checks a tile in the grid to determine if it contains a mine """
        status = {'boardClear' : False, 'containsMine' : False, 'isCovered' : True,  }
        if self.grid[index].containsMine:
            status['containsMine'] = True
            return status
        if not self.grid[index].isCovered:
            status['isCovered'] = False
        self.cascadeOrClearOneMine(index)
        if (self.FREE_TILE_COUNT <= 0):
            status['boardClear'] = True
        return status

    def displayGrid(self):
        """ Show all display characters of mines in grid as a square matrix """
        print("\n           ** LET'S GO **")
        row = ''
        for index in range(len(self.grid)):
            row += self.grid[index].displayCharacter + ' '
            if (index+1) % ROW_SIZE == 0:
                print(row)
                row = ''

    def displayMines(self):
        """ Show mine position in grid as square matrix """
        print("\n       ** MINE PLACEMENT **")
        row = ""
        for index in range(len(self.grid)):
            if self.grid[index].containsMine:
                row += "* "
            else:
                row += self.grid[index].displayCharacter + " "
            if (index+1) % ROW_SIZE == 0:
                print(row)
                row = ""

    def displayNeighbors(self):
        """ Show number of neighboring mines for each tile """
        print("\n        ** NEIGHBORING MINES **")
        row = ""
        for index in range(len(self.grid)):
            row += str(self.grid[index].neighboringMineCount) + " "
            if (index+1) % ROW_SIZE == 0:
                print(row)
                row = ""
