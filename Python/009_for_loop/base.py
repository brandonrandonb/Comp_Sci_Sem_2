a = int(input("how long do you want your line to be? "))
b = input("do you want your line to be vertical or horizontal? ")

if b == "v":
    for a in range(0,a):
        print("*", "")
elif b == "h":
    for a in range(0,a):
        print("*", end="")

 