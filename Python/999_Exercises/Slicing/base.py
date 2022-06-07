x = 0
y = 1
q=input("please enter name. \n")
for i in range (0,len(q)):
    print(q[x:y])
    x = x + 1
    y = y + 1
if(q[x:y] == " "):
    print(q[x:len(q)])
    print(q[0:x])
    
    
    
    
    
    
    
    