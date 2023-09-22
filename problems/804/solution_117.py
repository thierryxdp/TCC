def filtra_pares(t):
    x=()
    a=(t[0],)
    b=(t[1],)
    c=(t[2],)
    d=(t[3],)
    if a%2==0 and b%2==0:
        return x=x+a+b
    elif a%2==0 and c%2==0:
        return x=x+a+b
    elif d%2==0:
        return x=x+d
    elif a%2==0 and c%2==0 and d%2==0:
        return x=x+a+c+d
    elif a%2==0 and b%2==0 and c%2==0:
        return x=x+a+b+c
    elif c%2==0:
        return x=x+c
    elif c%2==0 and d%2==0:
        return x=x+c+d
    elif b%2==0 and c%2==0:
        return x=x+b+c
    elif a%2==0:
        return x=x+a
    else:
        return x