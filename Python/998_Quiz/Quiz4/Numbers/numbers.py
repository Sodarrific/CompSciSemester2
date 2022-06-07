#list
lost = [6,9,32,28,15,22,3,18]

#average variables
average = 0

#average
for i in range(0,len(lost)):
    average = average + lost[i]
finalaverage = average / len(lost)

#minimum variables
minimum = lost[0]
finalminimum = 0

#min
for i in range(0,len(lost)):
    if minimum > lost[i]:
        finalminimum = lost[i]

#maximum variables
maximum = lost[0]
finalmaximum = 0

#max
for i in range(0,len(lost)):
    if maximum < lost[i]:
        finalmaximum = lost[i]

#what am i doing
print(finalaverage)
print(finalminimum)
print(finalmaximum)