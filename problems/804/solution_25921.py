def filtra_pares(t):
    if t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return t
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2==0:
        return t[1:4]
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        return t[2:4]
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        return t[3:4]
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        a=()
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2!=0:
        return t[:1]
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return t[:2]
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return t[:3]
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2!=0:
        return t[1:2]
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return t[1:3]
    elif t[0]%2==0 and t[1]%2==0 and t[2]%2==0 and t[3]%2!=0:
        return t[:3]
    elif t[0]%2!=0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        return t[2:3]
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2!=0:
        a=(t[0],t[2])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        a=(t[0],t[2],t[3])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[0],t[3])
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[1],t[3])
        return a
    elif t[0]%2!=0 and t[1]%2==0 and t[2]%2!=0 and t[3]%2==0:
        a=(t[1],t[3])
        return a
    elif t[0]%2==0 and t[1]%2!=0 and t[2]%2==0 and t[3]%2==0:
        a=(t[1],t[2],t[3])
        return a