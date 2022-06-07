#variable startup
x = 0
start = 0
end = 0
agestart = 0
ageend = 0
#number get
print("favorite number here")
numb = str(input())
#start the process
for i in range(0,len(numb)):
    if start == 0:
        if(numb[i:i+1] == "1"):
            start = i
        elif(numb[i:i+1]== "2"):
            start = i
        elif(numb[i:i+1]== "3"):
            start = i
        elif(numb[i:i+1]== "4"):
            start = i
        elif(numb[i:i+1]== "5"):
            start = i
        elif(numb[i:i+1]== "6"):
            start = i
        elif(numb[i:i+1]== "7"):
            start = i
        elif(numb[i:i+1]== "8"):
            start = i
        elif(numb[i:i+1]== "9"):
            start = i
        elif(numb[i:i+1]== "0"):
            start = i
    else:
        if(numb[i:i+1] == "1"):
            end = i + 1
        elif(numb[i:i+1]== "2"):
            end = i + 1
        elif(numb[i:i+1]== "3"):
            end = i + 1
        elif(numb[i:i+1]== "4"):
            end = i + 1
        elif(numb[i:i+1]== "5"):
            end = i + 1
        elif(numb[i:i+1]== "6"):
            end = i + 1
        elif(numb[i:i+1]== "7"):
            end = i + 1
        elif(numb[i:i+1]== "8"):
            end = i + 1
        elif(numb[i:i+1]== "9"):
            end = i + 1
        elif(numb[i:i+1]== "0"):
            end = i + 1

#number get
print("age here")
age = str(input())
#start the process again
for q in range(0,len(age)):
    if agestart == 0:
        if(age[q:q+1] == "1"):
            agestart = q
        elif(age[q:q+1]== "2"):
            agestart = q
        elif(age[q:q+1]== "3"):
            agestart = q
        elif(age[q:q+1]== "4"):
            agestart = q
        elif(age[q:q+1]== "5"):
            agestart = q
        elif(age[q:q+1]== "6"):
            agestart = q
        elif(age[q:q+1]== "7"):
            agestart = q
        elif(age[q:q+1]== "8"):
            agestart = q
        elif(age[q:q+1]== "9"):
            agestart = q
        elif(age[q:q+1]== "0"):
            agestart = q
    else:
        if(age[q:q+1] == "1"):
            ageend = q + 1
        elif(age[q:q+1]== "2"):
            ageend = q + 1
        elif(age[q:q+1]== "3"):
            ageend = q + 1
        elif(age[q:q+1]== "4"):
            ageend = q + 1
        elif(age[q:q+1]== "5"):
            ageend = q + 1
        elif(age[q:q+1]== "6"):
            ageend = q + 1
        elif(age[q:q+1]== "7"):
            ageend = q + 1
        elif(age[q:q+1]== "8"):
            ageend = q + 1
        elif(age[q:q+1]== "9"):
            ageend = q + 1
        elif(age[q:q+1]== "0"):
            ageend = q + 1
print(numb[start:end])
print(age[agestart:ageend])
actualnumb = (int(numb[start:end]))
actualage = (int(age[agestart:ageend]))
finalnumber = actualnumb * actualage
print(finalnumber)