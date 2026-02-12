import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
num1 = 12
num2 = 18
print(lcm(num1, num2))
