#Write a python script to enter any number and print the sum of its digit.
n=int(input("Enter any number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of digits is ",sum)
