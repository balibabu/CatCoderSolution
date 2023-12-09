inp=input()
data=inp.split()
gridSize=data[0]
cursor=1
gridValues={}
stocks={}
stockCursor=(ord(gridSize[0])-ord('A')+1)*int(gridSize[1:])
for row in range(ord('A'),ord(gridSize[0])+1):
    for col in range(1,int(gridSize[1:])+1):
        ch=chr(row)+str(col)
        gridValues[ch]=int(data[cursor])
        stocks[ch]=int(data[cursor+stockCursor])
        cursor+=1
ordersCount=int(data[cursor+stockCursor])
orders=data[cursor+stockCursor+1:]
revenue=0
for order in orders:
    if stocks[order]>0:
        revenue+=gridValues[order]
        stocks[order]-=1
print(revenue)