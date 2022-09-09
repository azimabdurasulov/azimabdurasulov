from calendar import c
import imp
from math import*
a = int (input ("a="))
b = int (input ("b="))
c = int (input ("c="))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + sqrt(D)) /( 2*a )
    x2 = (-b - sqrt(D)) /( 2*a )
    print("Javob:", x1, "va", x2)
elif D == 0:
    x = -b / (2*a)
    print("Javob:", x)
else:
    print("Yechim yo`q")
print("Dastur tugadi")