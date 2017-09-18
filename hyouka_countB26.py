import piece5B26
import numpy as np

#合法手をピースの大きさごとに分けた配列として
#大きいピースの配列から返してくれるはずの関数
def hyouka_count(save_hand, next_hand):
    EXCEPT=10000
    length=(len(save_hand))
    
    if length==0:		
        return 0

    save_hand_5=[]#5ピースの配列
    save_hand_4=[]#4ピースの配列
    save_hand_3=[]#3ピースの配列
    save_hand_2=[]#2ピースの配列
    save_hand_1=[]#1ピースの配列

    nex_hand_5 = []
    nex_hand_4 = []
    nex_hand_3 = []
    nex_hand_2 = []
    nex_hand_1 = []

    for t in range(0,length):
        x = save_hand[t][0]
        y = save_hand[t][1]
        p = save_hand[t][2]

        piece=piece5B26.ex_pieces[save_hand[t][2]]

        #np.count_nonzeroでpiece内の0以外の要素を数える

        if np.count_nonzero(piece)==5:     
            save_hand_5.append([x,y,p])
            nex_hand_5.append(next_hand[t])

        elif np.count_nonzero(piece)==4:
            save_hand_4.append([x,y,p])
            nex_hand_4.append(next_hand[t])

        elif np.count_nonzero(piece)==3:
            save_hand_3.append([x,y,p])
            nex_hand_3.append(next_hand[t])

        elif np.count_nonzero(piece)==2:
            save_hand_3.append([x,y,p])
            nex_hand_3.append(next_hand[t])

        elif np.count_nonzero(piece)==1:
            save_hand_3.append([x,y,p])
            nex_hand_3.append(next_hand[t])
        
    if len(save_hand_5)!=0:
        return (save_hand_5, nex_hand_5)
    elif len(save_hand_4)!=0:
        return (save_hand_4, nex_hand_4)
    elif len(save_hand_3)!=0:
        return (save_hand_3, nex_hand_3)
    #elif len(save_hand_2)!=0:
    #    return (save_hand_2, nex_hand_2)
    #elif len(save_hand_1)!=0:
    #    return (save_hand_1, nex_hand_1)
    else:
        return 0
