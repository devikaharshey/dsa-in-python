# Sum of First N Natural Numbers
def sumOfNaturalNumbers(num):
    sum = 0
    for i in range(1, num+1):
        sum += i

    return sum

num = int(input("Enter a number: "))
print(f"Answer is: {sumOfNaturalNumbers(num)}")