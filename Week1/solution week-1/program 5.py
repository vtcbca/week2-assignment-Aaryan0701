#Write a python script to enter any string and count vowel.
sen=input("Write sentence:")
vowel=0
for i in range(len(sen)):
    if sen[i] in ['a','e','i','o','u','A','E','I','O','U']:
        vowel+=1
print("{} contains {} vowles.".format(sen,vowel))
