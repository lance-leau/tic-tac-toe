from tictactoe import *
from minMax import *



board = tictactoe()
#board.setBox(1, 1, State.cross())

aiX = AI(State.cross())
aiO = AI(State.circle())

currPlayer = aiO
otherPlayer = aiX
while board.checkGameState() == State.blank():
    if currPlayer == aiX:
        currPlayer = aiO
        otherPlayer = aiX
    else:
        currPlayer = aiX
        otherPlayer = aiO
    
    board.prettyPrint()
    move = minMax(currPlayer, otherPlayer, board)
    board.setBox(move[0], move[1], currPlayer.player)
board.prettyPrint()
if not board.checkGameDraw():
    print("PLAYER", board.checkGameState(), "WON !")
else:
    print("GAME IS A DRAW")