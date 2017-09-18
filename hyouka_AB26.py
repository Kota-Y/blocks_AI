import piece5B26
import numpy as np

def hyouka_A(board,hand):
    length=(len(hand))
    if length==0:
        return

    board1=np.arange(25).reshape(5,5)#eleボードとピースを足したボード
    board2=np.arange(25).reshape(5,5)#ボードの5*5の要素element
    
    result = []
    thebest = 0

    for t in range(0,length):
        x = hand[t][0]
        y = hand[t][1]
        piece = piece5B26.ex_pieces[hand[t][2]]
        
        board1=board[x-2:x+3,y-2:y+3]
       # print(board1)
       # print(piece)
        board2=board1*piece
        result.append(np.sum(board2))
            
    herepoint = np.array(result)

    return herepoint
