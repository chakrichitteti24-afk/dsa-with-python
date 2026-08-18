n = int(input("enter your number"))

reverse = 0
while n>0:
    digest =n%10
    reverse=reverse*10+digest
    n=n//10
print("the reverse number",reverse)