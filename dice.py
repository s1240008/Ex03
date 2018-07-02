import random

print("What is your name?")

name = raw_input()

print("Hello, "+name+"!")

print("Rolling the dice...")

c=0

for i in range(2):
    a=random.randrange(1,6)
    print("Die"+str(i+1)+": "+str(a))
    c+=a

print("Total value: "+str(c))

if c>=7:
    print(name+" Won!")

else :
    print(name+" Lose...")
