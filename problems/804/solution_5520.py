def filtra_pares(a):
    x,y,z,w=a
    a=(x,y,z,w)
    x=x%2==0
    y=y%2==0
    z=z%2==0
    w=w%2==0
    if x and y and z and w:
        return a
    elif x and y and z:
        return a[0:3]
    elif x and y and w:
        return a[0:2]+a[3]
    elif x and z and w:
        return a[0:1]+a[2]
    elif y and z and w:
        return a[1]
    elif x and y:
        return a[0:2]
    elif x and z:
        return a[0:1]+a[2:3]
    elif x and w:
        return a[0:1]+a[3]
    elif y and z:
        return a[1:3]
    elif y and w:
        return a[1:2]+a[3]
    elif z and w:
        return a[2:]
    elif x:
        return a[0:1]
    elif y:
        return a[1:2]
    elif z:
        return a[2:3]
    elif w:
        return a[3]
    else:
        return ()