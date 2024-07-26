# Write a Python Function to Find The Max Of Three.....
def max_of_three(a, b, c):
  if a >= b and a>=c:
    return a
  elif b >= a and b >= c :
    return b
  else :
    return c 
  
  
  
i = int(input("enter the number : "))  
o = int(input("enter the number : "))  
u = int(input("enter the number : "))   

print ("Max Of Three Numbers is " , max_of_three(i,o,u))



Max of Three Program

This program defines a function max_of_three that takes three numbers as input and returns the largest of the three. The function uses conditional statements to compare the values and determine the greatest.

Features:

- Takes three numbers as input
- Returns the largest of the three numbers
- Handles edge cases where two or more numbers are equal

