def posLetra(s, l, n):
    pos = s.find(l)
    while pos >= 0 and n > 1:
        pos = s.find(l, pos + 1)
        n -= 1
    return pos