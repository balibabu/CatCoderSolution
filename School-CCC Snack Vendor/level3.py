def get_change(money):
    change=[1, 2, 5, 10, 20, 50, 100, 200]
    returnChange=[]
    note=change[-1]
    noteCount=0
    while change:
        note=change[-1]
        if note>money:
            change.pop()
            returnChange.insert(0,noteCount)
            noteCount=0
        else:
            noteCount+=1
            money-=note
    return returnChange

inp=input()
data=inp.split()
gridSize=data[0]
cursor=1
gridValues={}
for row in range(ord('A'),ord(gridSize[0])+1):
    for col in range(1,int(gridSize[1:])+1):
        ch=chr(row)+str(col)
        gridValues[ch]=int(data[cursor])
        cursor+=1
order=data[cursor]
coins=list(map(int,data[cursor+2:]))
total=sum(coins)
price=gridValues[order]
if total>=price:
    change=get_change(total-price)
    print("CHANGE",end=' ')
    for i in change:
        print(i,end=' ')
else:
    print("MISSING",price-total)