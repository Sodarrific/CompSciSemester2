sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
y = 0
z = 1
whale = "whale"


for t in range(0,len(sentence)):
    g = sentence[t]
    if g == whale:
        y = y + 1
    z = z + 1

print(y)










#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
