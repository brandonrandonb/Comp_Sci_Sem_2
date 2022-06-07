mynum = [6,9,32,28,15,22,3,18]

themax = mynum[0]
themin = mynum[0]
add = 0
avg = 0

for q in range (0,len(mynum)):
    if (mynum[q] >themax):
        mudamuda = themax = mynum[q]
        print(mudamuda)

for w in range (0,len(mynum)):
    if (mynum[w] < themin):
        ja = themin = mynum[w]
        print(ja)

for e in range (0,len(mynum)):
    add = add+mynum[e]
    avg = add/len(mynum)
    print(avg)