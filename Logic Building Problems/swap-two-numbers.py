# Swapping Numbers
def swapTwoNumbers(a,b):
    c = a
    a = b
    b = c

    return a,b

a,b = map(int, input("Enter numbers: ").split())
print(f"Before swapping: a = {a}, b = {b}\n After swapping: a = {swapTwoNumbers(a,b)[0]}, b = {swapTwoNumbers(a,b)[1]}")