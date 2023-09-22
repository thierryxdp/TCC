def filtra_pares(x,y,z,w):
    if x%2==0 and y%2==0 and z%2==0 and w%2==0:
        return (x,y,z,w)
    if x%2==0 and y%2==0 and z%2==0 and not w%2==0:
        return (x,y,z)
    if x%2==0 and y%2==0 and not z%2==0 and not w%2==0:
        return (x,y)
    if x%2==0 and not y%2==0 and not z%2==0 and not w%2==0:
        return (x)
    if x%2!=0 and y%2==0 and not z%2==0 and not w%2==0:
        return (y)
    if x%2!=0 and not y%2==0 and z%2==0 and not w%2==0:
        return (z)
    if x%2!=0 and y%2==0 and z%2==0 and w%2==0:
        return (y,z,w)
    if x%2!=0 and not y%2==0 and z%2==0 and w%2==0:
        return (z,w)
    if x%2!=0 and not y%2==0 and not z%2==0 and w%2==0:
        return (w)
    if x%2!=0 and not y%2==0 and not z%2==0 and not w%2==0:
        return ()
    if x%2==0 and not y%2==0 and not z%2==0 and w%2==0:
        return (x,w)
    if x%2==0 and not y%2==0 and  z%2==0 and not w%2==0:
        return (x,z)
    if x%2!=0 and y%2==0 and  z%2==0 and not w%2==0:
        return (y,z)
    if x%2!=0 and y%2==0 and not z%2==0 and w%2==0:
        return (y,w)
    if a%2==0 and not y%2==0 and z%2==0 and w%2==0:
        return (x,z,w)
    if a%2==0 and  y%2==0 and not z%2==0 and w%2==0:
         return (x,y,w)