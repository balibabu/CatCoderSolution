inp=input()
data=inp.split()
price=int(data[0])
coins=list(map(int,data[2:]))
total=sum(coins)
if total>=price:
    print("CHANGE",total-price)
else:
    print("MISSING",price-total)