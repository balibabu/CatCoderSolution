def get_row_col(grid):
    row=ord(grid[0])-64
    col=int(grid[1:])
    return row,col

def distance(x1,y1,x2,y2,defect):
    if x1==x2:
        dis=abs(x1-x2)+abs(y1-y2)
        if y1<y2:
            if defect==0:
                return dis + dis%2
        else:
            if defect==4:
                return dis + dis%2
        return dis
    
    if y1==y2:
        dis=abs(x1-x2)+abs(y1-y2)
        if x1<x2:
            if defect==6:
                return dis + dis%2
        else:
            if defect==2:
                return dis + dis%2
        return dis

            

    
    if x1>x2 and y1>y2:
        if defect==3:
            return x1-x2+y1-y2
        else:
            d=min(x1-x2,y1-y2)
            return d+distance(x1=x1-d,y1=y1-d,x2=x2,y2=y2,defect=defect)
    elif x1>x2 and y1<y2:
        if defect==1:
            return x1-x2+y2-y1
        else:
            d=min(x1-x2,y2-y1)
            return d+distance(x1=x1-d,y1=y1+d,x2=x2,y2=y2,defect=defect)
        
    elif x1<x2 and y1>y2:
        if defect==5:
            return x2-x1+y1-y2
        else:
            d=min(x2-x1,y1-y2)
            return d+distance(x1=x1+d,y1=y1-d,x2=x2,y2=y2,defect=defect)
    
    else:
        if defect==7:
            return x2-x1+y2-y1
        else:
            d=min(x2-x1,y2-y1)
            return d+distance(x1=x1+d,y1=y1+d,x2=x2,y2=y2,defect=defect)
        

inp=input()
data=inp.split()
gridSize=data[0]
p1=data[1]
p2=data[2]
defect=int(data[3])
x1,y1=get_row_col(p1)
x2,y2=get_row_col(p2)
print(distance(x1,y1,x2,y2,defect))