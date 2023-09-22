def bolo(A,B,C):
    a=A//2
    b=B//3
    c=C//5
    if(a<=b and a<=c):
        return a
    elif(b<=c and b<=a):
        return b
    elif(c<=a and c<=b):
        return c
    else:
        return 0