#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
n=int(input("Enter any number:"))
temp=n
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==temp:
    print("{} is a palindrome number.".format(temp))
else:
    print("{} is a not palindrome number.".format(temp))
