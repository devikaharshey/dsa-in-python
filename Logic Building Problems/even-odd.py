# Even or Odd
def evenOdd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
    
num = int(input("Enter a number: "))
print(evenOdd(num))