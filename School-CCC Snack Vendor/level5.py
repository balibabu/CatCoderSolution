def get_row_col(grid):
    row=ord(grid[0])-64
    col=int(grid[1:])
    return row,col
def distance(p1,p2):
    x1,y1=get_row_col(p1)
    x2,y2=get_row_col(p2)
    if x1==x2 or y1==y2:
        return abs(x1-x2)+abs(y1-y2)

    if x1>x2:
        pass
    else:
        x1,x2=x2,x1
        y1,y2=y2,y1
        
    x=x1-x2
    if y1>y2:
        y=y1-y2-x
    else:
        y=y2-y1-x
    if y<0: y=0
    return x+y

inp=input()
data=inp.split()
gridSize=data[0]
p1=data[1]
p2=data[2]
print(distance(p1,p2))