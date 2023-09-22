def filtra_pares(a):
    """Retorna apenas os elementos pares da tupla
    int, int, int, int"""
    # se todos forem pares
    if (a[0])%2==0 and (a[1])%2==0 and (a[2])%2==0 and (a[3])%2==0:
        return a[0],a[1],a[2],a[3]
    # se apenas um for par
    elif (a[0])%2==0 and (a[1])%2!=0 and (a[2])%2!=0 and (a[3])%2!=0:
        return (a[0],)
    elif (a[0])%2!=0 and (a[1])%2==0 and (a[2])%2!=0 and (a[3])%2!=0:
        return (a[1],)
    elif (a[0])%2!=0 and (a[1])%2!=0 and (a[2])%2==0 and (a[3])%2!=0:
        return (a[2],)
    elif (a[0])%2!=0 and (a[1])%2!=0 and (a[2])%2!=0 and (a[3])%2==0:
        return (a[3],)
    # se dois forem pares
    elif (a[0])%2==0 and (a[1])%2==0 and (a[2])%2!=0 and (a[3])%2!=0:
        return (a[0],a[1])
    elif (a[0])%2==0 and (a[1])%2!=0 and (a[2])%2==0 and (a[3])%2!=0:
        return (a[0],a[2])
    elif (a[0])%2==0 and (a[1])%2!=0 and (a[2])%2!=0 and (a[3])%2==0:
        return (a[0],a[3])
    elif (a[0])%2!=0 and (a[1])%2==0 and (a[2])%2==0 and (a[3])%2!=0:
        return (a[1],a[2])
    elif (a[0])%2!=0 and (a[1])%2==0 and (a[2])%2!=0 and (a[3])%2==0:
        return (a[1],a[3])
    elif (a[0])%2!=0 and (a[1])%2!=0 and (a[2])%2==0 and (a[3])%2==0:
        return (a[2],a[3])
    # se três forem pares
    elif (a[0])%2==0 and (a[1])%2==0 and (a[2])%2==0 and (a[3])%2!=0:
        return (a[0],a[1],a[2])
    elif (a[0])%2==0 and (a[1])%2==0 and (a[2])%2!=0 and (a[3])%2==0:
        return (a[0],a[1],a[3])
    elif (a[0])%2!=0 and (a[1])%2==0 and (a[2])%2==0 and (a[3])%2==0:
        return (a[1],a[2],a[3])
    elif (a[0])%2==0 and (a[1])%2!=0 and (a[2])%2==0 and (a[3])%2==0:
        return (a[0],a[2],a[3])
    else:
        return ()