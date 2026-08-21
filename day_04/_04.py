a =int(input("enter you st number"))
b= int(input("enter your end number"))
count = 0

for n in range(a,b+1):
    factors=0
    for i in range(1,n+1):
        if n%i ==0:
             factors=factors+1
    if factors==2:
        count=count+1
print(count)
