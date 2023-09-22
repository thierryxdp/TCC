def posLetra(s, l, n):
    o = 0
    for i, si in enumerate(s):
        if si == l:
            o += 1
        if o == n:
            return i
    return -1