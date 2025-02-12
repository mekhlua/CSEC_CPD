lst=list(map(int,input().strip().split()))
se=set(lst)
n=len(lst)-len(se)
print(n)