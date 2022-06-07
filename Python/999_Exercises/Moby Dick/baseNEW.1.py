x=0

sent = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
print(sent)
for i in range (0,len(sent)):
    if sent[i:i+5] == "whale":
        x=x+1
print("There are " + str(x) + " whales in this sentence.")











