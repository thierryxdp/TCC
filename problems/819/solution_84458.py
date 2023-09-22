def filtraMultiplos(ls,n):
    r = []
    for e in ls:
        if e%n == 0:
            r.append(e)
    return r