def posLetra(s, l, n):
    a = -1
    b = 0
    i = o
    while i in range(len(s)):
        if i == l:
            a = s.index(l)
            b = b + 1
            i = i + 1
    if b < n:
        return -1
    else:
        return a