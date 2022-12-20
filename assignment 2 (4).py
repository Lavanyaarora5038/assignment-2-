x=int(input("x="))
y=int(input("y="))
z=int(input("z="))

if(x>y & x>z):
    print("x is greater than both y and z")

elif(y>x and y>z):
    print("y is greater than both x and z")

else:
    print("z is greater than both x and y")