# Write a Python program to get the volume of a sphere

import math

radius = float(input("Enter the radius of the sphere: "))

v = ((4.0/3.0) * math.pi * radius**3)  # volume = 4/3*π*r^3
print(v)
