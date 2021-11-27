## app <--- two integes      <--- user
##     <--- choose operation <--- user
##          display result   <--- user



def ii (which):  # which = "first"
    print("Enter",which,"integer:  ", end= "") 
    return int(input())


a = ii("first")
b = ii ("Second")

## HW1, next operation: / - * , if the user choses an inexistent operation
## -> "worng operation"

#a = int(input("Enter first interger:"))     # a = 1
#b = int(input("Enter second interger:"))    # b = 2
 
op = input ("Choose operation (* / + -): ")  # op = "+"

res = 0

if op == "+":
    res = a + b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
elif  op == "-":
    res = a - b
else:
    print("WORNG OPERATION !!!")         

print("Result:" , res)
