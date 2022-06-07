import random

resta = ["Greasy Grove", "Pizza Pit", "Taco Town "]
GG = ["Burger ", "Soda ", "Ice Cream "]
PP = ["Pizza ", "Juice ", "Breadsticks "]
TT = ["Taco ", "Cola ", "Salsa "]
a = input("Choose a restaurant, Greasy Grove, Pizza Pit, or Taco Town \n")
b = random.randrange(0,3)



if a == "Greasy Grove":
    random.randrange(0,len(GG))
    print(GG)
    print("The suggested menu item for Greasy Grove is: ")
    print(GG[b])

elif a == "Pizza Pit":
    random.randrange(0,len(PP))
    print(PP)
    print("The suggested menu item for Pizza Pit is: ")
    print(PP[b])
    
elif a == "Taco Town":
    random.randrange(0,len(TT))
    print(TT)
    print("The suggested menu item for Taco Town is: ")
    print(TT[b])