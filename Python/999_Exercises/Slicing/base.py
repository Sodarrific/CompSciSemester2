#start individual letters
print("Name?")
name = str(input())
y = 1
z = 1
space = ' '
#for individual letters
for i in range(0,len(name)):
    print(name[i:y])
    y = y + 1

#start last first
for t in range(0,len(name)):
    g = name[t]
    if g == space:
        break
    z = z + 1

print(name[z:len(name)])
print(name[0:z])