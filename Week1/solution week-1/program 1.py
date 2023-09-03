#Write a python script to enter any number and check its prime or not.
n=int(input("Enter any number:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("{} is a prime number.".format(n))
else:
    print("{} is not a prime number.".format(n))
