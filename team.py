n=int(input())
lines=[]
x=0
for i in range(n):
    line=list(map(int,input().split()))
    lines.append(line)
    if sum(lines[i])>=2:
        x+=1
print(x)

