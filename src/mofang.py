# {"F":"yellow","R":"blue","L":"red","U":"white","D":"orange","B":"green"}
# {"yellow":0,"blue":1,"red":2,"white":3,"orange":4,"green":5}
# maps = {"F":[1,2,3,4,5,6,7,8,9],"R":[11,12,13,14,15,16,17,18,19],"L":[21,22,23,24,25,26,27,28,29],"U":[31,32,33,34,35,36,37,38,39],"D":[41,42,43,44,45,46,47,48,49],"B":[51,52,53,54,55,56,57,58,59]}
# def Print(m,row):
#     for j in range(0,m.__len__(),row):
#         print(m[j:j+row])
# def rotate(a,row):
#     for row_2 in range(row):
#         for col_2 in range(row_2, row):
#             a[col_2 * row + row_2], a[row_2 * row + col_2] = a[row_2 * row + col_2], a[col_2 * row + row_2]
#
# def rotate_r(a, row):
#     m = list(a)
#     a.clear()
#     a += [x[::-1] for x in zip(*m)]
# #F顺时针
# a = [[col for col in range(4)] for row in range(4)]
# #a = [0 for i in range(4)] + [1 for i in range(4)] + [2 for i in range(4)] + [3 for i in range(4)]
# #Print(a,4)
# for i in a:
#     print(i)
# print('-'*20)
# rotate_r(a,4)
# #Print(a,4)
# for i in a:
#     print(i)
# row = 4
# # for row_2 in range(row):
# #     for col_2 in range(row):
# #         a[col_2 * row + row_2], a[row_2 * row + col_2] = a[row_2 * row + col_2], a[col_2 * row + row_2]
F = "F"
R = "R"
L = "L"
B = "B"
U = "U"
D = "D"
def rotate(m):
    pass
maps = {F:[[1,2,3,4,5,6,7,8,9],"URDL"],
        R:[[21,22,23,24,25,26,27,28,29],"UBDF"],
        L:[[31,32,33,34,35,36,37,38,39],"UFDB"],
        B:[[41,42,43,44,45,46,47,48,49],"ULDR"],
        U:[[51,52,53,54,55,56,57,58,59],"BRFL"],
        D:[[61,62,63,64,65,66,67,68,69],"FRBL"],}
# maps[F][0][0:3] = [11,12,13]
# maps[F][0][6:9]
#maps[F][0][2:9:3] = [11,12,13]
#print(maps[F][0][0:9:3])
#print(maps)


#旋转顶面
rotate(maps[F][0])
for i in maps[F][1]:
    maps[i],"F"

def get(face,bar):
    l = maps[face]
    #face = "U"
    index = l[1].index(bar)
    if index == 0:
        return l[0][0:3]
    elif index == 1:
        return l[0][2:9:3]
    elif index == 2:
        return l[0][6:9]
    elif index == 3:
        return l[0][0:9:3]

def set(face, bar,new):
    l = maps[face]
    # face = "U"
    index = l[1].index(bar)
    if index == 0:
        l[0][0:3] = new
    elif index == 1:
        l[0][2:9:3] = new
    elif index == 2:
        l[0][6:9] = new
    elif index == 3:
        l[0][0:9:3] = new

#set("F","U",[11,12,13])
#print(maps[F])
#顺时针旋转
def roate_other(face,m):
    last = get(m[face][1][3],face)
    for i in range(3,-1,-1):
        if i ==  0:
            #print(m[face][1][0]," ",m[face][1][3])
            set(m[face][1][i],face,last)
            break
        set(m[face][1][i], face, get(m[face][1][i-1],face))
def roate_other_r(face, m):
    first = get(m[face][1][0], face)
    for i in range(0,4):
        if i == 3:
            set(m[face][1][i], face, first)
            #print(m[face][1][i],m[face][1][0])
            break
        #print(m[face][1][i], m[face][1][i + 1])
        set(m[face][1][i], face, get(m[face][1][i+ 1], face))


roate_other_r("F",maps)
for i in maps:
    print(i,":",maps[i])



