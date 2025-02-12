x=int(input())
s=input().split()
p=0
c=0
for i in s:
    if p==0 and int(i)<0:
        c+=int(i)
    else:
        p+=int(i)
print(abs(c))