#Write a python script to enter any string, replace vowel with its position number.
name=input("Enter any name:")
new_name=""
for i in range(len(name)):
    if name[i] in ['a','e','i','o','u']:
        new_name+=str(i)
    else:
        new_name+=name[i]
print(new_name)
