import sys

sentinel = '' # ends when this string is seen
temp = []
num = input()
string = input()
temp.append(num)
temp.append(string)

rolls = temp[1]
tally = [rolls.count('1'),rolls.count('2'),rolls.count('3'),rolls.count('4'),rolls.count('5'),rolls.count('6')]

theone = -1

for x in range (len(tally)):
    if(tally[x] == 1):
            theone = x
if(theone == -1):
    print ("none")
else:  
    find = theone+1
    rolls = rolls.replace(" ","")
  
      
    print (rolls.index(str(find))+1)



