def posLetra(s, l, n):
    a = -1
    b = 0
    for i in s:
        if i == l:
            a = s.index(i)
            b = b + 1
    if b < n:
        return -1
    else:
        return a