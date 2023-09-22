def filtra_pares(tup):
    a=(tup[0])
    b=(tup[1])
    c=(tup[2])
    d=(tup[3])

    if int(a%2==0) and int(b%2==0) and int(c%2==0) and int(d%2==0):
        return ((a,b,c,d))
    elif int(a%2==0) and int(b%2==0) and int(c%2==0) and int(d%2!=0):
        return ((a,b,c))
    elif int(a%2==0) and int(b%2==0) and int(c%2!=0) and int(d%2==0):
        return ((a,b,d))
    elif int(a%2==0) and int(b%2!=0) and int(c%2==0) and int(d%2==0):
        return ((a,c,d))
    elif int(a%2!=0) and int(b%2==0) and int(c%2==0) and int(d%2==0):
        return ((b,c,d))
    elif int(a%2==0) and int(b%2!=0) and int(c%2!=0) and int(d%2!=0):
        return ((a,))
    elif int(a%2==0) and int(b%2==0) and int(c%2!=0) and int(d%2!=0):
        return ((a,b))
    elif int(a%2==0) and int(b%2!=0) and int(c%2==0) and int(d%2!=0):
        return ((a,c))
    elif int(a%2==0) and int(b%2!=0) and int(c%2!=0) and int(d%2==0):
        return ((a,d))
    elif int(a%2!=0) and int(b%2==0) and int(c%2!=0) and int(d%2!=0):
        return ((b,))
    elif int(a%2!=0) and int(b%2==0) and int(c%2==0) and int(d%2!=0):
        return ((b,c))
    elif int(a%2!=0) and int(b%2==0) and int(c%2!=0) and int(d%2==0):
        return ((b,d))
    elif int(a%2!=0) and int(b%2!=0) and int(c%2==0) and int(d%2!=0):
        return ((c,))
    elif int(a%2!=0) and int(b%2!=0) and int(c%2==0) and int(d%2==0):
        return ((c,d))
    elif int(a%2!=0) and int(b%2!=0) and int(c%2!=0) and int(d%2==0):
        return ((d,))
    else:
        return ()