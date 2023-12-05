#!/usr/bin/python3
'''''
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
  print(number,"is positive")
elif number<0:
  print(number,"is negative")
else:
  print(number,"is zero")
  '''
#!/usr/bin/python3
import random
number = random.randint(-10, 10)


print(number,"is positive" if number > 0 else "is zero" if number == 0 else "is negative")
