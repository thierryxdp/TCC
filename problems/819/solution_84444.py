def filtraMultiplos(ls,d):
    r = []
    for e in ls:
        if d(e):
            r.append(d)
    return r