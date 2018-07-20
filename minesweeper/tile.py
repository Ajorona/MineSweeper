
class Tile():
    """ A single tile in the minesweeper grid. contains the following attributes:

    displayCharacter: character to display in the minesweeper grid.
    isCovered: Has the mine been selected to be cleared by the user.
    containsMine: Does the tile contain a mine.
    neighboringMineCount: How many of the 8 tiles adjacent contain a mine?
    """
    def __init__(self, displayCharacter):
        self.displayCharacter = displayCharacter
        self.isCovered = True
        self.containsMine = False
        self.neighboringMineCount = 0
