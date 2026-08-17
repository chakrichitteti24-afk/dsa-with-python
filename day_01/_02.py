a = int(input("enter your first number"))
b = int(input("enter your second number"))
c = int(input("enter your third number"))

''' conditions'''
if a>=b and a>=c:
    largest =a
elif b>=a and b>=c:
    largest =b
else:
    largest =c 
print("he largest number", largest)