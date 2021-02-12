"""
-------------------------------------------------------------------------------
Name:     problem2.py
Purpose:  This program determines if a triangle is a right angle triangle.

Author:   Tam.S

Created:  12/02/2021
------------------------------------------------------------------------------
"""

print(" ****** Summer Destination Calculator ****** ")

# get mark
mark = float(input("Enter your mark: "))

# get earnings before the summer
earnings = float(input("Enter your earnings before summer: "))

# compute and output summer destination
if mark >= 80 and earnings >= 500:
  print("You get to go to Europe!")
elif mark >= 80:
  print("You get to go to California!")
else:
  print("You don't get to go away.")