def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        print("Ділення на нуль неможливе.")
        return
    return x / y

arg1 = float(input("Веддіть перше число:"))
arg2 = float(input("Введіть друге число:"))
operation = input("Введіть математичну операцію (+, -, *, /):")

if operation == "+":
    result = add(arg1, arg2)
elif operation == "-":
    result = subtract(arg1, arg2)
elif operation == "*":
    result = multiply(arg1, arg2)
elif operation == "/":
    result = divide(arg1, arg2)
else:
    result = "Недопустима операція"

print("Результат:", result)

