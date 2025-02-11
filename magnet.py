n=int(input())
s=[]
for i in range(n):
    s.append(input())
j=1
for i in range(1,n):   
    if s[i]!=s[i-1]:
        j+=1
print(j)