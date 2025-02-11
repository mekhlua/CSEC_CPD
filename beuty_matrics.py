all=[]
for i in range(5):
    matrics=list(map(int,input().split()))
    all.append(matrics)
for i,matrics in enumerate(all):
    for k,l in enumerate (matrics):
        if all[i][k]==1:
            x=abs(i-2),abs(k-2)
            break
print(sum(x))