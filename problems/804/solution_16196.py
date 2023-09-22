def filtra_pares(t):
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    if a%2!=0 and b%2==0 and c%2==0 and d%2==0:
        return ((b),(c),(d))
    elif b%2!=0 and a%2==0 and c%2==0 and d%2==0:
        return ((a),(c),(d))
    elif c%2!=0 and a%2==0 and b%2==0 and d%2==0:
        return ((a),(b),(d))
    elif d%2!=0 and a%2==0 and b%2==0 and c%2==0:
        return ((a),(b),(c))
    elif a%2!=0 and b%2!=0and c%2==0 and d%2==0:
        return ((c),(d))
    elif a%2!=0 and c%2!=0 and b%2==0 and d%2==0:
        return ((b),(d))
    elif a%2!=0 and  d%2!=0 and b%2==0 and c%2==0:
        return ((b),(c))
    elif b%2!=0 and c%2!=0 and a%2==0 and d%2==0:
        return ((a),(d))
    elif c%2!=0 and  d%2!=0 and a%2==0 and b%2==0:
        return ((a),(b))
    elif b%2!=0 and  d%2!=0 and a%2==0 and c%2==0:
        return ((a),(c))
    elif a%2!=0 and b%2!=0 and c%2!=0 and d%2==0: 
        return ((d,))
    elif a%2!=0 and c%2!=0 and d%2!=0 and b%2==0:
        return ((b,))
    elif b%2!=0 and c%2!=0 and d%2!=0 and a%2==0:
        return ((a,))
    elif a%2!=0 and b%2!=0 and d%2!=0 and c%2==0:
        return ((c,))
    else:
        return ()