def posLetra(s, l, n):
    a = -1
    b = 0
    while i in range(len(s)):
        if i == l:
            a = s.index(l)
            b = b + 1
    if b < n:
        return -1
    else:
        return a