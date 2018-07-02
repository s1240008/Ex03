import random

print("Rolling the dice...")

c=0

for i in range(2):
    a=random.randrange(1,6)
    print("Die"+str(i+1)+": "+str(a))
    c+=a

print("Total value: "+str(c))
