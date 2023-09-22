def filtra_pares(a):
    b = (a[0],)
    c = (a[1],)
    d = (a[2],)
    e = (a[3],)
    f = (a[0], a[1])
    g = (a[0], a[2])
    h = (a[0], a[3])
    i = (a[0], a[1], a[2])
    j = (a[0], a[1], a[2], a[3])
    l = (a[0], a[2], a[3])
    n = (a[1], a[2])
    o = (a[1], a[2], a[3])
    p = (a[1], a[3])
    q = (a[2], a[3])
    if a[0]%2 == 0 and a[1]%2 == 0 and a[2]%2 == 0 and a[3]%2 == 0:
        return j
    elif a[0]%2 == 0 and a[1]%2 == 0 and a[2]%2 == 0:
        return i
    elif a[0]%2 == 0 and a[2]%2 == 0 and a[3]%2 == 0:
        return l
    elif a[1]%2 == 0 and a[2]%2 == 0 and a[3]%2 == 0:
        return o
    elif a[0]%2 == 0 and a[1]%2 == 0:
        return f
    elif a[0]%2 == 0 and a[2]%2 == 0:
        return g
    elif a[0]%2 == 0 and a[3]%2 == 0:
        return h
    elif a[1]%2 == 0 and a[2]%2 == 0:
        return n
    elif a[1]%2 == 0 and a[3]%2 == 0:
        return p
    elif a[2]%2 == 0 and a[3]%2 == 0:
        return q
    elif a[3]%2 == 0:
        return e
    elif a[2]%2 == 0:
        return d
    elif a[1]%2 == 0:
        return c
    elif a[0]%2 == 0:
        return b
    else:
        return ()