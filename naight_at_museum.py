s=input()
first=ord('a')
v=0
for i in s:
    current=ord(i)
    v+=min(abs(current-first),26-abs(current-first))
    first=current
print(v)