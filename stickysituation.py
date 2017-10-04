num = input()
sides = input()
sides = sides.split()
sides = [int(x) for x in sides]
sides.sort()
yes = False

many = len(sides)
for x in range(2,many):
    if(sides[x] < sides[x-1] + sides[x-2]):
       yes = True

if (yes == True):
    print ("possible")
else:
    print ("impossible")
