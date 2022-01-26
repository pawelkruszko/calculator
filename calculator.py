import operator

menu = """Two Numbers Calculator:
operators:
  +
  -
  *
  /

MENU:
1. calculator
2. exit
"""
print(menu)

while True:

    menu_option = int(input("(type menu option number to continue): "))

    if menu_option not in (1, 2):
        print("Wrong menu option selected, try again.")
        continue

    if menu_option == 2:
        print("Exiting...")
        break

    # input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    # input sign
    signs = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    sign = input(f"Input operator {signs.keys()}: ")

    # calculating
    operation = signs.get(sign)
    if operation is None:
        print("Invalid operator")
    else:
        print(operation(num1, num2))
