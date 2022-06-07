import random
word_list = []
#with open('allow_words.txt') as f:
 #   for line in f:
  #      l = line.strip()
   #     print(l)
    #    word_list.append(l)
        
num = random.randrange(12972)
answer = word_list[num]
print(answer)

a = 0
for i in range(0,6):
    guess = input("Guess a word! ")
    if guess == answer:
        print("Hooray!")
        a = 1
        break
    else:
        print("lol no")
        print("guess again")
if a == 0:
    print("son of a bitch-" + answer)