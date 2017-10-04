import sys

sentinel = '' # ends when this string is seen
for line in iter(input, sentinel):
    if(line == "0 0 0 0"):
        break
    else:
        locks = line.split()
        degrees = 720 + 360
        if(int(locks[1])>int(locks[0])):
            degrees +=(40-(int(locks[1])-int(locks[0])))*9
        else:
            degrees +=((int(locks[0])-int(locks[1])))*9
        if(int(locks[1]) > int(locks[2])):
            degrees +=(40-(int(locks[1])-int(locks[2])))*9
        else:
            degrees +=((int(locks[2])-int(locks[1])))*9
        if(int(locks[3]) > int(locks[2])):
            degrees +=(40-(int(locks[3])-int(locks[2])))*9
        else:
            degrees +=((int(locks[2])-int(locks[3])))*9
        print(degrees)
