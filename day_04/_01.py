# find product of vectors
n= int(input("enter your number"))

product =1
while n>0:
    digit = n%10
    product=product*digit
    n=n//10
print(product)