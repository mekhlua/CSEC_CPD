import math
Y, W = map(int, input().split())
max_roll = max(Y, W)
favorable_outcomes = 6 - max_roll + 1
gcd = math.gcd(favorable_outcomes, 6)
numerator = favorable_outcomes // gcd
denominator = 6 // gcd
print(f"{numerator}/{denominator}")
