def bolos(a,b,c):
    a=(3/2)*b
    a=(5/2)*c
    
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c