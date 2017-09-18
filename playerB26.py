from blokus.player import Player
from blokus.utils import encodeFourCode
from blokus.piece import Pieces
from blokus.move import getAllMovePatterns
import numpy as np
import math
import piece5B26
import pieceB26
import random
import hyoukaB26
import hyouka_AB26
import hyouka_countB26

FUTURE_WEIGHT = 20
CORNER_WEIGHT = 5
SIDE_WEIGHT = 0
SAME_WEIGHT = 0
BOARD_CORNER = 10
FUTURE_KEEP = 2

#--------------------------------------------------------------------------------
CORNER = math.log10(BOARD_CORNER)

val_board = np.arange(576).reshape(24,24)
val_board[::,::] = 9

width = np.logspace(0,CORNER,20)
height = np.logspace(CORNER,0,20).reshape(20,1)

val_board[2:22,2:22] = width + height
#-----------------------------------------------------------------------------------
class CPlayerB26(Player):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.logs = []

    def log(self, player, move):
        self.logs.append((player, move))

    def move(self, board, pieces):
        np_board = np.array(board)
        #--------------------------------------------------------------------------------------
    	#引数handの将来性を評価するための関数
        def future(hand):
            #-----------------------------------------------------------------------------------
            #引数handの持つ角の先に広がるスペース(0)をカウントし出力
            def zero_future(field):
                zero_count = 0
                clocation_y,clocation_x = np.where(field == 8)
			
                for s in range(0,len(clocation_x)):
                    location_x = clocation_x[s]
                    location_y = clocation_y[s]
                    #右
                    while field[location_y,location_x+1] == 0:
                        location_x += 1
                        zero_count += 1
                    location_x = clocation_x[s]
                    #右下
                    while field[location_y+1,location_x+1] == 0:
                        location_x += 1
                        location_y += 1
                        zero_count += 1
                    location_x = clocation_x[s]
                    location_y = clocation_y[s]
                    #下
                    while field[location_y+1,location_x] == 0:
                        location_y += 1
                        zero_count += 1
                    location_y = clocation_y[s]
                    #左下
                    while field[location_y+1,location_x-1] == 0:
                        location_x -= 1
                        location_y += 1
                        zero_count += 1
                    location_x = clocation_x[s]
                    location_y = clocation_y[s]
                    #左
                    while field[location_y,location_x-1] == 0:
                        location_x -= 1
                        zero_count += 1
                    location_x = clocation_x[s]
                    #左上
                    while field[location_y-1,location_x-1] == 0:
                        location_x -= 1
                        location_y -= 1
                        zero_count += 1
                    location_x = clocation_x[s]
                    location_y = clocation_y[s]
                    #上
                    while field[location_y-1,location_x] == 0:
                        location_y -= 1
                        zero_count += 1
                    location_y = clocation_y[s]
                    #右上
                    while field[location_y-1,location_x+1] == 0:
                        location_x += 1
                        location_y -= 1
                        zero_count += 1
                        
                return zero_count * CORNER_WEIGHT
            #-----------------------------------------------------------------------------------
            #あらかじめ評価づけされたボード上でのhandの角の将来性を評価する
            def log_future(park):
                cloc_y,cloc_x = np.where(park == 8)
                value = 0
                value_list = []

                for n in range(0,len(cloc_x)):
                    palocation_x = cloc_x[n]
                    palocation_y = cloc_y[n]
                    
                    if park[palocation_y+1,palocation_x] != 1 and park[palocation_y-1,palocation_x] != 1 and park[palocation_y,palocation_x+1] != 1 and park[palocation_y,palocation_x-1] != 1:
             
                        #右
                        while park[palocation_y,palocation_x+1] == 0:
                            value += val_board[palocation_y-1,palocation_x-1+1]
                            palocation_x += 1
                        palocation_x = cloc_x[n]
                        #右下
                        while park[palocation_y+1,palocation_x+1] == 0:
                            value += val_board[palocation_y-1+1,palocation_x-1+1]
                            palocation_x += 1
                            palocation_y += 1
                        palocation_x = cloc_x[n]
                        palocation_y = cloc_y[n]
                        #下
                        while park[palocation_y+1,palocation_x] == 0:
                            value += val_board[palocation_y-1+1,palocation_x-1]
                            palocation_y += 1
                        palocation_y = cloc_y[n]
                        #左下
                        while park[palocation_y+1,palocation_x-1] == 0:
                            value += val_board[palocation_y-1+1,palocation_x-1-1]
                            palocation_x -= 1
                            palocation_y += 1
                        palocation_x = cloc_x[n]
                        palocation_y = cloc_y[n]
                        #左
                        while park[palocation_y,palocation_x-1] == 0:
                            value += val_board[palocation_y-1,palocation_x-1-1]
                            palocation_x -= 1
                        palocation_x = cloc_x[n]
                        #左上
                        while park[palocation_y-1,palocation_x-1] == 0:
                            value += val_board[palocation_y-1-1,palocation_x-1-1]
                            palocation_x -= 1
                            palocation_y -= 1
                        palocation_x = cloc_x[n]
                        palocation_y = cloc_y[n]
                        #上
                        while park[palocation_y-1,palocation_x] == 0:
                            value += val_board[palocation_y-1-1,palocation_x-1]
                            palocation_y -= 1
                        palocation_y = cloc_y[n]
                        #右上
                        while park[palocation_y-1,palocation_x+1] == 0:
                            value += val_board[palocation_y-1-1,palocation_x-1+1]
                            palocation_x += 1
                            palocation_y -= 1

                        value_list.append(value)

                return value / FUTURE_KEEP
	#------------------------------------------------------------------------------------
            expect = []
            future_board = np.arange(676).reshape(26,26)
            fourth_board = np.arange(676).reshape(26,26)

            future_board[::,::] = 9
            fourth_board[::,::] = 9

            future_board[3:23,3:23] = np_board.copy()
            fourth_board[3:23,3:23] = np_board.copy()

            #引数handの正しい座標に正しいピースを置く
            for t in range(0,len(hand)):
                future_x = hand[t][0]+1
                future_y = hand[t][1]+1
                future_piece = pieceB26.pieces[hand[t][2]]

                future_board[future_x-3:future_x+4,future_y-3:future_y+4] = fourth_board[future_x-3:future_x+4,future_y-3:future_y+4]
                future_board[future_x-3:future_x+4,future_y-3:future_y+4] += future_piece
                
                expect.append(log_future(future_board))

                future_board[::,::] = fourth_board[::,::]

            np_expect = np.array(expect)
           
            return np_expect
        #---------------------------------------------------------------------------
        #最終的な評価付けの関数
        def evaluation(pro_board, next_hand_ele, future, hereis):
            length = (len(next_hand_ele))

            ele_board = np.arange(25).reshape(5,5)
            add_board = np.arange(25).reshape(5,5)

            point = np.array([])
            fu_result = []
            thebest = 0
    
            for t in range(0,length):
                x = next_hand_ele[t][0]
                y = next_hand_ele[t][1]
                pieceB26 = piece5B26.ex_pieces[next_hand_ele[t][2]]

                ele_board = pro_board[x-2:x+3,y-2:y+3]
                add_board = ele_board*pieceB26
                fu_result.append(np.sum(add_board))

            toenemy = np.array(fu_result)
            point = toenemy + future + hereis

            thebest = np.where(point==np.max(point))
            this_is_it = random.choice(thebest[0])
            
            return this_is_it
        #----------------------------------------------------------------
        #自分の合法手と、相手が置くことのできる場所を返す関数
        def legal(color, temp_board, other_pieces, value_board):
            other_board = np.arange(576).reshape(24,24)
            ex_board = np.arange(576).reshape(24,24)

            other_board[::,::] = 9

            other_board[2:22,2:22] = temp_board.copy()
            #----------------------------------------------------------------------
            other_board[other_board==1] = 1496
            other_board[other_board==color] = 1
            other_board[other_board==1496] = color

            ex_board = other_board.copy()
            #-------------------------------------------------------------------
            for x in range(2,22):
                for y in range(2,22):
                    if temp_board[x-2,y-2]==color:
                        #右下
                        if ex_board[x+1,y+1]!=1:
                            if ex_board[x+1,y]!=1 and ex_board[x+1,y+2]!=1 and ex_board[x,y+1]!=1 and ex_board[x+2,y+1]!=1 and ex_board[x+1,y+1]!=2 and ex_board[x+1,y+1]!=3 and ex_board[x+1,y+1]!=4 and ex_board[x+1,y+1]!=9:
                                other_board[x+1,y+1]=8
                            else:
                                other_board[x+1,y+1]=9
                        #下
                        if ex_board[x+1,y]!=1:
                                other_board[x+1,y]=9
                        #左下
                        if ex_board[x+1,y-1]!=1:
                            if ex_board[x+1,y]!=1 and ex_board[x,y-1]!=1 and ex_board[x+1,y-2]!=1 and ex_board[x+2,y-1]!=1 and ex_board[x+1,y-1]!=2 and ex_board[x+1,y-1]!=3 and ex_board[x+1,y-1]!=4 and ex_board[x+1,y-1]!=9:
                                other_board[x+1,y-1]=8
                            else:
                                other_board[x+1,y-1]=9
                        #右    
                        if ex_board[x,y+1]!=1:
                                other_board[x,y+1]=9
                        #左
                        if ex_board[x,y-1]!=1:
                                other_board[x,y-1]=9
                        #右上
                        if ex_board[x-1,y+1]!=1:
                            if ex_board[x,y+1]!=1 and ex_board[x-1,y+2]!=1 and ex_board[x-2,y+1]!=1 and ex_board[x-1,y]!=1 and ex_board[x-1,y+1]!=2 and ex_board[x-1,y+1]!=3 and ex_board[x-1,y+1]!=4 and ex_board[x-1,y+1]!=9:
                                other_board[x-1,y+1]=8
                            else:
                                other_board[x-1,y+1]=9
                        #上
                        if ex_board[x-1,y]!=1:
                                other_board[x-1,y]=9
                        #左上
                        if ex_board[x-1,y-1]!=1:
                            if ex_board[x-1,y]!=1 and ex_board[x,y-1]!=1 and ex_board[x-1,y-2]!=1 and ex_board[x-2,y-1]!=1 and ex_board[x-1,y-1]!=2 and ex_board[x-1,y-1]!=3 and ex_board[x-1,y-1]!=4 and ex_board[x-1,y-1]!=9:
                                other_board[x-1,y-1]=8
                            else:
                                other_board[x-1,y-1]=9
            #--------------------------------------------------------------------------------------
            #敵の持っているコマを取得
            if color%4 != 1:
                other_pieces = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
                eco_board = np.arange(400).reshape(20,20)
                eco_board[::,::] = 0

                other_board[other_board==2] = 5

                l_two_x, l_two_y = [19],[0]
                
                for i in reversed(range(0, 102)):
                    for x in range(2,22):
                        for y in range(2,22):
                            if other_board[x,y]==1 and eco_board[x-2,y-2]!=4:
                                square = other_board[x-2:x+3,y-2:y+3]

                                orip = piece5B26.ex_pieces[i]
                                square_r = square + orip
                                square_r[square_r!=2] = 0

                                if np.array_equal(square_r-orip, orip) == True:
                                    two_x, two_y = np.where(square_r==2)
                                    l_two_x.extend(x+two_x-4)
                                    l_two_y.extend(y+two_y-4)
                                    for n in range(0, len(l_two_x)):
                                        eco_board[l_two_x[n],l_two_y[n]] = 4
                                    if i==0:
                                        other_pieces.remove('a')
                                    elif 1<=i and i<=4:
                                        other_pieces.remove('b')
                                    elif 5<=i and i<=6:
                                        other_pieces.remove('c')
                                    elif 7<=i and i<=10:
                                        other_pieces.remove('d')
                                    elif 11<=i and i<=14:       
                                        other_pieces.remove('e')
                                    elif 15<=i and i<=22:
                                        other_pieces.remove('f')
                                    elif 23<=i and i<=26:
                                        other_pieces.remove('g')
                                    elif 27<=i and i<=30:
                                        other_pieces.remove('h')
                                    elif 31<=i and i<=38:
                                        other_pieces.remove('i')
                                    elif 39<=i and i<=40:
                                        other_pieces.remove('j')
                                    elif 41<=i and i<=48:
                                        other_pieces.remove('k')
                                    elif 49<=i and i<=56:
                                        other_pieces.remove('l')
                                    elif 57<=i and i<=64:
                                        other_pieces.remove('m')
                                    elif 65<=i and i<=68:
                                        other_pieces.remove('n')
                                    elif 69<=i and i<=76:
                                        other_pieces.remove('o')
                                    elif 77<=i and i<=80:
                                        other_pieces.remove('p')
                                    elif 81<=i and i<=84:
                                        other_pieces.remove('q')
                                    elif 85<=i and i<=88:
                                        other_pieces.remove('r')
                                    elif 89<=i and i<=92:
                                        other_pieces.remove('s')
                                    elif 93<=i and i<=100:
                                        other_pieces.remove('t')
                                    elif i==101:
                                        other_pieces.remove('u')
                                    break
                #print("敵の色：",color,"残りのコマ：",other_pieces)
                other_board[other_board==5] = 2
            #----------------------------------------------------------------------
            #合法手の取得
            box  = np.arange(25).reshape(5,5)
            next_hand = []
            save_hand = []

            eight_x, eight_y = np.where(other_board==8)

            if len(eight_x)!=0:
                min_x, max_x = min(eight_x),max(eight_x)
                min_y, max_y = min(eight_y),max(eight_y)

                if min_x>=4:
                    range_x_min = min_x-2
                else:
                    range_x_min = 2
                if max_x<=20:
                    range_x_max = max_x+2
                else:
                    range_x_max = 22

                if min_y>=4:
                    range_y_min = min_y-2
                else:
                    range_y_min = 2
                if max_y<=20:
                    range_y_max = max_y+2
                else:
                    range_y_max = 22

                for x in range(range_x_min,range_x_max):
                    for y in range(range_y_min,range_y_max):
                        if other_board[x,y]==0 or other_board[x,y]==8:
                            box = other_board[x-2:x+3,y-2:y+3]

                            for i in range(0, 102):
                                if i==0:
                                    if 'a' not in other_pieces:
                                        continue
                                elif 1<=i and i<=4:
                                    if 'b' not in other_pieces:
                                        continue
                                elif 5<=i and i<=6:
                                    if 'c' not in other_pieces:
                                        continue
                                elif 7<=i and i<=10:
                                    if 'd' not in other_pieces:
                                        continue
                                elif 11<=i and i<=14:
                                    if 'e' not in other_pieces:
                                        continue
                                elif 15<=i and i<=22:
                                    if 'f' not in other_pieces:
                                        continue
                                elif 23<=i and i<=26:
                                    if 'g' not in other_pieces:
                                        continue
                                elif 27<=i and i<=30:
                                    if 'h' not in other_pieces:
                                        continue
                                elif 31<=i and i<=38:
                                    if 'i' not in other_pieces:
                                        continue
                                elif 39<=i and i<=40:
                                    if 'j' not in other_pieces:
                                        continue
                                elif 41<=i and i<=48:
                                    if 'k' not in other_pieces:
                                        continue
                                elif 49<=i and i<=56:
                                    if 'l' not in other_pieces:
                                        continue
                                elif 57<=i and i<=64:
                                    if 'm' not in other_pieces:
                                        continue
                                elif 65<=i and i<=68:
                                    if 'n' not in other_pieces:
                                        continue
                                elif 69<=i and i<=76:
                                    if 'o' not in other_pieces:
                                        continue
                                elif 77<=i and i<=80:
                                    if 'p' not in other_pieces:
                                        continue
                                elif 81<=i and i<=84:
                                    if 'q' not in other_pieces:
                                        continue
                                elif 85<=i and i<=88:
                                    if 'r' not in other_pieces:
                                        continue
                                elif 89<=i and i<=92:
                                    if 's' not in other_pieces:
                                        continue
                                elif 93<=i and i<=100:
                                    if 't' not in other_pieces:
                                        continue
                                elif i==101:
                                    if 'u' not in other_pieces:
                                        continue
                            
                                pie = piece5B26.ex_pieces[i]
                                
                                box[box==2] = 9
                                box[box==3] = 9
                                box[box==4] = 9
                                
                                box_r = box * pie
                                
                                box_r[box_r==0] = 1496
                                box_r[box_r==1] = 0
                                box_r[box_r==1496] = 1
                                
                                if np.max(box_r)==8 and np.min(box_r)==1:
                                    if i==0:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'a',i))
                                    elif 1<=i and i<=4:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'b',i*2-2))
                                    elif 5<=i and i<=6:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'c',i*2-10))
                                    elif 7<=i and i<=10:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'d',i*2-13))
                                    elif 11<=i and i<=14:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'e',i*2-22))
                                    elif 15<=i and i<=22:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'f',i-15))
                                    elif 23<=i and i<=26:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'g',i-23))
                                    elif 27<=i and i<=30:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'h',i*2-54))
                                    elif 31<=i and i<=38:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'i',i-31))
                                    elif 39<=i and i<=40:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'j',i*2-78))
                                    elif 41<=i and i<=48:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'k',i-41))
                                    elif 49<=i and i<=56:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'l',i-49))
                                    elif 57<=i and i<=64:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'m',i-57))
                                    elif 65<=i and i<=68:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'n',i-65))
                                    elif 69<=i and i<=76:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'o',i-69))
                                    elif 77<=i and i<=80:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'p',i*2-154))
                                    elif 81<=i and i<=84:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'q',i*2-161))
                                    elif 85<=i and i<=88:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'r',i*2-169))
                                    elif 89<=i and i<=92:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'s',i-89))
                                    elif 93<=i and i<=100:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'t',i-93))
                                    elif i==101:
                                        save_hand.append([x,y,i])
                                        next_hand.append(encodeFourCode(x-2,y-2,'u',i-100))
            #-------------------------------------------------------------------------------------
            #save_handに含まれるすべての手を仮想ボード上に置き、相手が置くことのできる場所を取得
            if color%4 != 1:
                enemy_will_board = np.arange(576).reshape(24,24)
                enemy_will_board[::,::] = 0
                
                for t in range(0,len(save_hand)):
                    enemy_will_x = save_hand[t][0]
                    enemy_will_y = save_hand[t][1]
                    azap = piece5B26.ex_pieces[save_hand[t][2]]
                    
                    enemy_will_board[enemy_will_x-2:enemy_will_x+3,enemy_will_y-2:enemy_will_y+3] += azap
                    
                eneval_board = value_board + enemy_will_board
        #---------------------------------------------------------------------------------------
        #自分の合法手、相手が置く可能性のある場所を返す
            if color%4 == 1:
                return(save_hand, next_hand)
            elif color%4 != 1:
                return(eneval_board)
        #--------------------------------------------------------------------------------------
        #相手の角と辺を識別するボードを生成する関数
        def rival():
            rival_board = np.arange(576).reshape(24,24)
            temp_board = np.arange(576).reshape(24,24)
            
            rival_board[::,::] = 9
            temp_board[::,::] = 9

            rival_board[2:22,2:22] = np_board.copy()
            temp_board[2:22,2:22] = np_board.copy()

            for x in range(2,22):
                for y in range(2,22):
                    if board[x-2,y-2] == 0:
                        #左上
                        if temp_board[x-1,y-1] == 2:
                            if temp_board[x,y-1] == 2 or temp_board[x-1,y] == 2:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x-1,y-1] == 3:
                            if temp_board[x,y-1] == 3 or temp_board[x-1,y] == 3:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x-1,y-1] == 4:
                            if temp_board[x,y-1] == 4 or temp_board[x-1,y] == 4:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        #上
                        if temp_board[x-1,y] == 2 or temp_board[x-1,y] == 3 or temp_board[x-1,y] == 4:
                            rival_board[x,y] = rival_board[x,y] + SIDE_WEIGHT
                        #右上
                        if temp_board[x-1,y+1] == 2:
                            if temp_board[x,y+1] == 2 or temp_board[x-1,y] == 2:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x-1,y+1] == 3:
                            if temp_board[x,y+1] == 3 or temp_board[x-1,y] == 3:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x-1,y+1] == 4:
                            if temp_board[x,y+1] == 4 or temp_board[x-1,y] == 4:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        #左
                        if temp_board[x,y-1] == 2 or temp_board[x,y-1] == 3 or temp_board[x,y-1] == 4:
                            rival_board[x,y] = rival_board[x,y] + SIDE_WEIGHT
                        #右
                        if temp_board[x,y+1] == 2 or temp_board[x,y+1] == 3 or temp_board[x,y+1] == 4:
                            rival_board[x,y] = rival_board[x,y] + SIDE_WEIGHT
                        #左下
                        if temp_board[x+1,y-1] == 2:
                            if temp_board[x,y-1] == 2 or temp_board[x+1,y] == 2:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x+1,y-1] == 3:
                            if temp_board[x,y-1] == 3 or temp_board[x+1,y] == 3:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x+1,y-1] == 4:
                            if temp_board[x,y-1] == 4 or temp_board[x+1,y] == 4:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        #下
                        if temp_board[x+1,y] == 2 or temp_board[x+1,y] == 3 or temp_board[x+1,y] == 4:
                            rival_board[x,y] = rival_board[x,y] + SIDE_WEIGHT
                        #右下
                        if temp_board[x+1,y+1] == 2:
                            if temp_board[x,y+1] == 2 or temp_board[x+1,y] == 2:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x+1,y+1] == 3:
                            if temp_board[x,y+1] == 3 or temp_board[x+1,y] == 3:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
                        if temp_board[x+1,y+1] == 4:
                            if temp_board[x,y+1] == 4 or temp_board[x+1,y] == 4:
                                rival_board[x,y] = rival_board[x,y] + SAME_WEIGHT
                            else:
                                rival_board[x,y] = rival_board[x,y] + CORNER_WEIGHT
            return rival_board        
        #---------------------------------------------------------------------------------
        #より確実な将来性を吟味する関数
        def spera(s_legal_hand, other_legal_board):
            sub_pieces = pieces[:]
            sub_board = np.arange(676).reshape(26,26)
            risk_board = np.arange(676).reshape(26,26)
            sub_board[::,::] = 9
            sub_board[3:23,3:23] = board.copy()
            risk_board[::,::] = 9
            risk_board[1:25,1:25] = other_legal_board.copy()

            got_futures = []
            added_future = []
            each_future = []
            t_list = []
            max_t_list = []
            risk_list = []

            each_pieces = []
            #-------------------------------------------------------------------------------
            #perfect_future専用の合法手取得用関数内関数
            def legal_future(n, board_future, pieces_future, save_hand_future):
                s_h_f = []
                eightx, eighty = np.where(board_future==8)

                if save_hand_future[n][2]==0:
                    pieces_future.remove('a')
                elif 1<=save_hand_future[n][2] and save_hand_future[n][2]<=4:
                    pieces_future.remove('b')
                elif 5<=save_hand_future[n][2] and save_hand_future[n][2]<=6:
                    pieces_future.remove('c')
                elif 7<=save_hand_future[n][2] and save_hand_future[n][2]<=10:
                    pieces_future.remove('d')
                elif 11<=save_hand_future[n][2] and save_hand_future[n][2]<=14:       
                    pieces_future.remove('e')
                elif 15<=save_hand_future[n][2] and save_hand_future[n][2]<=22:
                    pieces_future.remove('f')
                elif 23<=save_hand_future[n][2] and save_hand_future[n][2]<=26:
                    pieces_future.remove('g')
                elif 27<=save_hand_future[n][2] and save_hand_future[n][2]<=30:
                    pieces_future.remove('h')
                elif 31<=save_hand_future[n][2] and save_hand_future[n][2]<=38:
                    pieces_future.remove('i')
                elif 39<=save_hand_future[n][2] and save_hand_future[n][2]<=40:
                    pieces_future.remove('j')
                elif 41<=save_hand_future[n][2] and save_hand_future[n][2]<=48:
                    pieces_future.remove('k')
                elif 49<=save_hand_future[n][2] and save_hand_future[n][2]<=56:
                    pieces_future.remove('l')
                elif 57<=save_hand_future[n][2] and save_hand_future[n][2]<=64:
                    pieces_future.remove('m')
                elif 65<=save_hand_future[n][2] and save_hand_future[n][2]<=68:
                    pieces_future.remove('n')
                elif 69<=save_hand_future[n][2] and save_hand_future[n][2]<=76:
                    pieces_future.remove('o')
                elif 77<=save_hand_future[n][2] and save_hand_future[n][2]<=80:
                    pieces_future.remove('p')
                elif 81<=save_hand_future[n][2] and save_hand_future[n][2]<=84:
                    pieces_future.remove('q')
                elif 85<=save_hand_future[n][2] and save_hand_future[n][2]<=88:
                    pieces_future.remove('r')
                elif 89<=save_hand_future[n][2] and save_hand_future[n][2]<=92:
                    pieces_future.remove('s')
                elif 93<=save_hand_future[n][2] and save_hand_future[n][2]<=100:
                    pieces_future.remove('t')
                elif save_hand_future[n][2]==101:
                    pieces_future.remove('u')
                
                minx, maxx = min(eightx),max(eightx)
                miny, maxy = min(eighty),max(eighty)

                if minx>=5:
                    from_x = minx-2
                else:
                    from_x = 3
                if maxx<=21:
                    to_x = maxx+2
                else:
                    to_x = 23

                if miny>=5:
                    from_y = miny-2
                else:
                    from_y = 2
                if maxy<=21:
                    to_y = maxy+2
                else:
                    to_y = 23

                for x in range(from_x, to_x):
                    for y in range(from_y, to_y):
                        if board_future[x,y]==0 or board_future[x,y]==8:
                            f_box = board_future[x-3:x+4,y-3:y+4].copy()

                            for i in range(0, 102):
                                if i==0:
                                    if 'a' not in pieces_future:
                                        continue
                                elif 1<=i and i<=4:
                                    if 'b' not in pieces_future:
                                        continue
                                elif 5<=i and i<=6:
                                    if 'c' not in pieces_future:
                                        continue
                                elif 7<=i and i<=10:
                                    if 'd' not in pieces_future:
                                        continue
                                elif 11<=i and i<=14:
                                    if 'e' not in pieces_future:
                                        continue
                                elif 15<=i and i<=22:
                                    if 'f' not in pieces_future:
                                        continue
                                elif 23<=i and i<=26:
                                    if 'g' not in pieces_future:
                                        continue
                                elif 27<=i and i<=30:
                                    if 'h' not in pieces_future:
                                        continue
                                elif 31<=i and i<=38:
                                    if 'i' not in pieces_future:
                                        continue
                                elif 39<=i and i<=40:
                                    if 'j' not in pieces_future:
                                        continue
                                elif 41<=i and i<=48:
                                    if 'k' not in pieces_future:
                                        continue
                                elif 49<=i and i<=56:
                                    if 'l' not in pieces_future:
                                        continue
                                elif 57<=i and i<=64:
                                    if 'm' not in pieces_future:
                                        continue
                                elif 65<=i and i<=68:
                                    if 'n' not in pieces_future:
                                        continue
                                elif 69<=i and i<=76:
                                    if 'o' not in pieces_future:
                                        continue
                                elif 77<=i and i<=80:
                                    if 'p' not in pieces_future:
                                        continue
                                elif 81<=i and i<=84:
                                    if 'q' not in pieces_future:
                                        continue
                                elif 85<=i and i<=88:
                                    if 'r' not in pieces_future:
                                        continue
                                elif 89<=i and i<=92:
                                    if 's' not in pieces_future:
                                        continue
                                elif 93<=i and i<=100:
                                    if 't' not in pieces_future:
                                        continue
                                elif i==101:
                                    if 'u' not in pieces_future:
                                        continue
                            
                                seven_piece = pieceB26.pieces[i]
                                      
                                f_box[f_box==2] = 9
                                f_box[f_box==3] = 9
                                f_box[f_box==4] = 9
                                    
                                f_box_r = f_box * seven_piece
                                    
                                f_box_r[f_box_r==0] = 1496
                                f_box_r[f_box_r==1] = 0
                                f_box_r[f_box_r==1496] = 1
                                f_box_r[f_box_r==8] = 100
                                f_box_r[f_box_r==9] = 200
                                f_box_r[f_box_r==45]= 200
                             
                                if np.max(f_box_r)==100 and np.min(f_box_r)==1:
                                    s_h_f.append([x,y,i])
                
                return (s_h_f, pieces_future)
            #---------------------------------------------------------------------------------------------
            #1手目を仮想ボードに順番に配置
            for t in range(0,len(s_legal_hand)):
                first_board = sub_board.copy()
                first_board[first_board==1] = 5
                first_pieces = sub_pieces[:]

                first_x = s_legal_hand[t][0]+1
                first_y = s_legal_hand[t][1]+1
                first_hand = pieceB26.pieces[s_legal_hand[t][2]].copy()
                first_board[first_x-3:first_x+4,first_y-3:first_y+4] += first_hand
                first_board[first_board>=10] = 9
                first_eight_x, first_eight_y = np.where(first_board==8)

                first = piece5B26.ex_pieces[s_legal_hand[t][2]].copy()

                if len(first_eight_x)==0:
                    each_future.append([np.count_nonzero(first),0,0])
                    risk_list.append(["nothing","nothing"])
                    t_list.append(t)

                elif len(first_eight_x)!=0:
                    first_future_hand, temp_second_pieces = legal_future(t, first_board, first_pieces, s_legal_hand)

                    if len(first_future_hand)==0:
                        each_future.append([np.count_nonzero(first),0,0])
                        risk_list.append(["nothing","nothing"])
                        t_list.append(t)
                    else:
                        #ここから2手目
                        for u in range(0, len(first_future_hand)):
                            second_pieces = temp_second_pieces[:]
                            second_board = sub_board.copy()
                            second_board[first_x-2:first_x+3,first_y-2:first_y+3] += piece5B26.ex_pieces[s_legal_hand[t][2]].copy()
                            second_board[second_board==1] = 5

                            second_x = first_future_hand[u][0]
                            second_y = first_future_hand[u][1]
                            second_hand = pieceB26.pieces[first_future_hand[u][2]].copy()
                            second_board[second_x-3:second_x+4,second_y-3:second_y+4] += second_hand
                            second_board[second_board>=10] = 9
                            second_eight_x, second_eight_y = np.where(second_board==8)
                            
                            second = piece5B26.ex_pieces[first_future_hand[u][2]].copy()
                            second_risk_check = risk_board[second_x-2:second_x+3, second_y-2:second_y+3] * second

                            if np.count_nonzero(second_risk_check)>=1:
                                second_risk = "danger"
                            else:
                                second_risk = "reserved"

                            if len(second_eight_x)==0:
                                each_future.append([np.count_nonzero(first), np.count_nonzero(second),0])
                                risk_list.append([second_risk, "nothing"])
                                t_list.append(t)

                            elif len(second_eight_x)!=0:
                                second_future_hand, third_pieces = legal_future(u, second_board, second_pieces, first_future_hand)
                            
                                if len(second_future_hand)==0:
                                    each_future.append([np.count_nonzero(first), np.count_nonzero(second),0])
                                    risk_list.append([second_risk, "nothing"])
                                    t_list.append(t)

                                else:
                                    #ここから3手目
                                    for v in range(0, len(second_future_hand)):
                                        third_board = sub_board.copy()
                                        third_x = second_future_hand[v][0]
                                        third_y = second_future_hand[v][1]
                                        
                                        third = piece5B26.ex_pieces[second_future_hand[v][2]].copy()
                                        third_risk_check = risk_board[third_x-2:third_x+3,third_y-2:third_y+3] * third

                                        if np.count_nonzero(third_risk_check)>=1:
                                            risk_list.append([second_risk, "danger"])
                                        else:
                                            risk_list.append([second_risk, "reserved"])

                                        each_future.append([np.count_nonzero(first), np.count_nonzero(second), np.count_nonzero(third)])
                                        t_list.append(t)

            if t_list!=[]:
                for w in range(0, len(t_list)):
                    if risk_list[w][0] == "danger":
                        each_future[w][1] /= 2
                    if risk_list[w][1] == "danger":
                        each_future[w][2] /= 3
                
                    added_future.append(each_future[w][0]+each_future[w][1]+each_future[w][2])
            else:
                return 0
                
            max_t_list.append(t_list[added_future.index(max(added_future))])

            return random.choice(max_t_list)
#---------------------------------------------------------------------------------------------
#ここからmoveの実行部分
        self.count += 1
        hand = "pass"
        if self.count == 1:
            hand = encodeFourCode(18, 1, 's', 5)
            return hand
        if self.count == 2:
            hand = encodeFourCode(16, 5, 'q', 1)
            return hand
        if self.count == 3:
            hand = encodeFourCode(12, 7, 'r', 2)
            return hand
        else:
            CORNER_WEIGHT = 100 / ((self.count-3)*2)
            if CORNER_WEIGHT==8 or CORNER_WEIGHT==9:
                CORNER_WEIGHT = 7
#---------------------------------------------------------------------
#関数legalを実行して自分の合法手を取得
            o_pieces = []
            s_hand,n_hand = legal(1, np_board,  pieces, val_board)
#-------------------------------------------------------------------
#関数rivalを実行して相手の角と辺の情報を取得
            rivalcorner_board = rival()
#----------------------------------------------------------------------
            hold_hand = []
            hold_next = []
            #次の一手を打つ部分
            if len(s_hand) != 0 and hyouka_countB26.hyouka_count(s_hand, n_hand) != 0:
                if not len(s_hand) <= 200:
                    no_pro_hand, no_pro_next_hand = hyouka_countB26.hyouka_count(s_hand, n_hand)#ここで合法手中の最も大きなピースのみを新たな合法手として再定義する
                else:#s_handが200個以下なら大きさ重視の合法手を作らない
                    no_pro_hand, no_pro_next_hand = s_hand, n_hand
                  
                    zero_board = np.arange(576).reshape(24,24)
                    zero_board[::,::] = 0
                    s_v_board = legal(2, np_board, o_pieces, zero_board)
                    t_v_board = legal(3, np_board, o_pieces, s_v_board)
                    f_v_board = legal(4, np_board, o_pieces, t_v_board)
                    f_v_board[f_v_board!=0] = 9

                op_piece = hyoukaB26.hyouka(rivalcorner_board, no_pro_hand)

                if len(s_hand) <=200:
                    temp_s_hand = s_hand[:]

                    for t in range(0,len(temp_s_hand)):
                        hold_x = temp_s_hand[t][0]
                        hold_y = temp_s_hand[t][1]
                        hold_piece = piece5B26.ex_pieces[temp_s_hand[t][2]]
                        
                        hold_board = f_v_board.copy()
                        hold_check = hold_board[hold_x-2:hold_x+3,hold_y-2:hold_y+3] + hold_piece
                        check_x, check_y = np.where(hold_check==10)
                        if len(check_x)<=1:
                            hold_hand.append(temp_s_hand[t])
                            hold_next.append(n_hand[s_hand.index(temp_s_hand[t])])
                            n_hand.pop(s_hand.index(temp_s_hand[t]))
                            s_hand.remove(temp_s_hand[t])

                    if len(s_hand)!=0 and hyouka_countB26.hyouka_count(s_hand, n_hand) != 0:
                        no_pro_hand, no_pro_next_hand = hyouka_countB26.hyouka_count(s_hand, n_hand)
                    elif len(hold_hand)!=0 and hyouka_countB26.hyouka_count(hold_hand, hold_next) != 0:
                        no_pro_hand, no_pro_next_hand = hyouka_countB26.hyouka_count(hold_hand, hold_next)


                op_piece = evaluation(rivalcorner_board, no_pro_hand, future(no_pro_hand), hyouka_AB26.hyouka_A(val_board,no_pro_hand))

                if len(s_hand) <= 200:
                    temp_op_piece = spera(no_pro_hand, f_v_board)
                    if temp_op_piece != 0:
                        op_piece = temp_op_piece

                return no_pro_next_hand[op_piece]

            else:
                return "pass"
