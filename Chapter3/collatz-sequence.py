# Collatz Sequence
import sys
def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

print("Type in a number:")
try:
    number = int(input())
except ValueError:
    print("Invalid input: You must enter an integer.")
    sys.exit()

while number != 1:
    number = collatz(number)
