a=int(input("enter the nuber:"))
f=0
for i in range(2,a):
    if (a%i)==0:
     f=1
     break
if f==0:
    print("number is prime")
else:
    print("number is not prime")