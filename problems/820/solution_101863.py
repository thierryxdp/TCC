def posLetra(s, l, n):
    c = []
    i = 0
    while i in range len(s-1):
        if i == l:
            c.append(s.index(i))
            i = i+1
    if len(c) < n:
        return -1
    if len(c) >= n:
        return c[-1]