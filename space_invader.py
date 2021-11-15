"""This module simple simply contain the code to start the execution using an
instance of game.Game and tells it to start.
"""
from source import game 

if __name__ == '__main__':
    instance = game.Game()
    instance.start()
