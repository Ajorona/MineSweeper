from board import Board
from utilities import clearCLI
from time import sleep

from gamesettings import ROW_SIZE, NUMBER_OF_TILES, NUMBER_OF_MINES

def welcomeDisplay():
    title = ['M', 'I', 'N', 'E', 'S', 'W', 'E', 'E', 'P', 'E', 'R']

    decorator = "===================================\n" \
                    + "\t{}\n" \
                    + "===================================="
    welcomeStr = ''
    for letter in title:
        welcomeStr += letter + ' '
        print(decorator.format(welcomeStr))
        sleep(0.1)
        clearCLI()
    print(decorator.format(welcomeStr))

def mainDisplay():
    title = ['M', 'I', 'N', 'E', 'S', 'W', 'E', 'E', 'P', 'E', 'R']

    welcomeStr = "===================================\n" \
                    + "\t M I N E S W E E P E R\n" \
                    + "===================================="
    print(welcomeStr)

class Game():
    def __init__(self):
        self.board = Board()
        self.GAME_OVER = False
        self.WIN = False

    def getUserChoice(self):
        while True:
            userIn = input("Please select a tile between 1 and 100")
            try:
                userIn = int(userIn)
            except ValueError:
                print("{} is invalid input, try again".format(userIn))
            if userIn in range(1,101):
                return userIn - 1

    def makeMove(self, index):
        status = self.board.checkTile(index)
        print(status)
        if status['containsMine']:
            return  True
        elif not status['isCovered']:
            print("You have already checked that tile, try again!")
            return False
        if status['boardClear']:
            self.WIN = True
            return True

    def welcomeAnimation(self):
        welcomeDisplay()
        self.board.displayMines()
        sleep(1)
        clearCLI()
        for _ in range(3):
            self.board.displayNeighbors()
            sleep(0.5)
            clearCLI()
            sleep(1)

    def gameDisplay(self):
        mainDisplay()
        self.board.displayGrid()

    def mainLoop(self):
        self.welcomeAnimation()
        while not self.GAME_OVER:
            self.gameDisplay()
            index = self.getUserChoice()
            self.GAME_OVER = self.makeMove(index)
            clearCLI()
        if self.WIN:
            print("YOU WON")
        else:
            print("YOU LOSE")

    def run(self):
        self.mainLoop()
