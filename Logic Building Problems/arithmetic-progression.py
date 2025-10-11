# Arithmetic Progression (AP)
def arithmetic_progression(arr):
    d = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if (arr[i] - arr[i-1]) != d:
            return False
        
    return True

arr = []
n = int(input("Enter size of array: "))
print("Enter the elements: ")
for i in range(n):
    num = int(input())
    arr.append(num)

arr.sort()

print(f"The given array is an AP? {arithmetic_progression(arr)}")