def faltante(l):
    r = []
    s = []
    a = min(l)
    b = max(l)
    c = list(range(a, b))
    i = 0
    while i < len(c):
        if c[i] not in l:
            r.append(c[i])
        if a == 1 and len(l) > 1 and l in c:
            r.append(b+1)
        if a == 1 and len(l) == 1:
            r.append(2)
        if a != 1 and l in c:
            r.append(1)
        i += 1
    return r[0]