
VHNUMS = 3
CELLNUMS = VHNUMS * VHNUMS

# 若空白图像块不在最左边，则将空白块左边的块移动到空白块位置


gameBoard = [0, 2, 6, 1, -1, 5, 3, 7, 4]

# hash_map_n = {"231":("",""),"321":("231","UP"),"132":("321","LEFT")}
# hash_map_r = {"123":("",""),"213":("123","LEFT"),"132":("213","DOWN")}
#
# #key_middle the common key between two hash_map
# #return the the sequece from the key_begin of hash1 to key_begin of hash2
# #require data type key:(FATHER_KEY,DIRCT)



def calculate(gB,end):
    def moveRight(board, blackCell):
        if blackCell % VHNUMS == 0:
            return board
        board[blackCell - 1], board[blackCell] = board[blackCell], board[blackCell - 1]
        return board

    # 若空白图像块不在最右边，则将空白块右边的块移动到空白块位置
    def moveLeft(board, blackCell):
        if blackCell % VHNUMS == VHNUMS - 1:
            return board
        board[blackCell + 1], board[blackCell] = board[blackCell], board[blackCell + 1]
        return board

    # 若空白图像块不在最上边，则将空白块上边的块移动到空白块位置
    def moveDown(board, blackCell):
        if blackCell < VHNUMS:
            return board
        board[blackCell - VHNUMS], board[blackCell] = board[blackCell], board[blackCell - VHNUMS]
        return board

    # 若空白图像块不在最下边，则将空白块下边的块移动到空白块位置
    def moveUp(board, blackCell):
        if blackCell >= CELLNUMS - VHNUMS:
            return board
        board[blackCell + VHNUMS], board[blackCell] = board[blackCell], board[blackCell + VHNUMS]
        return board
    def result(key_middle, hash_map, hash_map1):
        reverseDirct = lambda dirct: {"UP": "DOWN", "LEFT": "RIGHT", "RIGHT": "LEFT", "DOWN": "UP"}[dirct]
        key = key_middle
        st = []
        while key.__len__() > 0 and hash_map[key][1].__len__() > 0:
            st.insert(0, hash_map[key][1])
            key = hash_map[key][0]
        key = key_middle
        while key.__len__() > 0 and hash_map1[key][1].__len__() > 0:
            st.append(reverseDirct(hash_map1[key][1]))
            key = hash_map1[key][0]
        return st
    def hash(gB):
        return "".join([str(x) for x in gB])
    dirct_map = {moveLeft: "LEFT", moveRight: "RIGHT", moveUp: "UP", moveDown: "DOWN"}
    if gB == end:
        return
    q_n = []
    q_r = []
    hash_map_n = {hash(gB):("","")}
    hash_map_r = {hash(end):("","")}
    q_n.append(gB)
    q_r.append(end)
    key_common = ""
    count = 0
    flag = True;
    while flag :
        cur = list(q_n[-1])
        q_n.pop()
        for func in dirct_map:
            board = func(list(cur),cur.index(-1))
            if hash(board) not in hash_map_n:
                q_n.insert(0,board)
                hash_map_n[hash(board)] = (hash(cur),dirct_map[func])
                if hash(board) in hash_map_r:
                    key_common = hash(board)
                    flag = False
        if flag == False:
            break
        cur = list(q_r[-1])
        q_r.pop()
        for func in dirct_map:
            board = func(list(cur), cur.index(-1))
            if hash(board) not in hash_map_r:
                q_r.insert(0, board)
                hash_map_r[hash(board)] = (hash(cur), dirct_map[func])
                if hash(board) in hash_map_n:
                    key_common = hash(board)
                    flag = False
        if flag == False:
            break
        count = count + 1
    return result(key_common,hash_map_n,hash_map_r)
end = [x for x in range(0,8)]
end.append(-1)
#print(end)
print(calculate(gameBoard,end))








