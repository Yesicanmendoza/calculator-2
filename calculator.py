"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter your equation > ")
    token_input = user_input.split(" ")
    if token_input[0] == "q":
        break
    elif token_input[0] == "pow":
        result = power(int(token_input[1]),int(token_input[2]))
        print(float(result))
    elif token_input[0] == "add":
        result = add(int(token_input[1]),int(token_input[2]))
        print(float(result))
    elif token_input[0] == "subtract":
        result = subtract(int(token_input[1]),int(token_input[2]))
        print(float(result))
    elif token_input[0] == "multiply":
        result = multiply(int(token_input[1]),int(token_input[2]))
        print(float(result))
    elif token_input[0] == "divide":
        result = divide(int(token_input[1]),int(token_input[2]))
        print(float(result))
    elif token_input[0] == "square":
        result = square(int(token_input[1]))
        print(float(result))
    elif token_input[0] == "cube":
        result = cube(int(token_input[1]))
        print(float(result))
    elif token_input[0] == "mod":
        result = mod(int(token_input[1]),int(token_input[2]))
        print(float(result))


