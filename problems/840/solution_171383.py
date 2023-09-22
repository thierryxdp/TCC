def bolo(A,B,C):
    a=A//2
    b=B//3
    c=C//5
    if(a=0 or b=0 or c=0):
    return 0
    elif(a<=b and a<=c):
        return a
    elif(b<=a and b<=c):
        return b
    else(c<=a and c<=b):
        return c