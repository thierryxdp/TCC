defreceitaBolo(A,B,C):
    a= A//2
    b= B//3
    c= C//5
    if(a<=b and a<=c):
        return a
    else if(b<=a and b<=c):
        return b
    else(c<=a and c<=b):
    return c