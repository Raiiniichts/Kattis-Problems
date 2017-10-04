import sys
dictionary = {'a' : '@', 'b' : '8', 'c': '(', 'd': '|)', 'e':'3', 'f': '#', 'g' :'6','h':'[-]','i':'|','j':'_|','k':'|<','l':'1','m':'[]\/[]','n':'[]\[]','o': '0','p':'|D','q':'(,)','r':'|Z','s':'$','t':"']['",'u':'|_|','v':'\/','w':'\/\/','x':'}{','y':"`/",'z':'2'}


x=input()
x = x.lower()
s = ""
for i in range (len(x)):
    if x[i].isalpha() == True:
        s += dictionary[x[i]]
    else:
        s += x[i]

print(s)


        
