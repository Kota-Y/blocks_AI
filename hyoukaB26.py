import piece5B26
import numpy as np

def hyouka(pro_board,next_hand_ele):
    length=(len(next_hand_ele))
    if length==0:
        return
    
    add_board=np.arange(25).reshape(5,5)#eleボードとピースを足したボード
    ele_board=np.arange(25).reshape(5,5)#ボードの5*5の要素element

    result5=0
    result4=0
    result3=0
    result2=0
    result1=0

    re_t5=-1
    re_t4=-1
    re_t3=-1
    re_t2=-1
    re_t1=-1

    for t in range(0,length):
        x=next_hand_ele[t][0]
        y=next_hand_ele[t][1]

        piece=piece5B26.ex_pieces[next_hand_ele[t][2]]

        if np.count_nonzero(piece)==5:
            ele_board=pro_board[x-2:x+3,y-2:y+3]
            add_board=ele_board*piece
            fu_result5=np.sum(add_board)

            if fu_result5 >= result5:
                result5=fu_result5
                MAX=fu_result5
                re_t5=t

        if np.count_nonzero(piece)==4:
            ele_board=pro_board[x-2:x+3,y-2:y+3]
            add_board=ele_board*piece
            fu_result4=np.sum(add_board)

            if fu_result4 >= result4:
                result4=fu_result4
                MAX=fu_result4
                re_t4=t

        if np.count_nonzero(piece)==3:
            ele_board=pro_board[x-2:x+3,y-2:y+3]
            add_board=ele_board*piece
            fu_result3=np.sum(add_board)

            if fu_result3 >= result3:
                result3=fu_result3
                MAX=fu_result3
                re_t3=t

        if np.count_nonzero(piece)==2:
            ele_board=pro_board[x-2:x+3,y-2:y+3]
            add_board=ele_board*piece
            fu_result2=np.sum(add_board)

            if fu_result2 >= result2:
                result2=fu_result2
                MAX=fu_result2
                re_t2=t

        if np.count_nonzero(piece)==1:
            ele_board=pro_board[x-2:x+3,y-2:y+3]
            add_board=ele_board*piece
            fu_result1=np.sum(add_board)

            if fu_result1 >= result1:
                result1=fu_result1
                MAX=fu_result1
                re_t1=t
        
    #if MAX == 0:
    #    return -1
    #print(MAX)
    #print(len(next_hand_ele))
    #print(re_t)
    if re_t5!=-1:
        return re_t5
    elif re_t4!=-1:
        return re_t4
    elif re_t3!=-1:
        return re_t3
    elif re_t2!=-1:
        return re_t2
    elif re_t1!=-1:
        return re_t1
