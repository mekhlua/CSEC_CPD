present=input().split()
x=int(present[0])
y=int(present[1])
for i in range(y):
    x*=3 
    y*=2  
    if(x>y):
        print(i+1)
        break