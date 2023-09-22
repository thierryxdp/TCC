def filtra(ls,d):
    r = []
    for e in ls:
        if d(e):
            r.append(d)
    return r