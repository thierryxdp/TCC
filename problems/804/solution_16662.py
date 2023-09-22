def filtra_pares(l1):
    a = l1[0]%2
    b = l1[1]%2
    c = l1[2]%2
    d = l1[3]%2
    if   a==b==c==d==0:
        return  l1[0],l1[1],l1[2],l1[3]
    elif a==b==c==0:
        return  l1[0],l1[1],l1[2]
    elif a==b==d==0:
        return  l1[0],l1[1],l1[3]
    elif b==c==d==0:
        return l1[1],l1[2],l1[3]
    elif a==d==0:
        return  l1[0],l1[3]
    elif a==b==0:
        return  l1[0],l1[1]
    elif a==c==0:
        return  l1[0],l1[2]
    elif b==d==0:
        return l1[1],l1[3]
    elif b==c==0:
        return l1[1],l1[2]
    elif c==d==0:
        return l1[2],l1[3]
    elif a==0:
        return l1[0],
    elif b==0:
        return l1[1],
    elif c==0:
        return l1[2],
    elif d==0:
        return l1[3],
    elif (a!=0) and (b!=0) and (c!=0) and (d!=0):
        return ()