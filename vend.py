friends_height=input().split()
x=0
freinds=input().split()
for i in range(int(friends_height[0])):
    if int(freinds[i])>int(friends_height[1]):
        x+=2
    else:
        x+=1
print(x)
    