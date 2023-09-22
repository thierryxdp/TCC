def faltante(l):
    l.sort()
    i = 1
    c = 0
    x = 0
    while c < len(l):
        if i+1 == l[c]:
            x = i
            i += 1
        i += 1
        c += 1
    return i