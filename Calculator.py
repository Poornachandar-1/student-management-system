print("simple calculator")
num1 = float(input("Enter first number: "))
operator = input("Enter operetor (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))
if operator == "+":
    print("Result =", num1 + num2)
elif operator == "-":
    print("Result =", num1 - num2)
elif operator == "*":
    print("Result =", num1 * num2)
elif operator == "/":
    print("Result =", num1 / num2)
elif operator == "%":
    print("Result =", num1 % num2)
else:
    print("Invalid Operator")
