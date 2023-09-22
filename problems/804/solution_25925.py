def filtra_pares(t):
    if t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        a=(t[0],)
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        a=(t[1],)
        return a
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[2],)
        return a
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[3],)
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        a=(t[0],t[1])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[0],t[2])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[0],t[3])
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[1],t[2])
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[1],t[3])
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        a=(t[0],t[1])
        return a
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        a=(t[2],t[3])
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[0],t[1],t[2])
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[0],t[1],t[3])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        a=(t[0],t[2],t[3])
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[1],t[2],t[3])
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[0],t[1],t[2])
        return a
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        a = tuple(t)
        return a
    else:
        a=()
        return a