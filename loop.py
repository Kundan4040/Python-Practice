n=0 # where n is iterator
"""while(n<=5):
    print("Kundan", n) 
    n=n+1"""

# print the number from 1 to 100
"""i=1
while(i<=100):
    print(i) 
    i=i+1 """

# print number from 100 to 1
"""i=100
while(i>=1):
    print(i)
    i=i-1"""

# Print the mutiplication table of a number n
"""print("Enter any number to print the table of that number")
n=int(input())
i=1
while(i<=10):
    print(n*i)
    i=i+1
    """

#Print the element of the following  list using a loop
#num=[1,4,9,16,25,36,49,64,81,100]
#traverse karna on every element

"""idx=0
while(idx<len(num)):

    print(num[idx])
    idx=idx+1
"""
# Search for a number X in this tuple using loop
"""num=[1,4,9,16,25,36,49,64,81,100]
x=49
i=0
while(i<len(num)):
    if(num[i] == x):
        print("found at index",i)
    else:
        print("Finding ...")
    i=i+1"""

#break keywords
"""i=1
while i<=5:
    if(i==3):
        print(i)
        continue #skip
    i=i+1"""

#Print the element of the following list using a loop
"""nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)"""

#Search for a number X in this tuple using loop
nums=[1,4,9,16,25,36,49,64,81,100]
x=49
for var in nums:
    if(var==x):
        print("Number is founded",x)
        break

    else:
        print("finding")    