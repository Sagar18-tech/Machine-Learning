x=input("Enter number 1:")
y=input("Enter number 2:")
op=input("Enter operator(+,-,*,/):")

if op=='+':
    print("Result is x+y:",int(x)+int(y))
elif op=='-':
    print("Result is x-y:",int(x)-int(y))
elif op=='*':
    print("Result is x*y:",int(x)*int(y))
elif op=='/':
    print("Result is x/y:",int(x)/int(y))
else:
    print("Invalid operator")