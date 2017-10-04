def func():
    x = input()
    two = x.split()
    H = int(two[0])
    if(len(two)==1):
        return (2**(H+1))-1
    top = (2**(H+1))-1
    letters = len(two[1])
    LR = str(two[1])
    for n in range(letters):
        top -= 2**n
    linelength = 2**letters
    newlinelength = linelength
    position = 0
    for yes in range(letters):
        if LR[yes] == "L":
            position += 0
        elif LR[yes] == "R":
            position += newlinelength/2
        newlinelength /= 2
    return int((top-position))
print (func())
    
