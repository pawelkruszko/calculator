# create simple calculator based on float numbers
import operator


while True:
    # input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # input sign
    signs = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.itruediv
             }

    sign = input(f"Input operator {signs.keys()}: ")

    # calculating
    operation = signs.get(sign)
    if operation is None:
        print("Invalid operator")
    else:
        print(operation(num1, num2))

