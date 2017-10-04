import sys

x = input("number")
print(x)
x = x.splitlines()
s = ""
def snowflakeRun(x):
    print (x)
    num = x[0]
    L = x[1]
    for times in range (num):
        length = x[1+L]
        snowflake(length, L+2)
        L += length
def snowflake(length,start):
    flakeList = x[start, start+length]
    for num in range (length):
        streak = flakeList.index(x, start, start+length) - num
        streakList.append(streak)
    s+= "/n" + max(streakList)
snowflakeRun(x)
print (s)

    
        
        
    
