a = int(input("How many things do you want to buy? \n"))
d = 0
for z in range (0,a):
    b = input("What items are you buying? \n")
    c = float(input("How much is this item? \n"))
    d = d+c
print("Your total is: $" + str(d))

