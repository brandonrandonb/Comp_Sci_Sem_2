import random

x = int(input("How many random numbers would you like? the max is 10. "))
thislist=[]
for i in range(0,x):
    thislist.append(print(random.randrange(1,10), end=", "))
    