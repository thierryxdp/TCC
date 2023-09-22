def faltante (l):
    ndp = list(range(len(l)+2))
    ndp.remove (0)
    for e in ndp:
        if e not in l:
            return e