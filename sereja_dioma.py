x=int(input())
cards = list(map(int, input().split()))
s=0
d=0
h=True

while cards:
    if cards[0]>cards[-1]:
        j=cards.pop(0)
    else:
        j=cards.pop(-1)
    
    if h:
            s+=j
    else:
            d+=j
    h=not h
print(s,d)

