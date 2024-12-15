from math import*
a=int(input("enter 1st side: "))
b=int(input("enter 2nd side: "))
c=int(input("enter 3rd side: "))
if a+b<=c or a+c<=b or b+c<=a:
    print("The input values do not form a valid triangle.")
else:
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    perimeter=a+b+c

    angle_a=degrees(acos((b**2+c**2-a**2)/(2*b*c)))
    angle_b=degrees(acos((a**2+c**2-b**2)/(2*a*c)))
    angle_c=degrees(acos((a**2+b**2-c**2)/(2*a*b)))

    
    print("Perimeter: ", perimeter)
    print("Area: ", area)
    print(  angle_a)
    print( angle_b)
    print( angle_c)