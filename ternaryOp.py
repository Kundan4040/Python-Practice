age=int(input("enter the your age : "))
# first method 
b="your are eligible" if age>=18 else "not eligible"
print(b)

#second method

print("you are eligible") if age>=18 else print("you are not eligible")

#third method which is clever method 
age1=20
c=("eligible", "not eligible")[age1>=18]
print(c)