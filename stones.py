x=int(input())
s=input()
z=0
for i in range(x-1):
    if s[i]==s[i+1]:
        z+=1
print(z)