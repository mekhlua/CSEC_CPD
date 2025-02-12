s = input().strip()  
t = input().strip() 
position = 0
for instruction in t:
    if instruction == s[position]:
        position += 1    
        if position >= len(s):
            break
print(position + 1)
