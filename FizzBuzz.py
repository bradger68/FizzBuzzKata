import math

def FizzBuzz(entry):
    if entry % 3 == 0 and entry % 5 == 0:
        return "FizzBuzz"
    elif entry % 3 == 0 and entry % 5 != 0:
        return "Fizz"
    elif entry % 3 != 0 and entry % 5 == 0:
        return "Buzz"
    else:
        return "."