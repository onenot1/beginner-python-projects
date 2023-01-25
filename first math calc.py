
def set_up_inputs(input_text):
    new_input = input(input_text)
    return new_input


def handle_math(operator, num1, num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "/":
        return num1/num2
    elif operator == "*":
        return num1*num2


def handle_math_input(math_input):
    num_one_input = set_up_inputs("Enter the first number:\n")
    num_two_input = set_up_inputs("Enter the second number:\n")
    print(handle_math(math_input, int(num_one_input), int(num_two_input)))


def handle_input(result_input):
    if result_input == "+" or result_input == "-" or result_input == "/" or result_input == "*":
        handle_math_input(result_input)
        handle_input(set_up_inputs("Select an operator [+,-,/,*]:\n"))
    else:
        print("You must select a valid operator.")
        handle_input(set_up_inputs("Select an operator [+,-,/,*]:\n"))


handle_input(set_up_inputs("Select an operator [+,-,/,*]:\n"))
