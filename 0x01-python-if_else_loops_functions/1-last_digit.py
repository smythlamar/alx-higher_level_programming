#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = int(number % 10)
    print(f"Last digit of {number} is {last_digit}")
elif number < 0:
    last_digit = int(number % -10)
    print(f"Last digit of {number} is {last_digit}")
else:
    print(f"Last digit of {number} is zero")
