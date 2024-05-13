from Game import Game, GameError
from sys import stderr
from abc import ABC, abstractmethod
#import PySimpleGUI as sg

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        #While there is not winner
        while self._game.winner is None:
            print(self._game)
            try:
                row = int(input("Enter Row: "))
                col = int(input("Enter Column: "))
                self._game.play(row, col)
            except GameError as e:
                print(e, file=stderr)
        print("The winner was", self._game.winner)
        #Get input from user
        #Play the input into the game


class Gui(Ui):
    pass
