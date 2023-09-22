def filtra_pares(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res