n = int(input("enter your number"))

if n<=1:
    print("the number is not prime")
else:
    prime= True
    for i in range(2,n+1):
        if n%i ==0:
            prime = False
            break
    if prime:
        print("the number is prime number")
    else:
        print("the number is not prime number")
