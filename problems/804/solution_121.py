def filtra_pares(t):
    x=()
    a=(t[0],)
    b=(t[1],)
    c=(t[2],)
    d=(t[3],)
    if t[0]%2==0 and t[1]%2==0:
        return a+b
    elif t[0]%2==0 and t[2]%2==0:
        return x=a+b
    elif t[3]%2==0:
        return x==x+d
    elif t[0]%2==0 and t[2]%2==0 and t[3]%2==0:
        return x==x+a+c+d
    elif t[0]%2==0 and t[1]%2==0 and t[3]%2==0:
        return x==x+a+b+c
    elif t[2]%2==0:
        return x==x+c
    elif t[2]%2==0 and t[3]%2==0:
        return x==x+c+d
    elif t[1]%2==0 and t[2]%2==0:
        return x==x+b+c
    elif t[0]%2==0:
        return x==x+a
    else:
        return x