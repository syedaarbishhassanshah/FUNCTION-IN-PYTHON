#write a python function to find the Max of Three....
def max_of_three(a,b,c):
    if a>=b and a>=c:
      return a
    elif b>=a and b>=c:
      return b
    else :
      return c
  
  
  
i = int(input("enter the number :"))
o = int(input("enter the number :"))
u = int(input("enter the number :"))

print("Max of Three Numbers is : ", max_of_three(i,o,u))