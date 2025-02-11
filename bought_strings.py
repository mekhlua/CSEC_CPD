first_string =input()
second_string =input()
x=first_string.lower()
y=second_string.lower()
if(x==y):
    print("0")
elif(x<y):
    print("-1")
else:
    print("1")