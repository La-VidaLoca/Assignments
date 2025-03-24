def calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"
op = (input("Enter Your Operation (add/sub/mul/div): "))
x =  int(input("Enter First Operand: "))
y =  int(input("Enter Second Operand: "))
print(calculator(x, y, op))