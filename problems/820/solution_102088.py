def posLetra(s, l, n):
    a = -1
    b = 0
    c = 0
    while c <= len(s):
        if c == l:
            a = s.index(c)
            b = b + 1
        c = c + 1
    if b < n:
        return -1
    else:
        return a