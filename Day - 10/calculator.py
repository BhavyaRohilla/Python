def addition(n1, n2):
    return n1 + n2


def substraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": addition, "-": substraction, "*": multiply, "/": divide}


def calculator():
    num1 = float(input("What's the first number? : "))

    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (
            input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator. : "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
