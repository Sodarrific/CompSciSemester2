number11 = (input())
number12 = int(number11)
equation1 = (input())
number21 = (input())
number22 = int(number21)
plus = ("+")
minus = ("-")
divid = ("/")
multi = ("*")

if equation1 == plus:
    print(number12+number22)
elif equation1 == minus:
    print(number12-number22)
elif equation1 == divid:
    print(number12/number22)
elif equation1 == multi:
    print(number12*number22)
else:
    print("what")