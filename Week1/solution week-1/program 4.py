#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not armstrong.
n=int(input("Enter any number:"))
temp=n
rev=0
while n!=0:
    rem=n%10
    rev=rev+(rem*rem*rem)
    n=n//10
if rev==temp:
    print("{} is a armstrong number.".format(temp))
else:
    print("{} is a not armstrong number.".format(temp))
