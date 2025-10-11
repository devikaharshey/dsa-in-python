# Closest Number
def closestNumber(n, m):
   q = int(n // m)

   num1 = m * q

   if((n * m) > 0):
      num2 = (m * (q + 1))
   else:
      num2 = (m * (q - 1))

   if(abs(n - num1) < abs(n - num2)):
      return num1
   
   return num2

n = int(input("Enter value of n: "))
m = int(input("Enter value of m: "))
print(f"Closest number is: {closestNumber(n, m)}")