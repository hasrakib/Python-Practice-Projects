# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math  # for pi value & power
import turtle  # to draw the circle

radius = float(input("What is the radius of the circle "))
pi_value = math.pi

area = pi_value * math.pow(radius, 2)

print(area)

t = turtle.Turtle()
t.circle(radius)
turtle.done()
