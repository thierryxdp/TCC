def faltante(l):
    numeropeca = len(l) + 1
    r = []
    a = min(l)
    b = max(l)
    c = list(range(a, b))
    i = 0
    while i <= len(c):
        if c[i] not in l:
            r.append(c[i])
    i += 1
    return r[0]