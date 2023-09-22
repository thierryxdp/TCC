def posLetra(s, l, n):
    b = 0
    a = 0
    for i in s:
        if i == l:
            b = b + 1
            a = s.index(i)
            s.replace(i, '')
    if b < n:
        return -1
    else:
        return a