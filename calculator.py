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
        

