import random
#else
complainlist = ["What's that", "I hate that place", "No", "Too far", "Never been there"]
randomcomplain = random.randrange(0,len(complainlist))
#restaurants
restaurantlist = ["Panera", "Din Tai Fung", "Papa's Pizzeria", "Kirby Cafe"]
#menus
paneralist = ["Chicken Noodle Soup", "Bread", "Mac N Cheese", "Tomato Soup and Croutons", "Baked Potato Soup"]
dinlist = ["Xiao Long Bao", "Wood Ear Mushroom", "Kurobuta Pork Bun", "Sauteed Broccoli", "Sauteed Spinach"]
papalist = ["Pizza with excessive amounts of truffle", "Pizza that is ok", "Pizza that is not ok", "Pizza depression", "Pissa"]
kirbolist = ["Kirby's Soft Pancakes", "Waddle Dee's Luxurious Hayashi Rice", "Pop Star Curry", "King Dedede's Heaping Pizza", "Kawasaki's Fickly"]
#suggestions
randompanerasuggest = random.randrange(0,len(paneralist))
randomdinsuggest = random.randrange(0,len(dinlist))
randompapasuggest = random.randrange(0,len(papalist))
randomkirbosuggest = random.randrange(0,len(kirbolist))
#start
print("Panera, Din Tai Fung, or Papa's Pizzeria")
choic = str(input())
#choice
if choic == restaurantlist[0]:
    print(paneralist[0])
    print(paneralist[1])
    print(paneralist[2])
    print(paneralist[3])
    print(paneralist[4])
    print("Suggestion: " + paneralist[randompanerasuggest])
elif choic == restaurantlist[1]:
    print(dinlist[0])
    print(dinlist[1])
    print(dinlist[2])
    print(dinlist[3])
    print(dinlist[4])
    print("Suggestion: " + dinlist[randomdinsuggest])
elif choic == restaurantlist[2]:
    print(papalist[0])
    print(papalist[1])
    print(papalist[2])
    print(papalist[3])
    print(papalist[4])
    print("Suggestion: " + papalist[randompapasuggest])
elif choic == restaurantlist[3]:
    print(kirbolist[0])
    print(kirbolist[1])
    print(kirbolist[2])
    print(kirbolist[3])
    print(kirbolist[4])
    print("Suggestion: " + kirbolist[randomkirbosuggest])
else:
    print(complainlist[randomcomplain])