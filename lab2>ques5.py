import math
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=b**2-4*a*c
if(d==0):
    print("both root are same:")
    print(-b/2*a)
elif(d>0):
    print("first root:",(-b + math.sqrt(d))/2*a)
    print("second root:",(-b-math.sqrt(d))/2*a)
else:
    print(" real part is",-b/(2*a))
    print(" imaginary_part:",math.sqrt(-d)/2*a)