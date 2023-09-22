def filtra_pares(tup):
    w=tup[0]
    x=tup[1]
    y=tup[2]
    z=tup[3]
    
    if w%2==0:
        return w,
    if x%2==0:
        return x,
    if y%2==0:
        return y,
    if z%2==0:
        return z,
    if (z,x,y,z)%2==1:
        return ()