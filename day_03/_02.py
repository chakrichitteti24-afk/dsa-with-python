a = int(input("enter your first number:"))
b=  int(input("enter your second number:"))

while b!=0:
    a,b =b,a%b
print("GCD:",a)