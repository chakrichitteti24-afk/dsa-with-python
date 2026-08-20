n = int(input("enter youir numbers:"))

sum = 0
while n>0:
    digit = n%10
    sum = sum+digit
    n=n//10
print("the sum of digits is ", sum)