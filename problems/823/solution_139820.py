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
            elif a == 1 and len(l) == 1:
                r.append(2)
            elif a != 1 and l in c:
                r.append(1)
        elif c[i] in l:
            s.append(c[i])
        i += 1
    return r[0]