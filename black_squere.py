n=list((input().split()))
s=input()
x=0
for j in s:
    x+=int(n[int(j)-1])
print(x)