n = int(input("enter your number:"))

original =n
sum =0
while n>0:
    digit =n%10
    sum=sum+digit**3
    n=n//10
if sum==original:
    print("the   given number is armstrong number is ",original)
else:
    print("the number is not armstrong number")