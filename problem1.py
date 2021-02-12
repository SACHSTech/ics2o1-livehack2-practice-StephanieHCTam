"""
-------------------------------------------------------------------------------
Name:     problem1.py
Purpose:  This program determines if a triangle is a right angle triangle.

Author:   Tam.S

Created:  12/02/2021
------------------------------------------------------------------------------
"""

print(" ****** Right Triangle Calculator ****** ")

# get side lengths of triangle
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# calculate squares
square1 = side1**2
square2 = side2**2
square3 = side3**2

# determine and output if sides make a right triangle
if (square1 + square2 == square3) or (square1 + square3 == square2) or (square2 + square3 == square1): 
  print("A triangle with lengths " + str(side1) + ", " + str(side2) + ", and " + str(side3) + " forms a right-angled triangle.")
else:
  print("A triangle with lengths " + str(side1) + ", " + str(side2) + ", and " + str(side3) + " does not form a right-angled triangle.")