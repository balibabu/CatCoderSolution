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
price=int(data[0])
coins=list(map(int,data[2:]))
total=sum(coins)
if total>=price:
    change=get_change(total-price)
    print("CHANGE",end=' ')
    for i in change:
        print(i,end=' ')
else:
    print("MISSING",price-total)