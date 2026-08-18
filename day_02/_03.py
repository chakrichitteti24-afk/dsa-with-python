n =int(input("enter your number"))

original = n
reverse =0
while n>0:
    digest=n%10
    reverse=reverse*10+digest
    n=n//10
if original==reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")