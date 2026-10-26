nums=[1,35,56,78,42,56]
x=42
idx=0
for el in nums:
    if(el == x):
        print("number is found at idx",idx)
        break
    idx +=1
