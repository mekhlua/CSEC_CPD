n=int(input())
sa=[]
h=[]
g=[]
z=0
for i in range(n):
    s=input().split()
    sa.append(s)

for i in sa:
    h.append(i[0])
    g.append(i[1])
for i in h:
    if i in g:
        z+=g.count(i)
print(z)
        


