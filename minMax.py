from tictactoe import *

class AI:
    def __init__(self, player):
        self.player = player
        if player == State.cross():
            enemy = State.circle()
        else:
            enemy = State.cross()
        self.enemy = enemy
        
def __minMax(player, enemy, board, currScore):
    state = board.checkGameState()
    if state == player.player:
        return ([0, 0], currScore+10)
    if state == player.enemy:
        return ([0, 0], currScore-10)
    elif state == "draw":
        return ([0, 0], currScore)
        
    moves = board.getEmptyBox()
    bestScores = [0]*len(moves)
    
    for i in range(len(moves)):
        copy = board.deepCopy()
        copy.setBox(moves[i][0], moves[i][1], player.player)
        minMaxRes = __minMax(enemy, player, copy, currScore)
        bestScores[i] = -minMaxRes[1]
    
    bestIndex = bestScores.index(max(bestScores))
    
    return(moves[bestIndex], bestScores[bestIndex])

def minMax(player, enemy, board):
    return __minMax(player, enemy, board, 0)[0]