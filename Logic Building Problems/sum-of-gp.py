# Geometric Progression (GP)
def sum_of_GP(a, r, n):
    if r == 1:
        return "Error"
    elif r < 1:
        return ((a * (1 - pow(r, n))) / (1 - r))
    else:
        return ((a * (pow(r, n) - 1)) / (r - 1))
    
a = float(input("Enter first term: "))
r = float(input("Enter common ratio: "))
n = int(input("Enter no. of terms: "))

print(f"Sum of GP: {sum_of_GP(a, r, n)}")