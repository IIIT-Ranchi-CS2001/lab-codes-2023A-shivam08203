x=str(input("Enter name: "))
y=int(input("Enter roll: "))
z=int(input("Enter marks: "))
g=0
f="fail"
if(z>=90):
    g=10
    f="outstanding"
    
elif(z<90 and z>=80):
    g=9
    f="very good"
    
elif(z<80 and z>=70):
    g=8
    f="good"
    
elif(z<70 and z>=60):
    g=7
    f="average"
    
elif(z<60 and z>=50):
     g=6
     f="pass"
     
elif(z<50):
  g=0
  f="fail"
  
print("Name:",x)
print("Roll:",y)
print("Marks:",z)
print("Grade:",g)
print("Remark:",f)
