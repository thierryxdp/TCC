def filtra_pares(e1,e2,e3,e4):
    a = e1%2
    b = e2%2
    c = e3%2
    d = e4%2
    if a==0 and b==0 and c==0 and d == 0:
        return (e1,e2,e3,e4)
    elif a==0 and b==0 and c == 0:
        return (e1,e2,e3)
    elif a==0 and b==0 and d == 0:
        return (e1,e2,e3)
    elif a==0 and c==0 and d == 0:
        return (e1,e3,e4)
    elif a==0 and b==0:
        return (e1,e2)
    elif a==0 and c==0:
        return (e1,e3)
    elif a==0 and d==0:
        return (e1,e4)
    elif a==0:
        return (e1)
    elif b==0 and c==0 and d==0:
        return (e2,e3,e4)
    elif b==0 and c==0:
        return (e2,e3)
    elif b==0 and d==0:
        return (e2,e4)
    elif b==0:
        return (e2)
    elif c==0 and d==0:
        return (e3,e4)
    elif c==0:
        return (e3)
    elif d==0:
        return (e4)
    else:
        return ()