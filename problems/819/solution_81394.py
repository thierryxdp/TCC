def filtraMultiplos (l,n):
    nl = []
    p = 0
    while p < len(l):
        if (l[p]%n == 0):
            nl = nl + [l[p]]
        p = p + 1
    return nl