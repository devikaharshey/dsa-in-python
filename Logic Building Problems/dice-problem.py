# Guess Opposite Number on Dice
def guess_opposite_number(num):
    return 7-num

num = int(input("Enter a dice number: "))
print(f"It's opposite number is {guess_opposite_number(num)}")