# Simple Interest Calculator
def simple_interest(p, r, t):
    return ((p * r * t) / 100)

p = int(input("Enter principal: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period: "))

print(f"Simple Interest: {simple_interest(p, r, t)}")