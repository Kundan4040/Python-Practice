print("Enter the thre number")
num1=int(input("enter the first number"))
num2=int(input("enter the first number"))
num3=int(input("enter the first number"))

"""if(num1>num2):
    if(num1>num3):
        print("num1 is the Greatest :", num1)
    else:
        print(" Num3 is greatest : ",num3)
elif(num2>num1):
    if(num2>num3):
        print("num2 is greatest : ", num2)
    else:
        print("num3 is greatest: ",num3) 
else:
    print("input the correct number")"""
if(num1>num2 and num1>num3):
    print("number1 is greatest : ", num1)
elif(num2>=num3):
    print("num2 is greatest ")
else:
    print("num3 is greatest : ", num3)

