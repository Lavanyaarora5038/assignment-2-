S1=int(input("Enter the length of 1st side : "))
S2=int(input("Enter the length of 2nd side : "))
S3=int(input("Enter the length of 3rd side : "))

if(S1+S2>S3 and S1+S3>S2 and S2+S3>S1):
    print("The triangle can be formed")

else:
    print("The triangle cannot be formed")