a =int(input("enter your first number:"))
b= int(input("enter your second number:"))

x =a
y=b
while y!=0:
    x,y =y,x%y
print("gcd",x)
gcd =x
lcm =(a*b)//gcd
print("lcm",lcm)
