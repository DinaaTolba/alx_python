#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = '-' if number < 0 else ''
last_digit = abs(number) % 10

if number>0:
    if last_digit> 5:
        print("Last digit of", number,"is",last_digit,"and is greater than 5")
    else:
        if last_digit==0:
            print("Last digit of", number,"is",last_digit,"and is 0")

elif number<0:
    if last_digit == 0:
        print("Last digit of", number,"is",last_digit,"and is 0")
    else:
        print("Last digit of", number,"is",sign, last_digit,"and is less than 6 and not 0")
