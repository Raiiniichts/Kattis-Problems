def tri(n):
    s = ''
    if n == 0:
        return
    else:
        for x in range (0,n+1):
            s += '\n'+('*'*x)
    return s
    

print (tri(7))

def starz(n):
    s2 = ''
    for x in range(n):
        s2 += '*'
    return s2 + '\n'
    
    
def recurvtri(n):
    if n ==  1:
        return starz(1)
    else:
        return recurvtri(n-1)+ starz(n)

print (recurvtri(7))
