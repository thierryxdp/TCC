def faltante(l):
    r = []
    s = []
    a = min(l)
    b = max(l)
    c = list(range(a, b+1))
    i = 0
    while i < len(c):
        if c[i] not in l:
            r.append(c[i])
        elif c[i] in l:
            s.append(c[i])
        elif a == 1 and l == c:
            r.append(b+1)
        elif a != 1 and l == c:
            r.append(a-1)
        i += 1
    return r[0]