birth = 11
print("What month in number is my birthday")
guesss = (input())
guess = int(guesss)
if guess == 11:
    print("yeh")
if guess < 11:
    print("too early")
if guess > 11:
    print("too late")