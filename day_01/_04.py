n = int(input("enter your number:"))
sum1 =0
sum2 =0
for i in range(1,n+1):
    if i%2==0:
        sum1+=i
    else:
        sum2+=i
print("the even numbers are",sum1)
print("the odd numbersare ",sum2)
print("the numbers are:",sum1+sum2)