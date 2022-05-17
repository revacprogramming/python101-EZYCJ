# Conditional Execution

hrs = input("Enter hours? ")
rate = input("enter hourly rate ")
h=float(hrs)
r=float(rate)
if h<40:
 pay=r*h
if h>40:
 pay=1.5*r*h
print(pay)