
class Tile():
    ''' A single tile in the minesweeper grid '''
    def __init__(self, displayCharacter):
        self.displayCharacter = displayCharacter
        self.isCovered = True
        self.containsMine = False
        self.neighboringMineCount = 0
