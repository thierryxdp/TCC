def filtra_pares(t):
    x=()
    a=(t[0],)
    b=(t[1],)
    c=(t[2],)
    d=(t[3],)
    if t[0]%2==0 and t[1]%2==0:
        return a+b
    elif t[0]%2==0 and t[2]%2==0:
        return a+b
    elif t[3]%2==0:
        return d
    elif t[0]%2==0 and t[2]%2==0 and t[3]%2==0:
        return a+c+d
    elif t[0]%2==0 and t[1]%2==0 and t[3]%2==0:
        return a+b+c
    elif t[2]%2==0:
        return c
    elif t[2]%2==0 and t[3]%2==0:
        return c+d
    elif t[1]%2==0 and t[2]%2==0:
        return b+c
    elif t[0]%2==0:
        return a
    else:
        return x