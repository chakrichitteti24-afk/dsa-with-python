n= int(input("enter a number"))

count =0
while n>0:
    n=n//10
    count=count+1
print("the digits",count)