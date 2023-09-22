def filtraMultiplo(r,n):
    r = []
    for e in r:
        if e % n == 0:
        r.append(e)
    return r