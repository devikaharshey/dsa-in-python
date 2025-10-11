# Simple Calculator
def calculator():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
        
    opr_range=('+','-','*','/','%')
    opr=input("Enter operator: ")
    
    while opr in opr_range:
       if opr == '+':
              print("Ans:",a+b)
              break
       elif opr == '-':
              print("Ans:",a-b)
              break
       elif opr == '*':
              print("Ans:",a*b)
              break
       elif opr == '/':
              if b==0:
                  print("Can't divide by 0!")
                  break
              else:
                  print("Ans:",a/b)
                  break
       elif opr == '%':
              print("Ans:",a%b)
              break
       else:
              print("Invalid Operator!")
        
calculator()
        
