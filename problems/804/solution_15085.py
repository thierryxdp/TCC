def filtra_pares(x,y,w,z):
    'fsdfsd'
    tup=(x,y,w,z)
    if tup[0]%2==0:
        if tup[1]%2==0:
            if tup[2]%2==0:
                if tup[3]%2==0:
                    return tup
                else:
                    return (x,y,w)
            elif tup[3]%2==0:
                return (x,y,z)
            else:
                return (x,y)