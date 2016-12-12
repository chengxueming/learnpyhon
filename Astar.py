from turtle import *
from time import sleep
x_offset = -300
y_offset =  200
m_width = 10
x_count = 50
y_count = 40
i = 1
arr = [[0 for i in range(x_count)] for i in range(y_count)]
#arr[0][15] = 1
#arr[1][0] = 1
#print("\n".join([str(x) for x in arr]))
#exit(1)
begin_pos = ()
end_pos = ()
colors = {1:'yellow',2:'black',3:'red',4:"blue"}
def dart():
    clear()
    tracer(0)
    for k in range(y_count):
        x,y = pos()
        goto(x_offset + 0,y)
        goto(x_offset + 0,y_offset - m_width * k)
        for i in range(x_count):
            goto(x_offset + m_width * i, y_offset-m_width * k)
            if arr[k][i] > 0:
                color('black', colors[arr[k][i]])
                begin_fill()
            for j in range(4):
                fd(m_width)
                lt(90)
            end_fill()
        goto(x_offset + 0,y_offset+ -m_width * k)
    tracer(1)

def Astar(begin,end,Arr):

    cal = lambda tu, dirct: (tu[0] + dirct[0], tu[1] + dirct[1])
    maybe = lambda p, e: abs(e[0] - p[0]) + abs(e[1] - p[1])
    isleagalpos = lambda p: True if p[0] >= 0 and p[0] < Arr[0].__len__() and p[1] >= 0 and p[1] < Arr.__len__() and Arr[p[1]][p[0]] != 3 else False

    def insert_to_open(op, ele):
        for val in op:
            if val[0] == ele:
                op.remove(val)
        for val in op:
            if val[1] >= ele[1]:
                op.insert(op.index(val), ele)
                return
        op.append(ele)
    open = [(begin, maybe(begin, end), 0)]
    close = {}
    count = 0
    points = [(-1, -1), (-1, 1), (0, -1), (0, 1), (1, 1), (1, -1), (1, 0), (-1, 0)]
    while open.__len__() > 0:
        count = count + 1
        beg_ele = open[0]
        open.pop(0)
        beg = beg_ele[0]
        close[beg] = beg_ele[2]
        if beg == end:
            break
        for dirc in points:
            pos = cal(beg, dirc)
            if not isleagalpos(pos):
                continue
            if dirc[0] != 0 and dirc[1] != 0:
                if Arr[pos[1]-1][pos[0]] == 3 or  Arr[pos[1]][pos[0] -1] == 3 or  Arr[pos[1] + 1][pos[0]] == 3 or  Arr[pos[1]][pos[0] + 1] == 3:
                    continue
            if pos not in close:
                ele = (pos, maybe(pos, end), beg)
                insert_to_open(open, ele)
    print("success")
    # print(close)
    ele = close[end]
    while isinstance(ele,tuple) and ele != begin:
        Arr[ele[1]][ele[0]] = 4
        print(ele)
        ele = close[ele]
def cal_w():
    print("hello")
    #print(begin_pos,end_pos)
    if begin_pos != () and end_pos != ():
        #pass
        Astar(begin_pos,end_pos,arr)
        dart()
def cal_s():
    global arr
    global i
    arr = [[0 for i in range(x_count)] for i in range(y_count)]
    i = 0
    dart()
def main():
    #onkey(None, "w")
    onkey(cal_w, "w")
    onkey(cal_s, "s")
    listen()
    onscreenclick(isclick, 1)
    dart()

def isclick(x=0,y=0):
    global i
    global begin_pos
    global end_pos
    x_r = abs(x - x_offset) // m_width
    y_r = abs(y - (y_offset+10)) // m_width
    if arr[int(y_r)][int(x_r)] == 0:
        arr[int(y_r)][int(x_r)] = i
        if i == 1:
            begin_pos = (int(x_r),int(y_r))
        elif i == 2:
            end_pos = (int(x_r),int(y_r))
        if i < 3:
            i= i + 1
    dart()
if __name__ == "__main__":
    main()
    mainloop()





